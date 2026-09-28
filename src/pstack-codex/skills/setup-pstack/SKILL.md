---
name: setup-pstack
description: Configure which models pstack uses per role. Detects available Codex models and writes the model override sheet. Use for /setup-pstack, "configure pstack models", changing pstack's model choices, or turning the SessionStart hook on or off.
---

# Setup pstack

Write Codex's per-role model override sheet at `<codex-home>/pstack-models.md`, where `<codex-home>` is `$CODEX_HOME` when set and `~/.codex` otherwise. Each pstack skill names a default model inline; the override sheet records the user's choices from the models available on this host. Preserve the existing 17 roles and default panel counts; an explicitly configured panel list still determines its count.

The sheet and hook setting are shared across projects. Choosing project scope below changes where the rows load, not where the sheet is stored or whether it is project-specific. Explain this scope before confirmation.

The model rows and default effort load through `<codex-home>/AGENTS.md`, or the project's `AGENTS.md` when the user chooses project scope. Codex does not use Claude-style `@` file includes. The session hook reads its setting directly from the sheet.

## Steps

### 1. Detect available models

Inspect the exposed subagent tool's accepted `model` and `reasoning_effort` values and the host's model listing. Use only confirmed model IDs. Do not infer subagent choices from a root-model picker or assume desktop, CLI, and cloud expose identical controls. Ask the user to confirm or supply additional model IDs they want checked. Never write an unverified real model ID as available. The aliases `inherit-parent` and `auto` remain valid choices: both omit `model` from the subagent call. If the host cannot honor a requested model or effort, report the limitation and ask for a replacement before continuing that step.

### 2. Load current state

The default role-to-model mapping is the sheet below. If the sheet exists, read it and treat its values as the current choices. Otherwise start from the defaults. A line whose role is not in that shape, such as `how critics`, is from a retired role. Drop it. Mark legacy Claude or other unavailable model names as needing a user choice; do not silently substitute a Codex model.

### 3. Map and confirm

Show every role with its current model, marking any real ID not in the detected set as needing a choice. List each line step 2 dropped or flagged. Ask whether to accept as-is or change specific roles, offering detected models plus `inherit-parent` and `auto`. Prefer the host's structured question tool when its supported mode and permitted question types fit; otherwise ask in text and await the answer.

For panel roles (arena runners, architect runners, interrogate reviewers), the value is a list and one subagent runs per entry, aliases included; list length sets the count. `arena cross-judge pool` is also a list, but Arena selects one judge whose model differs from the parent's when possible. Different Astra, Sol, and Luna models provide the configured model diversity; do not claim they are separate providers. `swarm workers` supplies the default for each worker unless a race or comparison assigns a model per arm.

Then ask for the `default effort`: `session` keeps the configured/session effort, or choose a supported level. Ask whether any role should use a different supported level. A role value may carry `@<level>`, such as `gpt-6-sol @xhigh`; panel entries take their own suffix. Pass an explicit level through `reasoning_effort` when the exposed schema supports it; `session` omits that argument. Do not dispatch through unregistered effort-agent types. Luna assignments request `max`, including panel entries; Luna does not support `ultra`. Retain configured/session effort for Sol and Astra unless the user changes it. If the selected host cannot honor a choice, report it and ask; never silently lower the effort.

### 4. Choose whether the session hook routes tasks

On a Codex host supporting plugin hooks, the plugin's `SessionStart` hook injects the poteto-mode mandate on startup, resume, clear, and compact. The host may require trust through `/hooks` before running it. Check actual support and trust state; do not claim an uninstalled or untrusted hook has run. Ask whether to keep the hook. The default is on. Write `session hook: on` or `session hook: off` in the sheet. No sheet or no line retains the upstream on default. Report an unsupported host rather than inventing another startup mechanism.

### 5. Validate

Every real model ID must be confirmed available for the intended subagent call; aliases remain valid. Validate the model without its `@<level>` suffix and each level against that model's accepted efforts on this host. `default effort` is a supported level or `session`. Validate Luna's effective effort as `max`. If a requested model, effort, or inheritance control cannot be honored, stop the affected step and ask for a replacement.

### 6. Write the override sheet

Write `<codex-home>/pstack-models.md` with the shape below, using the confirmed choices. Overwrite the sheet so reruns stay idempotent.

```markdown
# pstack model configuration

Per-role overrides for pstack-codex. Each skill names its defaults. Delete a role line to restore its skill default. `inherit-parent` and `auto` omit the subagent model argument; an alias in a panel still counts as one entry. A model may carry an effort suffix, such as `gpt-6-sol @xhigh`, dispatched through `reasoning_effort`. `default effort` governs entries without a suffix; `session` retains configured/session effort. All Luna assignments request `max`. If the host cannot honor a requested model or effort, report it and ask before continuing that step. `session hook: off` disables the supported plugin SessionStart hook; no line leaves it on.

feature, refactoring: gpt-6-sol
bug-fix: gpt-6-astra
perf-issue: gpt-6-astra
hillclimb: gpt-6-astra
judgment and prose: gpt-6-sol
strongest judgment: gpt-6-astra
how explorer: gpt-6-luna @max
how explainer: gpt-6-sol
why investigators: gpt-6-sol
why synthesizer: gpt-6-sol
reflect tooling: gpt-6-sol
reflect judgment, divergent, synthesizer: gpt-6-sol
arena runners: gpt-6-astra, gpt-6-sol, gpt-6-luna @max
arena cross-judge pool: gpt-6-astra, gpt-6-sol, gpt-6-luna @max
swarm workers: gpt-6-sol
architect runners: gpt-6-astra, gpt-6-sol, gpt-6-luna @max
interrogate reviewers: gpt-6-astra, gpt-6-sol, gpt-6-luna @max

default effort: session
session hook: on
```

### 7. Wire it in

Copy or update the model rows and `default effort` in `<codex-home>/AGENTS.md`, preserving unrelated instructions. If the user chose project scope, use that project's `AGENTS.md` instead. Do not copy the `session hook` line there: the plugin hook reads it directly from `<codex-home>/pstack-models.md`. Do not add an `@` include. Keep the confirmed scope and avoid duplicate stale role blocks on reruns.

### 8. Confirm

Tell the user where the sheet was written, how the model rows load, and whether the hook is configured on and actually supported/trusted. Re-running this skill updates the sheet. Disclose any capability that remains unavailable on this host.

## Models

Defaults are recorded in the plugin's [models.json](../../models.json). Keep this sheet and the model-consuming skills consistent with that file when maintaining the package.

- Native model defaults: `gpt-6-astra`, `gpt-6-sol`, `gpt-6-luna`; availability must be checked on the current host.
- Default panel: `gpt-6-astra`, `gpt-6-sol`, `gpt-6-luna @max`.
- Effort levels retained by the sheet: `low`, `medium`, `high`, `xhigh`, `max`, subject to the selected model and host.
- Default reasoning effort: `session`; every Luna assignment requests `max`.
- Single-role default: `gpt-6-sol`; strongest: `gpt-6-astra`.
