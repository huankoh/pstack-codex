# Native Codex changes and provenance

The source remains the complete pinned original-pstack subtree with the pinned
pstack-claude overlay. All 55 top-level skills, 23 playbooks, 3 nested Benny
skills, personas, and original-only material remain in the package. Hstack is
not an input.

## Approved scope

[NATIVE-PORT-DECISIONS.md](NATIVE-PORT-DECISIONS.md) records the interview and
explicit approvals. The native rewrite applies direct Codex instructions plus
these agreed exceptions:

- Native Sol/Astra/Luna defaults preserve the 17-role sheet and existing panels.
  Existing How explorers and per-feature source readers use Luna at max; Sol
  inspects decisive evidence and concludes. No compulsory scouting stage was added.
- Native scoped transcript discovery and reading replace the Claude record parser.
  Ambiguous matches fail instead of guessing an active chat; Reflect's digest
  fallback remains. Raw records, tool output, source lines, malformed records,
  and time-window gaps remain visible.
- Recoverable managed archival may proceed for unused worktrees after preserving
  needed files, without another confirmation. Primary, pinned, shared, and active
  checkouts remain protected. Destructive cleanup retains its gate.
- An unavailable requested model or effort requires the user's replacement choice;
  no automatic downgrade or substitution remains.
- Team/external messages reuse explicit existing authorization. Without it, draft
  and ask. The customer-message pause and other upstream gates remain.

Direct native translations cover tool calls, model/effort arguments, personas as
briefs, .agents/skills and AGENTS.md paths, explicit writer checkouts, supported
scheduling, and the native Codex-home hook setting. Operation-specific references
replace the general platform-mapping detour. The old codex-tools.md path remains
as a navigation/history stub; no active skill requires reading it first.

Workflow stages, counts, review separation, full checklists, broad triggers, and
verification requirements have not been simplified. Decision 11 restores original
Autopilot-full owner-merge authority while retaining stronger shipping checks and
operator-item/review gates. Decision 10 corrects authoring, delegate reuse, prompt
entry points, scheduler shutdown and the plan template. Setup still does not offer
verification creation, and the inherited invocation policies remain unchanged.
See [AUDIT-CORRECTIONS.md](AUDIT-CORRECTIONS.md) for the scoped delta and rationale.

Grok Bot UI and Benny retain their external integration procedures with explicit
capability prerequisites. No Codex webhook, secret-entry UI, or Slack event service
was invented. Separate replacement proposals remain unapproved.

Decision 12 adds the combined visual PR extension: the existing PR skill uses
HumanLayer show-me and visual-pr conventions with pstack's unchanged canonical
trail and audit. PR-bound work starts logging early; the short body links one
appendix that records revisions, decisions, proof and review gaps. Normal opening,
Autopilot and shipping callers prepare or refresh that packet. This is an approved
behavioral extension, not merely a platform translation. The HumanLayer license
is imported unchanged; no other HumanLayer skill is added.

Decision 13 publishes the approved package with three manifest URLs pointing to
`huankoh/pstack-codex`. No workflow bytes change. See [publication deltas](outputs/publication-deltas.json).

## Exact comparison with selected upstream

The 254-file package contains 109 byte-identical imports, 134 declared modified
imports, and 11 generated Codex files. Of the 37 imported files under scripts/,
36 remain byte-identical; only the transcript finder changed. The hook command
also now reads Codex home directly. Imported source hashes and body hashes remain
pinned to their original values.

The source lock uses fidelity schema 3. Every imported edit has its exact original
text, replacement, offset, rationale, and approval category. Validation reverses
those edits and requires byte-for-byte reconstruction of the pinned source,
in addition to checking output hashes, modes, inventory, metadata, and links.
An updated output hash alone cannot hide a workflow edit. Approval categories are
an audit aid, not proof of semantic approval; the recorded diffs still require
review against the user's decisions.

The full before/after declarations are in [sources.lock.json](sources.lock.json).
[patches/codex-compatibility.patch](patches/codex-compatibility.patch) reconstructs
the package from the original source union. Historical attribution, notices,
licenses, and the upstream changelog remain preserved.

## Every modified imported file

“Changed since 0.2.0” compares with the faithful adapter baseline at 9550052.
The decision-12 delta from 0.3.1 changes 11 existing package files and adds four;
[the exact record](outputs/combined-pr-deltas.json) preserves the previous bytes.
Untouched declarations are retained. The table below describes cumulative changes.

| File | Changed since 0.2.0 | Rationale |
| --- | --- | --- |
| [.codex-plugin/plugin.json](src/pstack-codex/.codex-plugin/plugin.json) | Yes | Native metadata and 0.4.0 approved PR extension; decision 13 points the three repository URLs to huankoh/pstack-codex. |
| [.codex-plugin/prompts/architect.md](src/pstack-codex/.codex-plugin/prompts/architect.md) | Yes | Retain prior declared native translations; Remove the obsolete platform-mapping detour while retaining the native skill invocation. See decisions 10-11 and the exact 0.3.0-to-0.3.1 audit correction delta. |
| [.codex-plugin/prompts/arena.md](src/pstack-codex/.codex-plugin/prompts/arena.md) | Yes | Retain prior declared native translations; Remove the obsolete platform-mapping detour while retaining the native skill invocation. See decisions 10-11 and the exact 0.3.0-to-0.3.1 audit correction delta. |
| [.codex-plugin/prompts/automate-me.md](src/pstack-codex/.codex-plugin/prompts/automate-me.md) | Yes | Retain prior declared native translations; Remove the obsolete platform-mapping detour while retaining the native skill invocation. See decisions 10-11 and the exact 0.3.0-to-0.3.1 audit correction delta. |
| [.codex-plugin/prompts/babysit.md](src/pstack-codex/.codex-plugin/prompts/babysit.md) | Yes | Retain prior declared native translations; Remove the obsolete platform-mapping detour while retaining the native skill invocation. See decisions 10-11 and the exact 0.3.0-to-0.3.1 audit correction delta. |
| [.codex-plugin/prompts/blast-radius.md](src/pstack-codex/.codex-plugin/prompts/blast-radius.md) | Yes | Retain prior declared native translations; Remove the obsolete platform-mapping detour while retaining the native skill invocation. See decisions 10-11 and the exact 0.3.0-to-0.3.1 audit correction delta. |
| [.codex-plugin/prompts/bro.md](src/pstack-codex/.codex-plugin/prompts/bro.md) | Yes | Retain prior declared native translations; Remove the obsolete platform-mapping detour while retaining the native skill invocation. See decisions 10-11 and the exact 0.3.0-to-0.3.1 audit correction delta. |
| [.codex-plugin/prompts/create-verification-skill.md](src/pstack-codex/.codex-plugin/prompts/create-verification-skill.md) | Yes | Retain prior declared native translations; Remove the obsolete platform-mapping detour while retaining the native skill invocation. See decisions 10-11 and the exact 0.3.0-to-0.3.1 audit correction delta. |
| [.codex-plugin/prompts/deslop.md](src/pstack-codex/.codex-plugin/prompts/deslop.md) | Yes | Retain prior declared native translations; Remove the obsolete platform-mapping detour while retaining the native skill invocation. See decisions 10-11 and the exact 0.3.0-to-0.3.1 audit correction delta. |
| [.codex-plugin/prompts/figure-it-out.md](src/pstack-codex/.codex-plugin/prompts/figure-it-out.md) | Yes | Retain prior declared native translations; Remove the obsolete platform-mapping detour while retaining the native skill invocation. See decisions 10-11 and the exact 0.3.0-to-0.3.1 audit correction delta. |
| [.codex-plugin/prompts/fix-ci.md](src/pstack-codex/.codex-plugin/prompts/fix-ci.md) | Yes | Retain prior declared native translations; Remove the obsolete platform-mapping detour while retaining the native skill invocation. See decisions 10-11 and the exact 0.3.0-to-0.3.1 audit correction delta. |
| [.codex-plugin/prompts/fix-merge-conflicts.md](src/pstack-codex/.codex-plugin/prompts/fix-merge-conflicts.md) | Yes | Retain prior declared native translations; Remove the obsolete platform-mapping detour while retaining the native skill invocation. See decisions 10-11 and the exact 0.3.0-to-0.3.1 audit correction delta. |
| [.codex-plugin/prompts/get-pr-comments.md](src/pstack-codex/.codex-plugin/prompts/get-pr-comments.md) | Yes | Retain prior declared native translations; Remove the obsolete platform-mapping detour while retaining the native skill invocation. See decisions 10-11 and the exact 0.3.0-to-0.3.1 audit correction delta. |
| [.codex-plugin/prompts/how.md](src/pstack-codex/.codex-plugin/prompts/how.md) | Yes | Retain prior declared native translations; Remove the obsolete platform-mapping detour while retaining the native skill invocation. See decisions 10-11 and the exact 0.3.0-to-0.3.1 audit correction delta. |
| [.codex-plugin/prompts/interrogate.md](src/pstack-codex/.codex-plugin/prompts/interrogate.md) | Yes | Retain prior declared native translations; Remove the obsolete platform-mapping detour while retaining the native skill invocation. See decisions 10-11 and the exact 0.3.0-to-0.3.1 audit correction delta. |
| [.codex-plugin/prompts/maintain-verification-skill.md](src/pstack-codex/.codex-plugin/prompts/maintain-verification-skill.md) | Yes | Retain prior declared native translations; Remove the obsolete platform-mapping detour while retaining the native skill invocation. See decisions 10-11 and the exact 0.3.0-to-0.3.1 audit correction delta. |
| [.codex-plugin/prompts/make-pr-easy-to-review.md](src/pstack-codex/.codex-plugin/prompts/make-pr-easy-to-review.md) | Yes | Retain prior approved translations; Describe the combined PR entry point without changing the wrapper invocation policy. Decision 12; exact 0.3.1-to-0.4.0 delta is separately recorded. |
| [.codex-plugin/prompts/no-comments.md](src/pstack-codex/.codex-plugin/prompts/no-comments.md) | Yes | Retain prior declared native translations; Remove the obsolete platform-mapping detour while retaining the native skill invocation. See decisions 10-11 and the exact 0.3.0-to-0.3.1 audit correction delta. |
| [.codex-plugin/prompts/poteto-mode.md](src/pstack-codex/.codex-plugin/prompts/poteto-mode.md) | Yes | Retain prior declared native translations; Remove the obsolete platform-mapping detour while retaining the native skill invocation. See decisions 10-11 and the exact 0.3.0-to-0.3.1 audit correction delta. |
| [.codex-plugin/prompts/recall.md](src/pstack-codex/.codex-plugin/prompts/recall.md) | Yes | Retain prior declared native translations; Remove the obsolete platform-mapping detour while retaining the native skill invocation. See decisions 10-11 and the exact 0.3.0-to-0.3.1 audit correction delta. |
| [.codex-plugin/prompts/reflect.md](src/pstack-codex/.codex-plugin/prompts/reflect.md) | Yes | Retain prior declared native translations; Remove the obsolete platform-mapping detour while retaining the native skill invocation. See decisions 10-11 and the exact 0.3.0-to-0.3.1 audit correction delta. |
| [.codex-plugin/prompts/setup-pstack.md](src/pstack-codex/.codex-plugin/prompts/setup-pstack.md) | Yes | Retain prior declared native translations; Remove the obsolete platform-mapping detour while retaining the native skill invocation. See decisions 10-11 and the exact 0.3.0-to-0.3.1 audit correction delta. |
| [.codex-plugin/prompts/show-me-your-work.md](src/pstack-codex/.codex-plugin/prompts/show-me-your-work.md) | Yes | Retain prior declared native translations; Remove the obsolete platform-mapping detour while retaining the native skill invocation. See decisions 10-11 and the exact 0.3.0-to-0.3.1 audit correction delta. |
| [.codex-plugin/prompts/swarm.md](src/pstack-codex/.codex-plugin/prompts/swarm.md) | Yes | Retain prior declared native translations; Remove the obsolete platform-mapping detour while retaining the native skill invocation. See decisions 10-11 and the exact 0.3.0-to-0.3.1 audit correction delta. |
| [.codex-plugin/prompts/tdd.md](src/pstack-codex/.codex-plugin/prompts/tdd.md) | Yes | Retain prior declared native translations; Remove the obsolete platform-mapping detour while retaining the native skill invocation. See decisions 10-11 and the exact 0.3.0-to-0.3.1 audit correction delta. |
| [.codex-plugin/prompts/teach.md](src/pstack-codex/.codex-plugin/prompts/teach.md) | Yes | Retain prior declared native translations; Remove the obsolete platform-mapping detour while retaining the native skill invocation. See decisions 10-11 and the exact 0.3.0-to-0.3.1 audit correction delta. |
| [.codex-plugin/prompts/technical-writing.md](src/pstack-codex/.codex-plugin/prompts/technical-writing.md) | Yes | Retain prior declared native translations; Remove the obsolete platform-mapping detour while retaining the native skill invocation. See decisions 10-11 and the exact 0.3.0-to-0.3.1 audit correction delta. |
| [.codex-plugin/prompts/thermo-nuclear-code-quality-review.md](src/pstack-codex/.codex-plugin/prompts/thermo-nuclear-code-quality-review.md) | Yes | Retain prior declared native translations; Remove the obsolete platform-mapping detour while retaining the native skill invocation. See decisions 10-11 and the exact 0.3.0-to-0.3.1 audit correction delta. |
| [.codex-plugin/prompts/typescript-best-practices.md](src/pstack-codex/.codex-plugin/prompts/typescript-best-practices.md) | Yes | Retain prior declared native translations; Remove the obsolete platform-mapping detour while retaining the native skill invocation. See decisions 10-11 and the exact 0.3.0-to-0.3.1 audit correction delta. |
| [.codex-plugin/prompts/unslop.md](src/pstack-codex/.codex-plugin/prompts/unslop.md) | Yes | Retain prior declared native translations; Remove the obsolete platform-mapping detour while retaining the native skill invocation. See decisions 10-11 and the exact 0.3.0-to-0.3.1 audit correction delta. |
| [.codex-plugin/prompts/what-did-i-get-done.md](src/pstack-codex/.codex-plugin/prompts/what-did-i-get-done.md) | Yes | Retain prior declared native translations; Remove the obsolete platform-mapping detour while retaining the native skill invocation. See decisions 10-11 and the exact 0.3.0-to-0.3.1 audit correction delta. |
| [.codex-plugin/prompts/why.md](src/pstack-codex/.codex-plugin/prompts/why.md) | Yes | Retain prior declared native translations; Remove the obsolete platform-mapping detour while retaining the native skill invocation. See decisions 10-11 and the exact 0.3.0-to-0.3.1 audit correction delta. |
| [CHANGES.md](src/pstack-codex/CHANGES.md) | Retained compatibility | Required native Codex metadata, namespace, prompt-reference or path compatibility; preserve unrelated upstream content. |
| [README.md](src/pstack-codex/README.md) | Yes | Retain prior approved translations; Document the single combined PR entry point. Decision 12; exact 0.3.1-to-0.4.0 delta is separately recorded. |
| [agents/comment-sicko.md](src/pstack-codex/agents/comment-sicko.md) | Yes | Keep persona instructions as native spawn briefs and express effort through Codex arguments rather than a registered Claude agent type. |
| [agents/poteto-agent.md](src/pstack-codex/agents/poteto-agent.md) | Yes | Retain prior declared native translations; Restore original and Claude delegate continuity through the native follow-up operation. See decisions 10-11 and the exact 0.3.0-to-0.3.1 audit correction delta. |
| [automations/benny/FOR_AGENTS.md](src/pstack-codex/automations/benny/FOR_AGENTS.md) | Yes | State exact unsupported integration prerequisites directly; retain the original external integration contract without inventing a native replacement. |
| [automations/benny/README.md](src/pstack-codex/automations/benny/README.md) | Yes | State exact unsupported integration prerequisites directly; retain the original external integration contract without inventing a native replacement. |
| [automations/benny/skills/reproduce-and-fix-issues/SKILL.md](src/pstack-codex/automations/benny/skills/reproduce-and-fix-issues/SKILL.md) | Yes | State exact unsupported integration prerequisites directly; retain the original external integration contract without inventing a native replacement. |
| [automations/benny/skills/setup-benny/SKILL.md](src/pstack-codex/automations/benny/skills/setup-benny/SKILL.md) | Yes | State exact unsupported integration prerequisites directly; retain the original external integration contract without inventing a native replacement. |
| [automations/benny/skills/triage-issue-reports/SKILL.md](src/pstack-codex/automations/benny/skills/triage-issue-reports/SKILL.md) | Yes | State exact unsupported integration prerequisites directly; retain the original external integration contract without inventing a native replacement. |
| [docs/guide/01-setup.md](src/pstack-codex/docs/guide/01-setup.md) | Yes | Translate user-facing runtime instructions to Codex and describe the selected pstack-claude workflow accurately; preserve upstream attribution and workflow scope. |
| [docs/guide/02-poteto-mode.md](src/pstack-codex/docs/guide/02-poteto-mode.md) | Yes | Translate user-facing runtime instructions to Codex and describe the selected pstack-claude workflow accurately; preserve upstream attribution and workflow scope. |
| [docs/guide/04-design.md](src/pstack-codex/docs/guide/04-design.md) | Yes | Translate user-facing runtime instructions to Codex and describe the selected pstack-claude workflow accurately; preserve upstream attribution and workflow scope. |
| [docs/guide/05-build-and-clean.md](src/pstack-codex/docs/guide/05-build-and-clean.md) | Yes | Translate user-facing runtime instructions to Codex and describe the selected pstack-claude workflow accurately; preserve upstream attribution and workflow scope. |
| [docs/guide/06-verify-and-ship.md](src/pstack-codex/docs/guide/06-verify-and-ship.md) | Yes | Retain prior approved translations; Explain visual context, evidence appendix, retrospective gaps and unchanged verification/merge requirements. Decision 12; exact 0.3.1-to-0.4.0 delta is separately recorded. |
| [docs/guide/07-overnight.md](src/pstack-codex/docs/guide/07-overnight.md) | Yes | Retain prior declared native translations; Restore original Autopilot-full owner-merge authority under its full-autonomy grant and clean root verdict; retain stronger Claude shipping checks, operator-named items, interaction review gates and Autopilot-stack semantics. See decisions 10-11 and the exact 0.3.0-to-0.3.1 audit correction delta. |
| [docs/guide/09-make-it-yours.md](src/pstack-codex/docs/guide/09-make-it-yours.md) | Yes | Translate user-facing runtime instructions to Codex and describe the selected pstack-claude workflow accurately; preserve upstream attribution and workflow scope. |
| [docs/guide/10-recipes-and-pitfalls.md](src/pstack-codex/docs/guide/10-recipes-and-pitfalls.md) | Yes | Translate user-facing runtime instructions to Codex and describe the selected pstack-claude workflow accurately; preserve upstream attribution and workflow scope. |
| [docs/guide/README.md](src/pstack-codex/docs/guide/README.md) | Yes | Translate user-facing runtime instructions to Codex and describe the selected pstack-claude workflow accurately; preserve upstream attribution and workflow scope. |
| [effort-agents/effort-high.md](src/pstack-codex/effort-agents/effort-high.md) | Yes | Keep persona instructions as native spawn briefs and express effort through Codex arguments rather than a registered Claude agent type. |
| [effort-agents/effort-low.md](src/pstack-codex/effort-agents/effort-low.md) | Yes | Keep persona instructions as native spawn briefs and express effort through Codex arguments rather than a registered Claude agent type. |
| [effort-agents/effort-max.md](src/pstack-codex/effort-agents/effort-max.md) | Yes | Keep persona instructions as native spawn briefs and express effort through Codex arguments rather than a registered Claude agent type. |
| [effort-agents/effort-medium.md](src/pstack-codex/effort-agents/effort-medium.md) | Yes | Keep persona instructions as native spawn briefs and express effort through Codex arguments rather than a registered Claude agent type. |
| [effort-agents/effort-xhigh.md](src/pstack-codex/effort-agents/effort-xhigh.md) | Yes | Keep persona instructions as native spawn briefs and express effort through Codex arguments rather than a registered Claude agent type. |
| [effort-agents/poteto-agent-high.md](src/pstack-codex/effort-agents/poteto-agent-high.md) | Yes | Keep persona instructions as native spawn briefs and express effort through Codex arguments rather than a registered Claude agent type. |
| [effort-agents/poteto-agent-low.md](src/pstack-codex/effort-agents/poteto-agent-low.md) | Yes | Keep persona instructions as native spawn briefs and express effort through Codex arguments rather than a registered Claude agent type. |
| [effort-agents/poteto-agent-max.md](src/pstack-codex/effort-agents/poteto-agent-max.md) | Yes | Keep persona instructions as native spawn briefs and express effort through Codex arguments rather than a registered Claude agent type. |
| [effort-agents/poteto-agent-medium.md](src/pstack-codex/effort-agents/poteto-agent-medium.md) | Yes | Keep persona instructions as native spawn briefs and express effort through Codex arguments rather than a registered Claude agent type. |
| [effort-agents/poteto-agent-xhigh.md](src/pstack-codex/effort-agents/poteto-agent-xhigh.md) | Yes | Keep persona instructions as native spawn briefs and express effort through Codex arguments rather than a registered Claude agent type. |
| [hooks/hooks.json](src/pstack-codex/hooks/hooks.json) | Yes | Use native PLUGIN_ROOT for the same SessionStart command and lifecycle triggers. |
| [hooks/session-start](src/pstack-codex/hooks/session-start) | Yes | Read the native Codex home model sheet directly; preserve session-hook opt-out semantics. |
| [hooks/session-start-context.md](src/pstack-codex/hooks/session-start-context.md) | Yes | Required native Codex metadata, namespace, prompt-reference or path compatibility; preserve unrelated upstream content. |
| [models.json](src/pstack-codex/models.json) | Yes | Retain 17-role vocabulary with approved native model defaults and Luna max; remove the cross-platform model mapping. |
| [skills/architect/SKILL.md](src/pstack-codex/skills/architect/SKILL.md) | Yes | Direct Codex tools, models, paths and approved runtime policies in the skill; preserve its upstream stages, roles, counts and outputs. |
| [skills/architect/references/runner-prompt.md](src/pstack-codex/skills/architect/references/runner-prompt.md) | Yes | Required native Codex metadata, namespace, prompt-reference or path compatibility; preserve unrelated upstream content. |
| [skills/arena/SKILL.md](src/pstack-codex/skills/arena/SKILL.md) | Yes | Direct Codex tools, models, paths and approved runtime policies in the skill; preserve its upstream stages, roles, counts and outputs. |
| [skills/automate-me/SKILL.md](src/pstack-codex/skills/automate-me/SKILL.md) | Yes | Retain prior declared native translations; Translate the authoring dependency to skill-creator without losing the subjective evaluation and conditional trigger-optimization contracts. See decisions 10-11 and the exact 0.3.0-to-0.3.1 audit correction delta. |
| [skills/babysit/SKILL.md](src/pstack-codex/skills/babysit/SKILL.md) | Yes | Direct Codex tools, models, paths and approved runtime policies in the skill; preserve its upstream stages, roles, counts and outputs. |
| [skills/create-verification-skill/SKILL.md](src/pstack-codex/skills/create-verification-skill/SKILL.md) | Yes | Direct Codex tools, models, paths and approved runtime policies in the skill; preserve its upstream stages, roles, counts and outputs. |
| [skills/figure-it-out/SKILL.md](src/pstack-codex/skills/figure-it-out/SKILL.md) | Yes | Direct Codex tools, models, paths and approved runtime policies in the skill; preserve its upstream stages, roles, counts and outputs. |
| [skills/how/SKILL.md](src/pstack-codex/skills/how/SKILL.md) | Yes | Direct Codex tools, models, paths and approved runtime policies in the skill; preserve its upstream stages, roles, counts and outputs. |
| [skills/how/references/explainer-prompt.md](src/pstack-codex/skills/how/references/explainer-prompt.md) | Yes | Required native Codex metadata, namespace, prompt-reference or path compatibility; preserve unrelated upstream content. |
| [skills/interrogate/SKILL.md](src/pstack-codex/skills/interrogate/SKILL.md) | Yes | Direct Codex tools, models, paths and approved runtime policies in the skill; preserve its upstream stages, roles, counts and outputs. |
| [skills/maintain-verification-skill/SKILL.md](src/pstack-codex/skills/maintain-verification-skill/SKILL.md) | Yes | Direct Codex tools, models, paths and approved runtime policies in the skill; preserve its upstream stages, roles, counts and outputs. |
| [skills/make-bot-ui/SKILL.md](src/pstack-codex/skills/make-bot-ui/SKILL.md) | Yes | State exact unsupported integration prerequisites directly; retain the original external integration contract without inventing a native replacement. |
| [skills/make-pr-easy-to-review/SKILL.md](src/pstack-codex/skills/make-pr-easy-to-review/SKILL.md) | Yes | Retain prior approved translations; Combine visual context, structural outlines and pstack audited evidence in the existing PR entry point; preserve its history and behavior guardrails. Decision 12; exact 0.3.1-to-0.4.0 delta is separately recorded. |
| [skills/make-pr-easy-to-review/references/visual-outline.md](src/pstack-codex/skills/make-pr-easy-to-review/references/visual-outline.md) | New approved import | Adapt HumanLayer show-me visual conventions for source-grounded Codex PR explanations and remote artifact constraints. Decision 12; exact 0.3.1-to-0.4.0 delta is separately recorded. |
| [skills/no-comments/SKILL.md](src/pstack-codex/skills/no-comments/SKILL.md) | Yes | Direct Codex tools, models, paths and approved runtime policies in the skill; preserve its upstream stages, roles, counts and outputs. |
| [skills/poteto-mode/SKILL.md](src/pstack-codex/skills/poteto-mode/SKILL.md) | Yes | Retain prior approved translations; Start canonical decision logging when PR-bound work starts and route presentation through the combined entry point. Decision 12; exact 0.3.1-to-0.4.0 delta is separately recorded. |
| [skills/poteto-mode/playbooks/authoring-a-skill.md](src/pstack-codex/skills/poteto-mode/playbooks/authoring-a-skill.md) | Yes | Direct native delegation, worktree, scheduling or evidence operation at its existing playbook step; preserve the procedure and verification requirements. |
| [skills/poteto-mode/playbooks/autonomous-run.md](src/pstack-codex/skills/poteto-mode/playbooks/autonomous-run.md) | Yes | Direct native delegation, worktree, scheduling or evidence operation at its existing playbook step; preserve the procedure and verification requirements. |
| [skills/poteto-mode/playbooks/autopilot-full.md](src/pstack-codex/skills/poteto-mode/playbooks/autopilot-full.md) | Yes | Retain prior approved translations; Publish an honest pending packet at early PR creation and refresh before final handoff or the authorized merge; preserve raw-log and merge rules. Decision 12; exact 0.3.1-to-0.4.0 delta is separately recorded. |
| [skills/poteto-mode/playbooks/autopilot-stack.md](src/pstack-codex/skills/poteto-mode/playbooks/autopilot-stack.md) | Yes | Retain prior approved translations; Publish the combined packet early and refresh at final parent/head without changing operator landing authority. Decision 12; exact 0.3.1-to-0.4.0 delta is separately recorded. |
| [skills/poteto-mode/playbooks/babysit.md](src/pstack-codex/skills/poteto-mode/playbooks/babysit.md) | Yes | Direct native delegation, worktree, scheduling or evidence operation at its existing playbook step; preserve the procedure and verification requirements. |
| [skills/poteto-mode/playbooks/bug-fix.md](src/pstack-codex/skills/poteto-mode/playbooks/bug-fix.md) | Yes | Direct native delegation, worktree, scheduling or evidence operation at its existing playbook step; preserve the procedure and verification requirements. |
| [skills/poteto-mode/playbooks/eval.md](src/pstack-codex/skills/poteto-mode/playbooks/eval.md) | Yes | Direct native delegation, worktree, scheduling or evidence operation at its existing playbook step; preserve the procedure and verification requirements. |
| [skills/poteto-mode/playbooks/feature.md](src/pstack-codex/skills/poteto-mode/playbooks/feature.md) | Yes | Direct native delegation, worktree, scheduling or evidence operation at its existing playbook step; preserve the procedure and verification requirements. |
| [skills/poteto-mode/playbooks/multi-phase-plan.md](src/pstack-codex/skills/poteto-mode/playbooks/multi-phase-plan.md) | Yes | Retain prior approved translations; Include early logging and combined PR preparation/refresh in the existing checklist. Decision 12; exact 0.3.1-to-0.4.0 delta is separately recorded. |
| [skills/poteto-mode/playbooks/opening-a-pr.md](src/pstack-codex/skills/poteto-mode/playbooks/opening-a-pr.md) | Yes | Retain prior approved translations; Prepare and publish the combined review packet without recursive dispatch or changes to forge, readiness, stack or babysit rules. Decision 12; exact 0.3.1-to-0.4.0 delta is separately recorded. |
| [skills/poteto-mode/playbooks/orchestrate.md](src/pstack-codex/skills/poteto-mode/playbooks/orchestrate.md) | Yes | Direct native delegation, worktree, scheduling or evidence operation at its existing playbook step; preserve the procedure and verification requirements. |
| [skills/poteto-mode/playbooks/session-pickup.md](src/pstack-codex/skills/poteto-mode/playbooks/session-pickup.md) | Yes | Direct native delegation, worktree, scheduling or evidence operation at its existing playbook step; preserve the procedure and verification requirements. |
| [skills/poteto-mode/playbooks/shipping.md](src/pstack-codex/skills/poteto-mode/playbooks/shipping.md) | Yes | Retain prior approved translations; Refresh visual context and actual receipt applicability after shipping preparation without replacing verification or merge gates. Decision 12; exact 0.3.1-to-0.4.0 delta is separately recorded. |
| [skills/poteto-mode/playbooks/visual-parity.md](src/pstack-codex/skills/poteto-mode/playbooks/visual-parity.md) | Yes | Direct native delegation, worktree, scheduling or evidence operation at its existing playbook step; preserve the procedure and verification requirements. |
| [skills/poteto-mode/playbooks/worktree-cleanup.md](src/pstack-codex/skills/poteto-mode/playbooks/worktree-cleanup.md) | Yes | Direct native delegation, worktree, scheduling or evidence operation at its existing playbook step; preserve the procedure and verification requirements. |
| [skills/poteto-mode/references/agents/comment-sicko.md](src/pstack-codex/skills/poteto-mode/references/agents/comment-sicko.md) | Yes | Keep persona instructions as native spawn briefs and express effort through Codex arguments rather than a registered Claude agent type. |
| [skills/poteto-mode/references/agents/poteto-agent.md](src/pstack-codex/skills/poteto-mode/references/agents/poteto-agent.md) | Yes | Retain prior declared native translations; Restore delegate continuity in the vendored persona copy. See decisions 10-11 and the exact 0.3.0-to-0.3.1 audit correction delta. |
| [skills/poteto-mode/references/codex-tools.md](src/pstack-codex/skills/poteto-mode/references/codex-tools.md) | Yes | Retire the mandatory translation table; keep the imported path as a navigation/history stub, with native operation-specific references. |
| [skills/principle-attack-the-premise/SKILL.md](src/pstack-codex/skills/principle-attack-the-premise/SKILL.md) | Retained compatibility | Direct Codex tools, models, paths and approved runtime policies in the skill; preserve its upstream stages, roles, counts and outputs. |
| [skills/principle-boundary-discipline/SKILL.md](src/pstack-codex/skills/principle-boundary-discipline/SKILL.md) | Retained compatibility | Direct Codex tools, models, paths and approved runtime policies in the skill; preserve its upstream stages, roles, counts and outputs. |
| [skills/principle-build-the-lever/SKILL.md](src/pstack-codex/skills/principle-build-the-lever/SKILL.md) | Retained compatibility | Direct Codex tools, models, paths and approved runtime policies in the skill; preserve its upstream stages, roles, counts and outputs. |
| [skills/principle-encode-lessons-in-structure/SKILL.md](src/pstack-codex/skills/principle-encode-lessons-in-structure/SKILL.md) | Retained compatibility | Direct Codex tools, models, paths and approved runtime policies in the skill; preserve its upstream stages, roles, counts and outputs. |
| [skills/principle-exhaust-the-design-space/SKILL.md](src/pstack-codex/skills/principle-exhaust-the-design-space/SKILL.md) | Retained compatibility | Direct Codex tools, models, paths and approved runtime policies in the skill; preserve its upstream stages, roles, counts and outputs. |
| [skills/principle-experience-first/SKILL.md](src/pstack-codex/skills/principle-experience-first/SKILL.md) | Retained compatibility | Direct Codex tools, models, paths and approved runtime policies in the skill; preserve its upstream stages, roles, counts and outputs. |
| [skills/principle-fix-root-causes/SKILL.md](src/pstack-codex/skills/principle-fix-root-causes/SKILL.md) | Retained compatibility | Direct Codex tools, models, paths and approved runtime policies in the skill; preserve its upstream stages, roles, counts and outputs. |
| [skills/principle-foundational-thinking/SKILL.md](src/pstack-codex/skills/principle-foundational-thinking/SKILL.md) | Retained compatibility | Direct Codex tools, models, paths and approved runtime policies in the skill; preserve its upstream stages, roles, counts and outputs. |
| [skills/principle-guard-the-context-window/SKILL.md](src/pstack-codex/skills/principle-guard-the-context-window/SKILL.md) | Retained compatibility | Direct Codex tools, models, paths and approved runtime policies in the skill; preserve its upstream stages, roles, counts and outputs. |
| [skills/principle-laziness-protocol/SKILL.md](src/pstack-codex/skills/principle-laziness-protocol/SKILL.md) | Retained compatibility | Direct Codex tools, models, paths and approved runtime policies in the skill; preserve its upstream stages, roles, counts and outputs. |
| [skills/principle-make-operations-idempotent/SKILL.md](src/pstack-codex/skills/principle-make-operations-idempotent/SKILL.md) | Retained compatibility | Direct Codex tools, models, paths and approved runtime policies in the skill; preserve its upstream stages, roles, counts and outputs. |
| [skills/principle-migrate-callers-then-delete-legacy-apis/SKILL.md](src/pstack-codex/skills/principle-migrate-callers-then-delete-legacy-apis/SKILL.md) | Retained compatibility | Direct Codex tools, models, paths and approved runtime policies in the skill; preserve its upstream stages, roles, counts and outputs. |
| [skills/principle-minimize-reader-load/SKILL.md](src/pstack-codex/skills/principle-minimize-reader-load/SKILL.md) | Retained compatibility | Direct Codex tools, models, paths and approved runtime policies in the skill; preserve its upstream stages, roles, counts and outputs. |
| [skills/principle-model-the-domain/SKILL.md](src/pstack-codex/skills/principle-model-the-domain/SKILL.md) | Retained compatibility | Direct Codex tools, models, paths and approved runtime policies in the skill; preserve its upstream stages, roles, counts and outputs. |
| [skills/principle-never-block-on-the-human/SKILL.md](src/pstack-codex/skills/principle-never-block-on-the-human/SKILL.md) | Yes | Direct Codex tools, models, paths and approved runtime policies in the skill; preserve its upstream stages, roles, counts and outputs. |
| [skills/principle-outcome-oriented-execution/SKILL.md](src/pstack-codex/skills/principle-outcome-oriented-execution/SKILL.md) | Retained compatibility | Direct Codex tools, models, paths and approved runtime policies in the skill; preserve its upstream stages, roles, counts and outputs. |
| [skills/principle-prove-it-works/SKILL.md](src/pstack-codex/skills/principle-prove-it-works/SKILL.md) | Retained compatibility | Direct Codex tools, models, paths and approved runtime policies in the skill; preserve its upstream stages, roles, counts and outputs. |
| [skills/principle-redesign-from-first-principles/SKILL.md](src/pstack-codex/skills/principle-redesign-from-first-principles/SKILL.md) | Retained compatibility | Direct Codex tools, models, paths and approved runtime policies in the skill; preserve its upstream stages, roles, counts and outputs. |
| [skills/principle-separate-before-serializing-shared-state/SKILL.md](src/pstack-codex/skills/principle-separate-before-serializing-shared-state/SKILL.md) | Retained compatibility | Direct Codex tools, models, paths and approved runtime policies in the skill; preserve its upstream stages, roles, counts and outputs. |
| [skills/principle-sequence-verifiable-units/SKILL.md](src/pstack-codex/skills/principle-sequence-verifiable-units/SKILL.md) | Retained compatibility | Direct Codex tools, models, paths and approved runtime policies in the skill; preserve its upstream stages, roles, counts and outputs. |
| [skills/principle-subtract-before-you-add/SKILL.md](src/pstack-codex/skills/principle-subtract-before-you-add/SKILL.md) | Retained compatibility | Direct Codex tools, models, paths and approved runtime policies in the skill; preserve its upstream stages, roles, counts and outputs. |
| [skills/principle-test-behavior-not-implementation/SKILL.md](src/pstack-codex/skills/principle-test-behavior-not-implementation/SKILL.md) | Retained compatibility | Direct Codex tools, models, paths and approved runtime policies in the skill; preserve its upstream stages, roles, counts and outputs. |
| [skills/principle-type-system-discipline/SKILL.md](src/pstack-codex/skills/principle-type-system-discipline/SKILL.md) | Retained compatibility | Direct Codex tools, models, paths and approved runtime policies in the skill; preserve its upstream stages, roles, counts and outputs. |
| [skills/recall/SKILL.md](src/pstack-codex/skills/recall/SKILL.md) | Yes | Direct Codex tools, models, paths and approved runtime policies in the skill; preserve its upstream stages, roles, counts and outputs. |
| [skills/reflect/SKILL.md](src/pstack-codex/skills/reflect/SKILL.md) | Yes | Retain prior declared native translations; Use skill-creator with the existing approval, draft/validate/test/iterate and description-optimization requirements. See decisions 10-11 and the exact 0.3.0-to-0.3.1 audit correction delta. |
| [skills/reflect/references/divergent-reviewer.md](src/pstack-codex/skills/reflect/references/divergent-reviewer.md) | Yes | Required native Codex metadata, namespace, prompt-reference or path compatibility; preserve unrelated upstream content. |
| [skills/reflect/references/judgment-reviewer.md](src/pstack-codex/skills/reflect/references/judgment-reviewer.md) | Yes | Required native Codex metadata, namespace, prompt-reference or path compatibility; preserve unrelated upstream content. |
| [skills/reflect/references/synthesizer.md](src/pstack-codex/skills/reflect/references/synthesizer.md) | Yes | Retain prior declared native translations; Keep authoring routing labels aligned with the native skill-creator dependency. See decisions 10-11 and the exact 0.3.0-to-0.3.1 audit correction delta. |
| [skills/reflect/references/tooling-reviewer.md](src/pstack-codex/skills/reflect/references/tooling-reviewer.md) | Yes | Required native Codex metadata, namespace, prompt-reference or path compatibility; preserve unrelated upstream content. |
| [skills/reflect/scripts/find-transcript.mjs](src/pstack-codex/skills/reflect/scripts/find-transcript.mjs) | Yes | Replace Claude record discovery with metadata-first workspace and thread scoped Codex rollout discovery; ambiguous or unavailable evidence is reported. |
| [skills/setup-pstack/SKILL.md](src/pstack-codex/skills/setup-pstack/SKILL.md) | Yes | Native Codex model detection, confirmed role sheet, effort arguments, instruction loading and hook support; preserve eight setup steps and shared sheet semantics. |
| [skills/show-me-your-work/SKILL.md](src/pstack-codex/skills/show-me-your-work/SKILL.md) | Yes | Direct Codex tools, models, paths and approved runtime policies in the skill; preserve its upstream stages, roles, counts and outputs. |
| [skills/swarm/SKILL.md](src/pstack-codex/skills/swarm/SKILL.md) | Yes | Direct Codex tools, models, paths and approved runtime policies in the skill; preserve its upstream stages, roles, counts and outputs. |
| [skills/teach/SKILL.md](src/pstack-codex/skills/teach/SKILL.md) | Yes | Direct Codex tools, models, paths and approved runtime policies in the skill; preserve its upstream stages, roles, counts and outputs. |
| [skills/typescript-best-practices/SKILL.md](src/pstack-codex/skills/typescript-best-practices/SKILL.md) | Retained compatibility | Direct Codex tools, models, paths and approved runtime policies in the skill; preserve its upstream stages, roles, counts and outputs. |
| [skills/why/SKILL.md](src/pstack-codex/skills/why/SKILL.md) | Yes | Direct Codex tools, models, paths and approved runtime policies in the skill; preserve its upstream stages, roles, counts and outputs. |

## Generated package files

| File | Rationale |
| --- | --- |
| [automations/benny/skills/reproduce-and-fix-issues/agents/openai.yaml](src/pstack-codex/automations/benny/skills/reproduce-and-fix-issues/agents/openai.yaml) | Native metadata preserving the inherited explicit-only invocation policy. |
| [automations/benny/skills/setup-benny/agents/openai.yaml](src/pstack-codex/automations/benny/skills/setup-benny/agents/openai.yaml) | Native metadata preserving the inherited explicit-only invocation policy. |
| [automations/benny/skills/triage-issue-reports/agents/openai.yaml](src/pstack-codex/automations/benny/skills/triage-issue-reports/agents/openai.yaml) | Native metadata preserving the inherited explicit-only invocation policy. |
| [skills/make-bot-ui/agents/openai.yaml](src/pstack-codex/skills/make-bot-ui/agents/openai.yaml) | Native metadata preserving the inherited explicit-only invocation policy. |
| [skills/make-pr-easy-to-review/references/review-packet.md](src/pstack-codex/skills/make-pr-easy-to-review/references/review-packet.md) | Define the approved compact body, readable evidence appendix, truthful revision-bound claims and idempotent publication procedure. Decision 12. |
| [skills/make-pr-easy-to-review/references/source-notice.md](src/pstack-codex/skills/make-pr-easy-to-review/references/source-notice.md) | Attribute pinned HumanLayer contributions and distinguish approved adaptations from preserved pstack requirements. Decision 12. |
| [skills/poteto-mode/references/delegation.md](src/pstack-codex/skills/poteto-mode/references/delegation.md) | Reuse the existing poteto delegate while preserving required fresh independent reviews. Approved in decision 10. |
| [skills/poteto-mode/references/local-worktrees.md](src/pstack-codex/skills/poteto-mode/references/local-worktrees.md) | Task-specific shared native local-worktrees procedure replacing the mandatory general platform mapping. |
| [skills/poteto-mode/references/scheduling.md](src/pstack-codex/skills/poteto-mode/references/scheduling.md) | Carry existing workflow stop and hold conditions into the persistent scheduler lifecycle; reuse schedule identity. Approved in decision 10. |
| [skills/reflect/references/codex-transcripts.md](src/pstack-codex/skills/reflect/references/codex-transcripts.md) | Task-specific native transcript procedure and evidence limits for approved scoped history workflows. |
| [skills/reflect/scripts/read-transcript.mjs](src/pstack-codex/skills/reflect/scripts/read-transcript.mjs) | Approved scoped native transcript reader retaining exact records, source lines, and evidence gaps. |

Validation evidence and remaining runtime gaps are recorded in [VALIDATION.md](VALIDATION.md).
