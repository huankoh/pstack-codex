---
name: arena
description: "Spawn N parallel candidates at the same task, pick a base, graft the strongest parts of the losers into it. Use for /arena, 'arena this', 'throw it in the arena', or when one attempt at a non-trivial artifact would lock in the wrong shape."
---

# Arena

Fan out N parallel attempts at the same task. Read every candidate end to end. Pick the strongest as the base. Graft the best ideas from the others into it. Verify the synthesized result.

## Start

Track a checklist with one entry per phase before launching anything; use the Codex host's plan tool when available.

1. Frame
2. Fan out
3. Cross-judge
4. Pick
5. Graft
6. Verify

## Phase A: Frame

The N candidates will receive the same prompt, so the prompt is the contract.

1. State the artifact each candidate is producing.
2. Derive the rubric. State what success looks like for *this* task, then turn it into 3-6 concrete gradeable criteria. The rubric is the picker's tool in Phase D. Candidates only see the task.
3. Pick the runners. Use the `arena runners` line in `pstack-models.md`. If the sheet or that line is missing, run one each on the defaults in [Models](#models). An `auto` or `inherit-parent` entry in this line or the cross-judge line means the parent model, so omit `model` for it. If a requested model or effort is unavailable on this host, report it and ask the user to choose a replacement before that seat runs. Spawn more when the arena covers multiple design directions. Same model N times when the work is generation-bound rather than judgment-sensitive.
4. Assign output paths. Each candidate that edits repository files gets a separate physical checkout, using [local worktrees](../poteto-mode/references/local-worktrees.md), plus an absolute output path. Candidates producing only separate standalone artifacts may use `/tmp/arena-<slug>/candidate-<n>/`. A branch name or output subdirectory alone does not isolate edits to a shared checkout. This follows the **separate-before-serializing-shared-state** principle skill.

## Phase B: Fan out

Launch all N `spawn_agent` calls in parallel, each with a distinct `task_name`, the task, the path to shared grounding, its own absolute output path and, for repository writers, its checkout and expected starting revision, and instructions to produce both the artifact and a short rationale. Use `message` for that brief; Codex has no `cwd` or `run_in_background` spawn field. Ask each writer to verify its checkout and revision before editing.

Each rationale names the alternatives the candidate considered and what it rejected.

If a candidate fails to produce output, proceed with N-1 and note the dropout in the synthesis record.

## Phase C: Cross-judge

After all Phase B candidates complete, choose one model from the `arena cross-judge pool` line in `pstack-models.md`. If the sheet or that line is missing, choose from the runner defaults in [Models](#models). Prefer a different model from the parent's. Spawn one judge with `spawn_agent` on that model, `fork_turns: "none"` where supported, and an explicit no-write instruction (Codex has no `readonly` spawn field). It sees the rubric and the candidates by path label, scores each criterion, and recommends a base with rationale. It runs in parallel with the parent's reading in Phase D, not with the candidates themselves. Don't spawn the judge while candidates are still writing.

## Phase D: Pick a base

Read every candidate end to end before picking.

Score each candidate against the rubric criterion by criterion, not on holistic feel. Compare against the cross-judge. Agreement on the base confirms the pick. Disagreement means one of you is biased or the rubric was ambiguous. Read both rationales before deciding.

Pick the base on which candidate a future maintainer can extend most easily without breaking invariants. Prefer the cleaner boundary or smaller API when two feel tied, per the Laziness Protocol.

Record the pick and the reason in a short synthesis note alongside the base artifact, including the cross-judge's verdict.

## Phase E: Graft

Walk each losing candidate once more and identify what is worth porting into the base. The signal is usually one or two things per candidate, not most of it.

Fold each graft in by hand, per the **redesign-from-first-principles** principle skill. Don't paste mechanically. The result has to remain coherent under one mental model.

Record what was grafted, from which candidate, and what was rejected and why.

When N candidates converge on the same shape, that is a strong agreement signal. Note the convergence in the record and ship the consensus shape. No graft is needed. When N candidates wildly diverge, Phase A was under-specified. Reframe and re-run rather than averaging the divergence.

## Phase F: Verify

The synthesized artifact has to hold up under the same scrutiny as any other output, per the **prove-it-works** principle skill.

If verification surfaces a problem the arena did not catch, either Phase A was wrong (re-frame and re-run) or one candidate caught it and you missed the graft (go back to Phase E). Don't paper over.

When the judge and candidate reports are captured, stop completed child agents with `interrupt_agent` where available.

## Outputs

One synthesized artifact. One short synthesis note alongside, naming the base, the grafts (with source candidate), the rejections, the dropouts if any, and the verification result.

## Models

Role defaults come from this plugin's `models.json`. A matching role line in the Codex `pstack-models.md` override sheet takes precedence; `setup-pstack` records that sheet's location. Preserve aliases: `auto` and `inherit-parent` omit `model` so the parent model is inherited. If a requested model or effort is unavailable on this host, report the limitation and ask the user to choose a replacement before continuing that step. Do not silently substitute or lower effort.

- arena runners: `gpt-6-astra`, `gpt-6.1-sol`, `gpt-6-luna`
- arena cross-judge pool: `gpt-6-astra`, `gpt-6.1-sol`, `gpt-6-luna`

## Reasoning effort

A role value may name effort after the model, for example `gpt-6.1-sol @xhigh`. Without `@`, use the sheet's `default effort` (`session` if absent); `session` omits `reasoning_effort`. Pass an explicit level through `spawn_agent.reasoning_effort` where supported. Every `gpt-6-luna` dispatch requests `max`, including configured panel seats. If that effort is unavailable, apply the model/effort limitation rule above.
