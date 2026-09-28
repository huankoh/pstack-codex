#!/usr/bin/env node
// Locate a Codex rollout within one explicitly named workspace. Read metadata
// before inspecting prompts so unrelated conversations are never content-scanned.
import { createReadStream, readdirSync, realpathSync, statSync } from "node:fs";
import { join, resolve } from "node:path";
import process from "node:process";
import { createInterface } from "node:readline";
import { fileURLToPath } from "node:url";

export function candidates(sessionsDir) {
  const files = [];
  const walk = (dir, depth) => {
    for (const entry of readdirSync(dir, { withFileTypes: true })) {
      const full = join(dir, entry.name);
      if (entry.isFile() && /^rollout-.*\.jsonl$/.test(entry.name)) files.push(full);
      else if (entry.isDirectory() && depth < 3) walk(full, depth + 1);
    }
  };
  walk(sessionsDir, 0);
  return files.map((path) => ({ path, mtime: statSync(path).mtimeMs }))
    .sort((a, b) => b.mtime - a.mtime).map(({ path }) => path);
}

async function* records(path) {
  const stream = createReadStream(path, { encoding: "utf8" });
  const lines = createInterface({ input: stream, crlfDelay: Infinity });
  try {
    for await (const line of lines) {
      try { yield JSON.parse(line); } catch { continue; }
    }
  } finally {
    lines.close();
    stream.destroy();
  }
}

export async function metadata(path) {
  // The identity record must be the first line. A damaged first line must not
  // be rescued by a later record, which could belong to another conversation.
  const stream = createReadStream(path, { encoding: "utf8" });
  const lines = createInterface({ input: stream, crlfDelay: Infinity });
  try {
    for await (const line of lines) {
      let record;
      try { record = JSON.parse(line); } catch { return null; }
      return record?.type === "session_meta" ? record.payload : null;
    }
  } finally { lines.close(); stream.destroy(); }
  return null;
}

export function messageText(payload) {
  if (typeof payload?.message === "string") return payload.message;
  if (payload?.type !== "message" || payload.role !== "user") return null;
  return Array.isArray(payload.content)
    ? payload.content.filter((block) => ["input_text", "text"].includes(block?.type) && typeof block.text === "string")
      .map((block) => block.text).join("\n")
    : null;
}

export async function openingPrompt(path) {
  for await (const record of records(path)) {
    if (record?.type === "event_msg" && record.payload?.type === "user_message")
      return messageText(record.payload);
  }
  // Response-item user text can be injected setup context. If the distinct
  // user_message event is missing, there is no reliable opening prompt.
  return null;
}

export async function findTranscript(sessionsDir, workspace, fragment, threadId = null) {
  const root = realpathSync(resolve(workspace));
  const hits = [];
  for (const path of candidates(sessionsDir)) {
    const meta = await metadata(path);
    if (!meta || typeof meta.cwd !== "string" || typeof meta.id !== "string") continue;
    if (meta.parent_thread_id || meta.agent_role || meta.agent_path ||
        (meta.source && typeof meta.source === "object" && Object.hasOwn(meta.source, "subagent"))) continue;
    let cwd;
    try { cwd = realpathSync(resolve(meta.cwd)); } catch { continue; }
    if (cwd !== root || (threadId && meta.id !== threadId)) continue;
    const prompt = await openingPrompt(path);
    if (prompt?.includes(fragment)) hits.push(path);
  }
  return hits.length === 1 ? hits[0] : null;
}

async function main(argv) {
  const [sessionsDir, workspace, fragment, flag, threadId] = argv;
  if (!sessionsDir || !workspace || !fragment || (flag && flag !== "--thread-id") || (flag && !threadId)) {
    console.error("usage: find-transcript.mjs <sessions-dir> <workspace-dir> <opening-prompt-fragment> [--thread-id <id>]");
    return 2;
  }
  const path = await findTranscript(sessionsDir, workspace, fragment, threadId);
  if (!path) {
    console.error("no unique workspace-scoped transcript matched; supply the active thread id or use a digest");
    return 1;
  }
  console.log(path);
  return 0;
}

function invokedDirectly() {
  if (!process.argv[1]) return false;
  try { return fileURLToPath(import.meta.url) === realpathSync(process.argv[1]); }
  catch { return false; }
}

if (invokedDirectly()) process.exitCode = await main(process.argv.slice(2));
