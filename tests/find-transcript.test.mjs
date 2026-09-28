import { afterEach, describe, expect, test } from "bun:test";
import { spawnSync } from "node:child_process";
import { mkdirSync, mkdtempSync, rmSync, utimesSync, writeFileSync } from "node:fs";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { candidates, findTranscript, metadata, openingPrompt } from "../src/pstack-codex/skills/reflect/scripts/find-transcript.mjs";
import { readTranscript } from "../src/pstack-codex/skills/reflect/scripts/read-transcript.mjs";

const finder = join(import.meta.dir, "../src/pstack-codex/skills/reflect/scripts/find-transcript.mjs");
const reader = join(import.meta.dir, "../src/pstack-codex/skills/reflect/scripts/read-transcript.mjs");
const roots = [];
afterEach(() => { for (const root of roots.splice(0)) rmSync(root, { recursive: true, force: true }); });
function setup() {
  const root = mkdtempSync(join(tmpdir(), "codex-rollout-")); roots.push(root);
  const sessions = join(root, "sessions"); const workspace = join(root, "project"); const other = join(root, "other");
  mkdirSync(sessions); mkdirSync(workspace); mkdirSync(other);
  return { root, sessions, workspace, other };
}
const row = (type, payload, timestamp = "2026-09-27T10:00:00Z") => JSON.stringify({ timestamp, type, payload });
function rollout(env, id, cwd, lines = [], mtime = 100, extras = {}) {
  const dir = join(env.sessions, "2026", "09", "27"); mkdirSync(dir, { recursive: true });
  const path = join(dir, `rollout-${id}.jsonl`);
  writeFileSync(path, [row("session_meta", { id, cwd, ...extras }), ...lines].join("\n") + "\n");
  utimesSync(path, mtime, mtime); return path;
}
const user = (s) => row("response_item", { type: "message", role: "user", content: [{ type: "input_text", text: s }] });
const event = (s) => row("event_msg", { type: "user_message", message: s });

describe("Codex rollout reader", () => {
  test("finds only a unique workspace and thread scoped chat", async () => {
    const e = setup();
    const own = rollout(e, "own", e.workspace, [user("fix login"), event("fix login")], 100);
    rollout(e, "foreign", e.other, [event("fix login")], 300);
    rollout(e, "child", e.workspace, [event("fix login")], 200, { parent_thread_id: "own" });
    rollout(e, "native-child", e.workspace, [event("fix login")], 250, { source: { subagent: { thread_spawn: { parent_thread_id: "own", depth: 1 } } } });
    expect(candidates(e.sessions)).toHaveLength(4);
    expect(await findTranscript(e.sessions, e.workspace, "fix login")).toBe(own);
    expect(await metadata(own)).toMatchObject({ id: "own", cwd: e.workspace });
    expect(await openingPrompt(own)).toBe("fix login");
    expect(await findTranscript(e.sessions, e.workspace, "fix login", "own")).toBe(own);
    expect(await findTranscript(e.sessions, e.other, "fix login", "own")).toBeNull();
    const hit = spawnSync("node", [finder, e.sessions, e.workspace, "fix login", "--thread-id", "own"], { encoding: "utf8" });
    expect(hit.status).toBe(0); expect(hit.stdout.trim()).toBe(own);
  });

  test("ambiguous prompts fail instead of choosing newest", async () => {
    const e = setup();
    rollout(e, "one", e.workspace, [event("same prompt")]);
    rollout(e, "two", e.workspace, [event("same prompt")], 200);
    expect(await findTranscript(e.sessions, e.workspace, "same prompt")).toBeNull();
    const miss = spawnSync("node", [finder, e.sessions, e.workspace, "same prompt"], { encoding: "utf8" });
    expect(miss.status).toBe(1); expect(miss.stderr).toContain("no unique");
  });

  test("opening prompt ignores injected setup user text before the real user event", async () => {
    const e = setup();
    const path = rollout(e, "actual", e.workspace, [
      user("AGENTS.md instructions for this workspace"),
      row("turn_context", { cwd: e.workspace }),
      event("Implement the requested feature"),
    ]);
    expect(await openingPrompt(path)).toBe("Implement the requested feature");
    expect(await findTranscript(e.sessions, e.workspace, "AGENTS.md")).toBeNull();
    expect(await findTranscript(e.sessions, e.workspace, "requested feature")).toBe(path);
    const noEvent = rollout(e, "no-event", e.workspace, [user("possibly injected user text")]);
    expect(await openingPrompt(noEvent)).toBeNull();
  });

  test("parses messages, tool calls and outputs with source lines and reports malformed records", async () => {
    const e = setup();
    const path = rollout(e, "run", e.workspace, [
      user("audit"),
      row("response_item", { type: "function_call", name: "exec_command", call_id: "c1", arguments: '{"cmd":"cat x"}' }),
      row("response_item", { type: "function_call_output", call_id: "c1", output: "x contents" }),
      row("response_item", { type: "custom_tool_call", name: "apply_patch", call_id: "c2", input: "*** Begin Patch" }),
      row("response_item", { type: "custom_tool_call_output", call_id: "c2", output: "ok" }),
      row("response_item", { type: "web_search_call", query: "source" }),
      "{bad",
      row("response_item", { type: "message", role: "assistant", content: [{ type: "output_text", text: "done" }] }, "2026-09-27T11:00:00Z"),
    ]);
    const result = await readTranscript(path, e.workspace);
    expect(result.malformed_lines).toEqual([8]);
    expect(result.records.map((r) => [r.line, r.payload.type])).toEqual([[2, "message"], [3, "function_call"], [4, "function_call_output"], [5, "custom_tool_call"], [6, "custom_tool_call_output"], [7, "web_search_call"], [9, "message"]]);
    expect(result.records[1].payload).toMatchObject({ call_id: "c1", name: "exec_command", arguments: '{"cmd":"cat x"}' });
    expect(result.records[2].payload.output).toBe("x contents");
    expect(result.records[4].payload.output).toBe("ok");
    expect((await readTranscript(path, e.workspace, { to: "2026-09-27T10:30:00Z" })).records).toHaveLength(6);
    await expect(readTranscript(path, e.workspace, { from: "2026-09-27T12:00:00Z", to: "2026-09-27T10:00:00Z" })).rejects.toThrow("from must not exceed");
    await expect(readTranscript(path, e.workspace, { from: "yesterday" })).rejects.toThrow("ISO8601");
    await expect(readTranscript(path, e.other)).rejects.toThrow("workspace identity");
    const cli = spawnSync("node", [reader, path, e.workspace], { encoding: "utf8" });
    expect(cli.status).toBe(0); expect(JSON.parse(cli.stdout).records).toHaveLength(7);
    const badCli = spawnSync("node", [reader, path, e.workspace, "--from", "yesterday"], { encoding: "utf8" });
    expect(badCli.status).toBe(1);
  });

  test("record shape gaps and original source line numbers remain visible", async () => {
    const e = setup();
    const path = rollout(e, "shapes", e.workspace, [
      "null", "[]", "42",
      JSON.stringify({ type: "response_item", line: 999, payload: { type: "function_call_output", output: "evidence" } }),
    ]);
    const full = await readTranscript(path, e.workspace);
    expect(full.malformed_lines).toEqual([2, 3, 4]);
    expect(full.untimed_lines).toEqual([5]);
    expect(full.records[0].line).toBe(5);
    expect(full.records[0].payload.output).toBe("evidence");
    const bounded = await readTranscript(path, e.workspace, { from: "2026-09-27T00:00:00Z" });
    expect(bounded.records).toEqual([]);
    expect(bounded.untimed_lines).toEqual([5]);
  });

  test("malformed or missing identity never unlocks content", async () => {
    const e = setup();
    const dir = join(e.sessions, "2026", "09", "27"); mkdirSync(dir, { recursive: true });
    const path = join(dir, "rollout-no-meta.jsonl"); writeFileSync(path, `${user("secret")}\n`);
    expect(await metadata(path)).toBeNull();
    expect(await findTranscript(e.sessions, e.workspace, "secret")).toBeNull();
    await expect(readTranscript(path, e.workspace)).rejects.toThrow("workspace identity");
    const laterMeta = join(dir, "rollout-later-meta.jsonl");
    writeFileSync(laterMeta, `{bad\n${row("session_meta", { id: "later", cwd: e.workspace })}\n${event("secret")}\n`);
    expect(await metadata(laterMeta)).toBeNull();
    expect(await findTranscript(e.sessions, e.workspace, "secret")).toBeNull();
    const importRun = spawnSync("node", ["-e", `import(${JSON.stringify(reader)}).then(() => console.log("ok"))`, "not-a-file"], { encoding: "utf8" });
    expect(importRun.status).toBe(0); expect(importRun.stdout.trim()).toBe("ok");
  });
});
