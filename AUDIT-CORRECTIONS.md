**Approved audit corrections — pstack-codex 0.3.1**

Implemented on 2026-09-28 following the user's approval of the five audit proposals and restoration of original Autopilot-full autonomy. The exact authorization is recorded in [decisions 10–11](NATIVE-PORT-DECISIONS.md). The prior [0.3.0 audit](FAITHFULNESS-AUDIT.md) remains a historical snapshot.

| Approved item | Current behavior | Reference |
| --- | --- | --- |
| Native authoring | Automate-me and Reflect use Codex skill-creator; Reflect's approval gate and authoring validation/iteration remain. Conditional description optimization uses actual triggering examples rather than a nonexistent named native loop. | [Automate-me](src/pstack-codex/skills/automate-me/SKILL.md#L66), [Reflect](src/pstack-codex/skills/reflect/SKILL.md#L48), [synthesizer](src/pstack-codex/skills/reflect/references/synthesizer.md#L17) |
| Delegate continuity | Resume an existing poteto delegate through native follow-up controls. Required fresh independent reviewers remain separate. | [Persona](src/pstack-codex/agents/poteto-agent.md#L3), [delegation](src/pstack-codex/skills/poteto-mode/references/delegation.md#L5) |
| Optional entry points | All 31 prompt wrappers invoke the native skill directly, without the retired mapping detour. | [Example](src/pstack-codex/.codex-plugin/prompts/poteto-mode.md#L7) |
| Scheduled lifecycle | Reuse schedule identity; stop or pause the workflow's heartbeat at its existing completion, stop, hold and terminal conditions; preserve unrelated automations. | [Scheduling](src/pstack-codex/skills/poteto-mode/references/scheduling.md#L6) |
| Plan consistency | The plan's merge action and authorized actor come from the selected execution playbook, preserving its operator-item and review gates. | [Plan template](src/pstack-codex/skills/poteto-mode/playbooks/multi-phase-plan.md#L134) |
| Original autonomy | Under a full-autonomy grant, an Autopilot-full owner can merge after the root's clean verdict and the stronger shipping checks. Operator-named items and explicit interaction review gates still wait for the operator. Autopilot-stack remains operator-landed. | [Autopilot-full](src/pstack-codex/skills/poteto-mode/playbooks/autopilot-full.md#L11) |

This restores **who may merge**, while retaining the Claude improvements to exact-head validity, base/context applicability, destination checks, pending-merge handling and durable verification. All verification lanes, counts, review separation and operator hold semantics remain. The shipping and resume helpers were not changed.

**What happened to verification and invocation rules?**

The verification skills were never removed from our package. [Create verification](src/pstack-codex/skills/create-verification-skill/SKILL.md) builds a project-specific verification skill; [Maintain verification](src/pstack-codex/skills/maintain-verification-skill/SKILL.md) keeps it current. Original setup also offered to create one at the end, when the repository lacked it. That offer was added in [original commit e42d29f](https://github.com/cursor/plugins/commit/e42d29fd5c8fe4f13e3bee7f53b35f410f65aee8). Claude imported the skills, but its rewritten setup lacks that offer. The checked history provides no documented rationale for omitting it. Calling that an intentional removal was stronger than the evidence justified.

The invocation change has a documented reason. In [Claude commit 1d791c8](https://github.com/michael-denyer/pstack-claude/commit/1d791c80c0f0234d420bd39d307f53b5cee6fef6), `disable-model-invocation` was removed from 12 command-paired skills because Claude's Skill tool refused to load them through their slash-command wrappers and startup routing. Reflect, Recall, Automate-me and Show-me-your-work are among the affected skills. It was a Claude-specific loading workaround. Our selected overlay inherited the wider eligibility; those four have no native explicit-only invocation policy. Eligibility does not mean that they should run on every request, and it does not remove their user-approval gates. Native automatic-selection behavior remains untested.

Claude also revised two principles in [commit 430a4f5](https://github.com/michael-denyer/pstack-claude/commit/430a4f5d1fdcba0750ffa21e441ced5114f7d8ce). Attack the Premise now tests the specific shared assumption instead of always requiring a distribution/imbalance census. Test Behavior judges a test by the relevant defect it detects instead of the original fixed assertion checklist. Those are inherited policy changes, not Codex necessities.

The user requested an explanation of these remaining differences. The setup offer, invocation policies and principle bodies were therefore left unchanged in 0.3.1. No further approval was inferred.

**Validation**

- Exact fidelity, metadata, link and inventory validation passed: 55 top-level skills, three nested Benny skills, 23 playbooks, 250 files.
- All 21 Python fidelity/package tests and 21 targeted plan/shipping tests passed. The three edited skills passed the official skill validator.
- Independent Astra review found no actionable issue in the 44-file approved delta.
- Independent Sol action-selection exercises covered seven merge cases and nine scheduling cases. Decisions preserved autonomous ordinary merging, manual exceptions, stale-head re-verification, schedule reuse and shutdown, holds, plateaus and unrelated schedules.
- Pinned-source reconstruction validated, its ZIP matched the source-built ZIP byte for byte, and a fresh extraction passed validation. Every approval delta also reverses exactly to the previous 0.3.0 ZIP.

The decision exercises did not make live service calls. Installation, trusted hook activation, managed worktree lifecycle, complete panel runs, CLI/cloud end-to-end behavior and live PR/CI/scheduler integration remain unproven. No plugin installation, publication, live merge, external message or recurring automation was performed.

The corrected artifact is `outputs/pstack-codex-0.3.1.zip` (local development artifact), SHA-256 `2f672d33ac7221aff02f8758a0b82efb6e5e52d6a5b17c427f3920c917f86271`. The previous ZIP is preserved. See [validation results](outputs/audit-fixes-validation.json), [exact approved deltas](outputs/approved-audit-deltas.json), and [all adaptations](ADAPTATIONS.md).
