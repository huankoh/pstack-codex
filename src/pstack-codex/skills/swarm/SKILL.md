---
name: swarm
description: "Fan out N parallel workers, drain them, and return one report. Use for /swarm, 'swarm this', or parallel coverage, races, gauntlets, and exploration."
---

# Swarm

Fan out N parallel workers. They may cover separate slices, race the same brief, or mix both. The parent waits, aggregates, and returns one report.

## Start

Track a checklist with one entry per phase before launching anything; use the Codex host's plan tool when available.

1. Frame
2. Fan out
3. Aggregate
4. Report

## Phase A: Frame

1. State the done predicate and the artifact or report the swarm must return.
2. Choose the shape. Partition into slices, race N workers on identical briefs, or mix both. For a race or mixed shape, declare `first pass`, `rank all`, or `best-of` before spawning.
3. Set N from the user or derive it from the shape. N is total workers, not the number that run at once.
4. Pick the worker model from the `swarm workers` line in `pstack-models.md`. If the sheet or that line is missing, use the default in [Models](#models). For `auto` or `inherit-parent`, omit `model` so the workers run on the parent model. If a requested model or effort is unavailable, report it and ask the user to choose a replacement before that worker runs. For a model race, name each arm's model up front.
5. Give each writing worker a separate physical checkout through [local worktrees](../poteto-mode/references/local-worktrees.md), an absolute path, and its own writable output. A branch name or output subdirectory alone does not isolate writes to one checkout. When workers verify or measure commits, each brief names the exact SHAs. A measurement brief also names the method (sample count, what one sample is, order). The worker records both in its result.

## Phase B: Fan out

Launch all N `spawn_agent` calls in parallel, each with a distinct `task_name`, independent `message`, and the step 4 `model`, omitted for `auto` or `inherit-parent`. Include the absolute checkout and expected revision in every writing brief; each worker verifies them before editing. Codex has no `cwd`, isolation, or `run_in_background` spawn field.

When a worker must start from a non-default branch, check that branch out in the worker's own worktree and name the worktree path in its brief.

Every brief stands alone. Include the goal, scope, exact slice or race arm, how to verify, and what to report. Reports use `PASS`, `ISSUES`, or `BLOCKED` with evidence. A worker that can prove a defect reports `ISSUES` and lists every issue it can prove, not only the first.

If a worker drops out, proceed with N-1 and note it.

## Phase C: Aggregate

Read the terminal results. Drop a result that does not record the SHAs and method its brief names, and rerun that worker once. After a second miss, record a gap. A gap does not count as a pass. For coverage, every required slice needs a result. For a race, apply the selection rule declared up front. Use first pass, rank all, or best-of. Do not paste raw worker dumps.

Keep a compact result table, one-line evidenced issues, and explicit gaps or dropouts.

Stop completed workers with `interrupt_agent` where available after their reports are captured.

## Phase D: Report

Return one consolidated in-chat report with the table, issue one-liners, gaps or dropouts, and the race rule when used.

## Models

Role defaults come from this plugin's `models.json`. A matching role line in the Codex `pstack-models.md` override sheet takes precedence; `setup-pstack` records that sheet's location. Preserve aliases: `auto` and `inherit-parent` omit `model` so the parent model is inherited. If a requested model or effort is unavailable on this host, report the limitation and ask the user to choose a replacement before continuing that step. Do not silently substitute or lower effort.

- swarm workers: `gpt-6-sol`

## Reasoning effort

A role value may name effort after the model, for example `gpt-6-sol @xhigh`. Without `@`, use the sheet's `default effort` (`session` if absent); `session` omits `reasoning_effort`. Pass an explicit level through `spawn_agent.reasoning_effort` where supported. Every `gpt-6-luna` dispatch requests `max`, including configured panel seats. If that effort is unavailable, apply the model/effort limitation rule above.
