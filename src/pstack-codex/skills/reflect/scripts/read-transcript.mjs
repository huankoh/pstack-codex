#!/usr/bin/env node
// Read one already identified Codex rollout, retaining line numbers for claims.
import { createReadStream, realpathSync } from "node:fs";
import { resolve } from "node:path";
import { createInterface } from "node:readline";
import { fileURLToPath } from "node:url";
import { metadata } from "./find-transcript.mjs";

function parseBounds({ from = null, to = null }) {
  const parse = (value) => {
    if (value === null) return null;
    if (typeof value !== "string" || !/^\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d(?:\.\d+)?(?:Z|[+-]\d\d:\d\d)$/.test(value))
      throw new Error("time bound must be ISO8601 with timezone");
    const ms = Date.parse(value);
    if (!Number.isFinite(ms)) throw new Error("invalid time bound");
    return ms;
  };
  const start = parse(from), end = parse(to);
  if (start !== null && end !== null && start > end) throw new Error("from must not exceed to");
  return { start, end };
}

export async function readTranscript(path, workspace, { from = null, to = null } = {}) {
  const { start, end } = parseBounds({ from, to });
  const meta = await metadata(path);
  if (!meta || typeof meta.id !== "string" || !meta.id || typeof meta.cwd !== "string" || realpathSync(resolve(meta.cwd)) !== realpathSync(resolve(workspace)))
    throw new Error("rollout has no matching workspace identity");
  const stream = createReadStream(path, { encoding: "utf8" });
  const lines = createInterface({ input: stream, crlfDelay: Infinity });
  const records = [];
  const malformed = [];
  const untimed = [];
  let lineNumber = 0;
  try {
    for await (const line of lines) {
      lineNumber++;
      let row;
      try { row = JSON.parse(line); } catch { malformed.push(lineNumber); continue; }
      if (!row || typeof row !== "object" || Array.isArray(row) || typeof row.type !== "string") { malformed.push(lineNumber); continue; }
      if (row.type === "session_meta") continue;
      const ms = Date.parse(row.timestamp);
      if (!Number.isFinite(ms)) {
        untimed.push(lineNumber);
        if (start !== null || end !== null) continue;
      }
      if ((start !== null && ms < start) || (end !== null && ms > end)) continue;
      // Preserve complete raw records, including call/result shapes unknown to
      // this version. A projection would hide tool or compaction evidence.
      records.push({ ...row, line: lineNumber });
    }
  } finally { lines.close(); stream.destroy(); }
  return { session_id: meta.id, cwd: meta.cwd, source: path, malformed_lines: malformed, untimed_lines: untimed, records };
}

async function main(argv) {
  const [path, workspace, ...rest] = argv;
  if (!path || !workspace || rest.length % 2) {
    console.error("usage: read-transcript.mjs <rollout-path> <workspace-dir> [--from ISO8601] [--to ISO8601]");
    return 2;
  }
  const opts = {};
  for (let i = 0; i < rest.length; i += 2) {
    if (rest[i] === "--from") opts.from = rest[i + 1];
    else if (rest[i] === "--to") opts.to = rest[i + 1];
    else return 2;
  }
  try { console.log(JSON.stringify(await readTranscript(path, workspace, opts))); return 0; }
  catch (error) { console.error(error.message); return 1; }
}

function invokedDirectly() {
  if (!process.argv[1]) return false;
  try { return realpathSync(process.argv[1]) === realpathSync(fileURLToPath(import.meta.url)); }
  catch { return false; }
}

if (invokedDirectly()) process.exitCode = await main(process.argv.slice(2));
