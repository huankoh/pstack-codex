---
name: reflect
description: Spawn three parallel review subagents over the active transcript, surface learnings, and route each to a concrete edit on an existing skill. Use when the user says reflect.
---

# Reflect

Mine the current conversation for durable learnings, then route them into skill edits.

## When to invoke

Invoke when the user says "reflect" or "/reflect". Skip when the conversation is trivial, off-topic, or already covered by an existing skill the parent followed correctly. One-offs are not learnings.

## Process

### 1. Locate the active transcript

The parent identifies the active Codex chat and exact workspace before fanning out. Follow [Codex transcript evidence](references/codex-transcripts.md): use the active thread id when available and a distinctive opening prompt fragment, inspect only the matched workspace's rollout, and read the full relevant records for exact claims. Do not content-scan unrelated chats. If the rollout is unavailable or ambiguous, write a tight digest of the session and pass that instead; label the digest and its evidence limit.

### 2. Spawn three reviewers in parallel

Three parallel `spawn_agent` calls with `agent_type: "default"`, with `model` set as below. Reviewers need MCP access for context lookups (tickets, chat threads, observability traces referenced in the transcript). Use available context lookup tools. The prompt forbids file writes. The parent applies edits.

Each reviewer and the synthesizer name a role line in `pstack-models.md` and a default in [Models](#models). Set `model` to that line's value, or to the default if the sheet or line is missing. Leave `model` unset for `auto` or `inherit-parent`. Request any configured effort via `reasoning_effort`; otherwise retain session effort. If the requested model or effort is unavailable, report it and ask for a replacement before that step.

| Lens | Role line | Prompt template |
|---|---|---|
| Judgment | `reflect judgment, divergent, synthesizer` | `references/judgment-reviewer.md` |
| Tooling | `reflect tooling` | `references/tooling-reviewer.md` |
| Divergent | `reflect judgment, divergent, synthesizer` | `references/divergent-reviewer.md` |

Pass each template verbatim, substituting the transcript path or digest where marked. Use `fork_turns: "none"` when the host supports it, with a complete brief. The reviewers must have available context lookup tools and must not write files; a prompt restriction alone is not an enforced read-only sandbox. Reviewers return findings to the parent. Interrupt completed children.

### 3. Synthesize

One `spawn_agent` call with `agent_type: "default"` and `model` from the `reflect judgment, divergent, synthesizer` line (default in [Models](#models)). Use available context lookup tools. The synthesizer's quality check includes spot-verifying citations, which can require MCP access. Use `references/synthesizer.md` verbatim, with each reviewer's full output inlined where marked. The synthesizer returns a structured Accepted / Rejected / Backlog list.

### 4. Structural enforcement check

Sanity-check the synthesizer's Accepted list. For any item that would be enforced more reliably by a lint rule, script, metadata flag, or runtime check, move it from Accepted to Backlog. See the **encode-lessons-in-structure** principle skill.

### 5. Apply

Before applying any Accepted edit, present the synthesizer's full Accepted/Rejected/Backlog output to the user and wait for explicit approval. The user picks which subset to apply and may redirect routings. Skill changes affect every future agent in the org. Do not auto-apply.

Backlog items file to whatever devex / backlog tracker your team uses automatically. Only the Accepted list waits for approval.

For each approved Accepted item, follow the Routing field exactly. Use the available Codex `skill-creator`; if it is unavailable, report the affected authoring step as unavailable and ask for a replacement:

- Trivial existing-skill edit (a one-line bullet, a tightened sentence, a stale fact corrected): parent does directly.
- Substantive existing-skill edit (a new section, a new pattern table, more than ~10 lines): hand to the **skill-creator** skill to draft, validate, test the relevant behavior, and iterate on observed failures.
- `tune description: <skill path>` (the skill exists but didn't trigger when it should have): use `skill-creator` to refine the description, test representative requests that should and should not trigger it, and iterate on observed misrouting.
- `new skill via skill-creator: <kebab-name>`: hand creation to `skill-creator`. Do not invent the shape ad hoc.

If your environment ships a SKILL.md validator, run it on every touched skill before declaring done. Skip this step if it doesn't.

### 6. Summarize for the user

Short list, no preamble:

- Edits applied: `<skill path>`. What changed, one line each.
- New skills created: `<skill path>`. One line each (rare).
- Backlog filed to the devex tracker: `<issue title>` (`<tags>`). One line each.
- Dropped: one line per rejected finding + reason from the synthesizer.

## Models

Role defaults come from this plugin's `models.json`. A matching role line in the `pstack-models.md` override sheet overrides each at runtime; `/setup-pstack` writes it and lists its path per runtime.

- reflect tooling: `gpt-6.1-sol`
- reflect judgment, divergent, synthesizer: `gpt-6.1-sol`

## Reasoning effort

A role value in the override sheet may name a reasoning effort after its model, as in `gpt-6.1-sol @xhigh`. A value without `@` takes the sheet's `default effort` line, a level or `session`; absent that line, retain session effort. `auto` and `inherit-parent` omit the model argument. Pass an explicit effort as `spawn_agent.reasoning_effort`. Every Luna dispatch requests `max`, including one selected by an override sheet. If the host rejects the requested model or effort, pause that affected dispatch and ask the user for a replacement.
