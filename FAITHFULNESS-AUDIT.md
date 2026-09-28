**Historical audit of 0.3.0.** The five findings were corrected in 0.3.1 on 2026-09-28 with explicit approval, and original Autopilot-full merge authority was restored. See [the resolution report](AUDIT-CORRECTIONS.md) for current status. The evidence and tables below describe the pre-correction snapshot.

**Faithfulness audit — pstack-codex 0.3.0, 2026-09-27**

**Verdict: the original inventory and the main workflow contracts are retained, but the native port is not yet complete enough to call fully faithful in execution.** Three concrete compatibility omissions remain, plus an underspecified scheduler stop lifecycle. Passing the fidelity checker does not establish semantic equivalence.

This audit compares the working source and delivered ZIP with two pinned Git trees: [original pstack, ecc249f1](https://github.com/cursor/plugins/tree/ecc249f1e306fc64ddf83c7bed16cacf7c2239db/pstack) and [pstack-claude, c02fd492](https://github.com/michael-denyer/pstack-claude/tree/c02fd4922b25ee005f42042463d741d236c2c35e/plugins/pstack). It does not claim to compare with later upstream changes. The 0.3.0 source is uncommitted over baseline commit `9550052`.

The agreed target is original pstack **with the pinned Claude updates**, followed by only the approved Codex/local-worktree translations. Literal equality with original pstack is a different target. The [decision record](NATIVE-PORT-DECISIONS.md) defines the approved deviations. No package, lock, test, adaptation, or proposal file was changed during this audit. Only this report and its inventory artifact were written.

**Findings that prevent a clean native-port verdict**

| ID | Finding and evidence | Effect | Concrete correction to consider |
| --- | --- | --- | --- |
| F1 — confirmed, normal priority | [Automate-me:66](src/pstack-codex/skills/automate-me/SKILL.md#L66), [Reflect:51](src/pstack-codex/skills/reflect/SKILL.md#L51), and [its synthesizer:17](src/pstack-codex/skills/reflect/references/synthesizer.md#L17) still require `plugin-dev:skill-development`. It is not bundled or exposed in this host's skill catalog. The [README:229](src/pstack-codex/README.md#L229) instead names Codex `skill-creator`. | The authoring branches cannot follow their documented dependency on this host. Original used `create-skill`; Claude changed the dependency; the native rewrite left that translation unfinished. | Translate the dependency and routing labels consistently to the supported native authoring workflow. Preserve the approval, draft, validation and iteration requirements; explicitly resolve any unsupported description-optimization step instead of silently omitting it. |
| F2 — confirmed, normal priority | [Poteto persona:3](src/pstack-codex/agents/poteto-agent.md#L3) and [its vendored copy:3](src/pstack-codex/skills/poteto-mode/references/agents/poteto-agent.md#L3) dropped the requirement to resume the existing delegate rather than spawn a sibling. It appears in both pinned sources. No equivalent remains elsewhere in the package. | A follow-up can lose the established delegate's context and change its lifecycle. This is a new Codex omission, not a Claude-overlay change. | Preserve that requirement with the native follow-up/resume operation, such as `followup_task` when the same child is available. Keep required independent reviewer roles independent. |
| F3 — confirmed, normal priority for optional entry points | All **31 optional prompt wrappers**, for example [poteto-mode:7](src/pstack-codex/.codex-plugin/prompts/poteto-mode.md#L7), still instruct the reader to use the general Claude-to-Codex map and its “Per-skill notes.” [That map](src/pstack-codex/skills/poteto-mode/references/codex-tools.md#L3) is now only a history/navigation stub. | These supplied entry points retain the detour the user asked to remove and refer to content that no longer exists. Direct SKILL.md entry points avoid this problem. Installed wrapper discovery was not exercised. | Keep each wrapper's skill invocation and remove the stale translation instruction; do not change the invoked workflow. |
| F4 — static gap, not a demonstrated runtime failure | [Scheduling:3](src/pstack-codex/skills/poteto-mode/references/scheduling.md#L3) introduces persistent recurring heartbeats and re-arming without tying their lifecycle to the playbook's stop conditions. [Babysit:16](src/pstack-codex/skills/poteto-mode/playbooks/babysit.md#L16) stops the watcher at merge-ready; [Autonomous run:11](src/pstack-codex/skills/poteto-mode/playbooks/autonomous-run.md#L11) stops when its predicate is met. | Ending a watcher or active turn does not by itself prove that a persistent future wakeup has stopped. Existing host tool guidance already advises reusing an automation, which mitigates duplication; the package still leaves the terminal scheduler action implicit. | Associate the schedule with its workflow and retain its identity. Update the existing schedule when re-arming, and explicitly suspend/end it on the inherited completion, stop and terminal conditions. Validate creation→re-arm→completion/stop without altering cadence or gates. |

These are proposed corrections, not approval records. No fixes were applied. F1–F3 complete or restore native compatibility; F4 makes the inherited stop behavior explicit for the new mechanism. They do not authorize workflow redesign.

**Differences from literal original pstack that come from the Claude overlay**

These are material changes, even though they are part of the user-selected composition rather than unauthorized Codex edits.

| Area | Original pstack | Pinned Claude and current Codex |
| --- | --- | --- |
| Autopilot-full merge ownership | Normal owners squash-merge after the root's clean verdict under the full-autonomy grant; operator-named items retain their gate. | Every owner stops at merge-ready. Every PR waits for the operator's explicit merge click. [Current contract](src/pstack-codex/skills/poteto-mode/playbooks/autopilot-full.md#L5). This is the largest inherited difference. |
| Shipping | Nine steps, independent verification and ordered squash merges. | Eleven steps with pending-merge cancellation, captured leases and replay boundaries, exact-head merge guards, durable future-merge/queue gates, destination checks and landing confirmation. [Shipping](src/pstack-codex/skills/poteto-mode/playbooks/shipping.md#L7), [merge safety](src/pstack-codex/skills/poteto-mode/references/merge-safety.md). |
| Worker environments | Cloud workers/VMs in the relevant orchestration, shipping and live-verification procedures. | Local agents and worktrees. Codex adds explicit physical checkout ownership. Role counts survive; separate-machine isolation does not. [Local worktrees](src/pstack-codex/skills/poteto-mode/references/local-worktrees.md#L3). |
| Pause/resume state | Looser resume notes, including temporary-file storage. | Shared Git-common-directory storage, artifact preservation, hashes, publication/readback and distinct missing/unavailable results. [Pause safely](src/pstack-codex/skills/poteto-mode/playbooks/pause-safely.md#L8), [resume storage](src/pstack-codex/skills/poteto-mode/references/resume-storage.md). |
| Setup verification offer | Offers optional creation of a verification skill after model setup. | That offer was removed by Claude; current setup preserves the removal. [Guide](src/pstack-codex/docs/guide/01-setup.md#L23). |
| Two principles | Attack-the-Premise uses a stronger census/asymmetry prescription; Test-Behavior includes an undefined-return/literal-output rule. | Claude changes them to hypothesis-specific experimentation and a defect-detection criterion. Codex preserves the selected principle bodies. [Attack the Premise](src/pstack-codex/skills/principle-attack-the-premise/SKILL.md), [Test Behavior](src/pstack-codex/skills/principle-test-behavior-not-implementation/SKILL.md). |
| Invocation eligibility | Reflect, Recall, Automate-me and Show-me-your-work have `disable-model-invocation: true`. | Claude removes those flags; current skills have no equivalent explicit-only policy. This changes eligibility relative to original, although actual host triggering has not been tested. |
| Other guidance | Original runtime persistence, writing and discovery conventions. | Claude adds managed-skill loading and issue tracking triggers, changes response-header guidance and bug-proof log presentation, and replaces `/goal`/cloud wakeups with standing orders and `/loop`. Codex translates the selected scheduling mechanism. |
| Extra skills | 47 top-level skills. | Eight added skills: `babysit`, `deslop`, `fix-ci`, `fix-merge-conflicts`, `get-pr-comments`, `make-pr-easy-to-review`, `thermo-nuclear-code-quality-review`, `what-did-i-get-done`. These enter through the Claude overlay, not hstack. |

**Inherited ambiguity requiring a separate decision:** the [multi-phase plan template:134](src/pstack-codex/skills/poteto-mode/playbooks/multi-phase-plan.md#L134) still offers “the owner squash-merges its own PR.” That sentence is in both upstream trees, but conflicts with the Claude overlay's later operator-merge rule in Autopilot-full, and with the current template's own [operator review gate:123](src/pstack-codex/skills/poteto-mode/playbooks/multi-phase-plan.md#L123). A proposed correction would make the template defer to the selected execution playbook's merge owner. The audit does not resolve it or restore original autonomous merges.

**Approved Codex changes found in the package**

- Native tool and skill instructions, AGENTS.md and Codex paths, direct effort arguments and explicit capability checks. Small operation-specific references replace the general mapping in active skills and playbooks, with the wrapper exception in F3.
- Sol for ordinary implementation and conclusions, Astra for strongest roles, and the existing Astra/Sol/Luna panels. Luna uses `max`, including panel seats and the approved existing retrieval roles. No compulsory scouting stage was added. Unavailable model/effort choices require the user's replacement decision.
- How retains 2–4 explorers only for complex questions and one explainer; simple questions still use one explainer without explorers. Why's investigators and Reflect's tooling reviewer stay Sol.
- Reflect retains three perspectives and one synthesizer; Arena retains the existing runner panel and one selected cross-judge. Independent review roles are not collapsed.
- Codex transcript finding/reading preserves workspace scope, raw records and source line numbers; the existing Reflect digest fallback remains explicitly weaker evidence.
- Physical local-worktree ownership, reuse and the expressly approved recoverable archival exception, with primary/pinned/shared/in-use protection and preservation of needed ignored files.
- The approved external-message authorization wording, retaining the customer-message pause and existing authorization. No new default permission to send messages was added.
- Grok Bot UI and Benny remain present with capability-prerequisite notices. They were not silently removed or replaced.

Astra/Sol/Luna provide different configured models; this is not evidence of different vendors or model families. The native wording reflects that narrower guarantee.

**Core workflow contracts preserved in the static comparison**

| Contract | Audit result |
| --- | --- |
| Feature development | How→Architect→decomposition/delegation or Arena→matching-surface verification→ordered commits→PR retained. |
| Bug fixing | Reproduction and mechanism proof before implementation, failing-first history and same-surface proof retained. |
| Multi-phase programs | All ten live lanes, regression lane, performance gate, at least two audit lanes and screenshot/video review gate retained. |
| Autopilot | One owner per PR, independent round verification, exact-head accounting, 30-minute audit and zero-write operator hold retained from Claude. |
| Babysit | Modes, frontier-only scope, conflicts→threads→CI order, one babysitter, frozen queue, merge-ready termination and no implied merge permission retained; see F4 for scheduler lifecycle. |
| Shipping | Independent verifier per PR, contiguous verified run, ceiling and exact revision/destination validity retained. |
| Orchestrate | Coordinator/worker/verifier separation, bounded retries, durable store, authoritative frontier and evidence ledger retained. |
| Personas and panels | Comment Sicko rules and panel jobs retained; poteto-agent continuity exception is F2. |

**Inventory and mechanical evidence**

| Inventory | Original subtree | Claude subtree | Selected union | Current package |
| --- | ---: | ---: | ---: | ---: |
| Files | 158 | 202 | 237 | 250 |
| Top-level skills | 47 | 54 | 55 | 55 |
| Nested Benny skills | 3 | 0 | 3 | 3 |
| Playbooks | 23 | 23 | 23 | 23 |

No path from either pinned subtree is missing. The union includes 35 original-only paths and 79 Claude-only paths. Of their 123 common paths, 28 are identical and 95 differ. These are exact-byte comparisons, not semantic quality scores.

The 13 files beyond that union comprise four attribution/history imports from the Claude repository and nine Codex-generated files. Across all 241 imported files, **141 are byte-identical and 100 are changed**. Of 37 imported script files, **36 are byte-identical**; the transcript finder is the changed script, accompanied by the new native reader. Of 58 SKILL.md files, 12 are byte-identical, 23 change only frontmatter when comparing normalized bodies, and 23 have body changes. Eight playbooks are byte-identical; 15 have translations.

The 250 delivered ZIP files match their current source bytes. Local `node_modules` installed for prior helper checks are excluded from the delivered package and from these inventory counts. The report's [machine-readable inventory](outputs/faithfulness-inventory.json) records every path, source identity, hashes, modes, additions and comparisons.

`tools/validate.py` was rerun during this audit and passed. It verifies exact declared-change accounting, schemas, references and inventory. Its use of the word “faithful” in its console output is not a semantic certification: F1–F4 can coexist with that pass.

The preceding implementation recorded 181 passing Bun tests, 21 passing Python tests, all 58 skill schemas, the plugin schema, TypeScript checks and deterministic pinned-source reconstruction. Those broader checks were not rerun wholesale for this read-only audit; see [validation evidence](VALIDATION.md). Static reviewers independently compared core playbooks, other skills/personas, and history/setup workflows with the pinned Git objects.

**Limits and lower-priority ambiguities**

| Item | What is established / still unknown |
| --- | --- |
| Installation and hosts | No installed discovery/trusted hook run or CLI/cloud end-to-end exercise. This audit does not certify all-host execution. |
| Scheduled monitoring | No live recurring-automation lifecycle test; F4 remains a static gap. |
| Panels and shipping | No complete Arena/Architect/Interrogate exercise and no live PR/CI/shipping trial. Static retention of a gate does not prove execution. |
| Transcript formats | Synthetic native fixtures were tested previously; no actual private transcript corpus was scanned. The reader verifies workspace identity; exact-thread selection relies on the finder's thread match and the documented procedure. |
| Worktree cleanup | Managed creation/archive/restore remains unproven. The retained helper still defaults to `~/.claude/projects`; the [native playbook:5](src/pstack-codex/skills/poteto-mode/playbooks/worktree-cleanup.md#L5) explicitly rejects that default and requires suitable scoped input or unavailable chat evidence. Its content/mtime scan cannot itself establish pinned-chat state; the playbook requires separate session/usage checks. No live cleanup was run. |
| TypeScript activation | [TypeScript:4](src/pstack-codex/skills/typescript-best-practices/SKILL.md#L4) preserves original `paths` as historical metadata and puts the .ts/.tsx trigger in the description. Path-based host activation equivalence has not been demonstrated; this is not evidence that the skill never triggers. |
| Model overrides | [How:47](src/pstack-codex/skills/how/SKILL.md#L47) calls the explainer “Sol,” although the same skill allows an override. The dispatch rows correctly use the configured role. This is a wording ambiguity; use “configured explainer (Sol by default)” if approved. |
| Shared configuration | Model-sheet storage remains global even when rows are loaded through a project's AGENTS.md. This inherited scope is disclosed; project-specific storage remains an unapproved proposal. |
| Unsupported integrations | Grok Bot UI and Benny are preserved capabilities awaiting integrations, not operational Codex equivalents. |

**Per-skill comparison index**

“Same” means byte-identical to the selected pinned source. “Metadata only” means only frontmatter differs after trimming body-edge whitespace. “Body translated” records a content difference, not a guarantee of semantic equivalence. The Claude column only records whether that upstream skill differs from original, not whether its difference is solely platform syntax.

| Skill | Original→Claude | Selected source→Codex | Audit note |
| --- | --- | --- | --- |
| [architect](src/pstack-codex/skills/architect/SKILL.md) | Changed in Claude | Body translated | Runner panel and synthesis retained. |
| [arena](src/pstack-codex/skills/arena/SKILL.md) | Changed in Claude | Body translated | Runner panel and one cross-judge retained. |
| [automate-me](src/pstack-codex/skills/automate-me/SKILL.md) | Changed in Claude | Body translated | F1: untranslated authoring dependency. |
| [babysit](src/pstack-codex/skills/babysit/SKILL.md) | Added by Claude | Body translated | Claude addition; poteto-mode playbook still has precedence. |
| [blast-radius](src/pstack-codex/skills/blast-radius/SKILL.md) | Changed in Claude | Same | Nothing changed from selected source. |
| [bro](src/pstack-codex/skills/bro/SKILL.md) | Changed in Claude | Same | Nothing changed from selected source. |
| [create-verification-skill](src/pstack-codex/skills/create-verification-skill/SKILL.md) | Changed in Claude | Body translated | Native .agents/skills/verify path; selected Claude naming retained. |
| [deslop](src/pstack-codex/skills/deslop/SKILL.md) | Added by Claude | Same | Nothing changed from selected source. |
| [figure-it-out](src/pstack-codex/skills/figure-it-out/SKILL.md) | Changed in Claude | Body translated | No additional semantic drift identified in this review. |
| [fix-ci](src/pstack-codex/skills/fix-ci/SKILL.md) | Added by Claude | Same | Nothing changed from selected source. |
| [fix-merge-conflicts](src/pstack-codex/skills/fix-merge-conflicts/SKILL.md) | Added by Claude | Same | Nothing changed from selected source. |
| [get-pr-comments](src/pstack-codex/skills/get-pr-comments/SKILL.md) | Added by Claude | Same | Nothing changed from selected source. |
| [how](src/pstack-codex/skills/how/SKILL.md) | Changed in Claude | Body translated | Exploration counts retained; override wording caveat above. |
| [interrogate](src/pstack-codex/skills/interrogate/SKILL.md) | Changed in Claude | Body translated | Existing independent reviewer panel retained. |
| [maintain-verification-skill](src/pstack-codex/skills/maintain-verification-skill/SKILL.md) | Changed in Claude | Body translated | Existing source readers use approved Luna/max. |
| [make-bot-ui](src/pstack-codex/skills/make-bot-ui/SKILL.md) | Original-only retained | Body translated | Original-only capability retained with explicit prerequisites. |
| [make-pr-easy-to-review](src/pstack-codex/skills/make-pr-easy-to-review/SKILL.md) | Added by Claude | Same | Nothing changed from selected source. |
| [no-comments](src/pstack-codex/skills/no-comments/SKILL.md) | Changed in Claude | Body translated | Comment Sicko persona and rules retained. |
| [poteto-mode](src/pstack-codex/skills/poteto-mode/SKILL.md) | Changed in Claude | Body translated | Core routing and gates retained; cross-cutting F2–F4 above. |
| [principle-attack-the-premise](src/pstack-codex/skills/principle-attack-the-premise/SKILL.md) | Changed in Claude | Metadata only | Substantive Claude change, unchanged Codex body. |
| [principle-boundary-discipline](src/pstack-codex/skills/principle-boundary-discipline/SKILL.md) | Changed in Claude | Metadata only | No additional semantic drift identified in this review. |
| [principle-build-the-lever](src/pstack-codex/skills/principle-build-the-lever/SKILL.md) | Changed in Claude | Metadata only | No additional semantic drift identified in this review. |
| [principle-encode-lessons-in-structure](src/pstack-codex/skills/principle-encode-lessons-in-structure/SKILL.md) | Changed in Claude | Metadata only | No additional semantic drift identified in this review. |
| [principle-exhaust-the-design-space](src/pstack-codex/skills/principle-exhaust-the-design-space/SKILL.md) | Changed in Claude | Metadata only | No additional semantic drift identified in this review. |
| [principle-experience-first](src/pstack-codex/skills/principle-experience-first/SKILL.md) | Changed in Claude | Metadata only | No additional semantic drift identified in this review. |
| [principle-fix-root-causes](src/pstack-codex/skills/principle-fix-root-causes/SKILL.md) | Changed in Claude | Metadata only | No additional semantic drift identified in this review. |
| [principle-foundational-thinking](src/pstack-codex/skills/principle-foundational-thinking/SKILL.md) | Changed in Claude | Metadata only | No additional semantic drift identified in this review. |
| [principle-guard-the-context-window](src/pstack-codex/skills/principle-guard-the-context-window/SKILL.md) | Changed in Claude | Metadata only | No additional semantic drift identified in this review. |
| [principle-laziness-protocol](src/pstack-codex/skills/principle-laziness-protocol/SKILL.md) | Changed in Claude | Metadata only | No additional semantic drift identified in this review. |
| [principle-make-operations-idempotent](src/pstack-codex/skills/principle-make-operations-idempotent/SKILL.md) | Changed in Claude | Metadata only | No additional semantic drift identified in this review. |
| [principle-migrate-callers-then-delete-legacy-apis](src/pstack-codex/skills/principle-migrate-callers-then-delete-legacy-apis/SKILL.md) | Changed in Claude | Metadata only | No additional semantic drift identified in this review. |
| [principle-minimize-reader-load](src/pstack-codex/skills/principle-minimize-reader-load/SKILL.md) | Changed in Claude | Metadata only | No additional semantic drift identified in this review. |
| [principle-model-the-domain](src/pstack-codex/skills/principle-model-the-domain/SKILL.md) | Changed in Claude | Metadata only | No additional semantic drift identified in this review. |
| [principle-never-block-on-the-human](src/pstack-codex/skills/principle-never-block-on-the-human/SKILL.md) | Changed in Claude | Body translated | Approved external-message clarification. |
| [principle-outcome-oriented-execution](src/pstack-codex/skills/principle-outcome-oriented-execution/SKILL.md) | Changed in Claude | Metadata only | No additional semantic drift identified in this review. |
| [principle-prove-it-works](src/pstack-codex/skills/principle-prove-it-works/SKILL.md) | Changed in Claude | Metadata only | No additional semantic drift identified in this review. |
| [principle-redesign-from-first-principles](src/pstack-codex/skills/principle-redesign-from-first-principles/SKILL.md) | Changed in Claude | Metadata only | No additional semantic drift identified in this review. |
| [principle-separate-before-serializing-shared-state](src/pstack-codex/skills/principle-separate-before-serializing-shared-state/SKILL.md) | Changed in Claude | Metadata only | No additional semantic drift identified in this review. |
| [principle-sequence-verifiable-units](src/pstack-codex/skills/principle-sequence-verifiable-units/SKILL.md) | Changed in Claude | Metadata only | No additional semantic drift identified in this review. |
| [principle-subtract-before-you-add](src/pstack-codex/skills/principle-subtract-before-you-add/SKILL.md) | Changed in Claude | Metadata only | No additional semantic drift identified in this review. |
| [principle-test-behavior-not-implementation](src/pstack-codex/skills/principle-test-behavior-not-implementation/SKILL.md) | Changed in Claude | Metadata only | Substantive Claude change, unchanged Codex body. |
| [principle-type-system-discipline](src/pstack-codex/skills/principle-type-system-discipline/SKILL.md) | Changed in Claude | Metadata only | No additional semantic drift identified in this review. |
| [recall](src/pstack-codex/skills/recall/SKILL.md) | Changed in Claude | Body translated | Scoped native transcript evidence. |
| [reflect](src/pstack-codex/skills/reflect/SKILL.md) | Changed in Claude | Body translated | Three reviewers + synthesizer retained; F1 authoring dependency. |
| [setup-pstack](src/pstack-codex/skills/setup-pstack/SKILL.md) | Changed in Claude | Body translated | 17 roles and shared-sheet semantics retained; no setup verify offer inherited. |
| [show-me-your-work](src/pstack-codex/skills/show-me-your-work/SKILL.md) | Changed in Claude | Body translated | Trail and evidence requirements retained. |
| [swarm](src/pstack-codex/skills/swarm/SKILL.md) | Changed in Claude | Body translated | Worker contract retained; approved Sol default. |
| [tdd](src/pstack-codex/skills/tdd/SKILL.md) | Changed in Claude | Same | Nothing changed from selected source. |
| [teach](src/pstack-codex/skills/teach/SKILL.md) | Changed in Claude | Body translated | Native request/effort mechanics; workflow retained. |
| [technical-writing](src/pstack-codex/skills/technical-writing/SKILL.md) | Changed in Claude | Same | Nothing changed from selected source. |
| [thermo-nuclear-code-quality-review](src/pstack-codex/skills/thermo-nuclear-code-quality-review/SKILL.md) | Added by Claude | Same | Nothing changed from selected source. |
| [typescript-best-practices](src/pstack-codex/skills/typescript-best-practices/SKILL.md) | Changed in Claude | Metadata only | Automatic path activation unproven. |
| [unslop](src/pstack-codex/skills/unslop/SKILL.md) | Changed in Claude | Same | Nothing changed from selected source. |
| [what-did-i-get-done](src/pstack-codex/skills/what-did-i-get-done/SKILL.md) | Added by Claude | Same | Nothing changed from selected source. |
| [why](src/pstack-codex/skills/why/SKILL.md) | Changed in Claude | Body translated | Sol investigation and synthesis retained. |

The three nested Benny skills (`setup-benny`, `triage-issue-reports`, `reproduce-and-fix-issues`) are original-only imports. Each retains its workflow, adds the explicit unsupported-integration prerequisite and has a generated explicit-only invocation policy. Their paths and hashes are in the inventory.

**Per-playbook comparison index**

| Playbook | Original→Claude | Selected source→Codex | Audit note |
| --- | --- | --- | --- |
| [authoring-a-skill](src/pstack-codex/skills/poteto-mode/playbooks/authoring-a-skill.md) | Changed in Claude | Translated | No additional semantic drift identified. |
| [autonomous-run](src/pstack-codex/skills/poteto-mode/playbooks/autonomous-run.md) | Changed in Claude | Translated | Stop predicate retained; scheduler lifecycle F4. |
| [autopilot-full](src/pstack-codex/skills/poteto-mode/playbooks/autopilot-full.md) | Changed in Claude | Translated | Operator-only merge inherited; scheduler lifecycle F4. |
| [autopilot-stack](src/pstack-codex/skills/poteto-mode/playbooks/autopilot-stack.md) | Changed in Claude | Translated | Existing stack ownership and operator merge gates retained. |
| [babysit](src/pstack-codex/skills/poteto-mode/playbooks/babysit.md) | Changed in Claude | Translated | Frontier and stop gates retained; scheduler lifecycle F4. |
| [bug-fix](src/pstack-codex/skills/poteto-mode/playbooks/bug-fix.md) | Changed in Claude | Translated | Red-first and mechanism proof retained. |
| [eval](src/pstack-codex/skills/poteto-mode/playbooks/eval.md) | Changed in Claude | Translated | Existing independent checks retained; configured-model diversity approved. |
| [feature](src/pstack-codex/skills/poteto-mode/playbooks/feature.md) | Changed in Claude | Translated | Ordered design/delegation/verify/PR workflow retained. |
| [hillclimb](src/pstack-codex/skills/poteto-mode/playbooks/hillclimb.md) | Changed in Claude | Same | Nothing changed from selected source. |
| [investigation](src/pstack-codex/skills/poteto-mode/playbooks/investigation.md) | Same in both | Same | Nothing changed from selected source. |
| [multi-phase-plan](src/pstack-codex/skills/poteto-mode/playbooks/multi-phase-plan.md) | Changed in Claude | Translated | Ten lanes and review gates retained; inherited merge-owner contradiction. |
| [opening-a-pr](src/pstack-codex/skills/poteto-mode/playbooks/opening-a-pr.md) | Changed in Claude | Translated | No additional semantic drift identified. |
| [orchestrate](src/pstack-codex/skills/poteto-mode/playbooks/orchestrate.md) | Changed in Claude | Translated | Coordinator/worker/verifier split retained; local worktree adaptation. |
| [pause-safely](src/pstack-codex/skills/poteto-mode/playbooks/pause-safely.md) | Changed in Claude | Same | Durable storage improvements inherited from Claude. |
| [perf-issue](src/pstack-codex/skills/poteto-mode/playbooks/perf-issue.md) | Changed in Claude | Same | Nothing changed from selected source. |
| [prototype](src/pstack-codex/skills/poteto-mode/playbooks/prototype.md) | Changed in Claude | Same | Nothing changed from selected source. |
| [refactoring](src/pstack-codex/skills/poteto-mode/playbooks/refactoring.md) | Changed in Claude | Same | Nothing changed from selected source. |
| [runtime-forensics](src/pstack-codex/skills/poteto-mode/playbooks/runtime-forensics.md) | Changed in Claude | Same | Nothing changed from selected source. |
| [session-pickup](src/pstack-codex/skills/poteto-mode/playbooks/session-pickup.md) | Changed in Claude | Translated | No additional semantic drift identified. |
| [shipping](src/pstack-codex/skills/poteto-mode/playbooks/shipping.md) | Changed in Claude | Translated | Stronger merge protections inherited from Claude. |
| [trace-forensics](src/pstack-codex/skills/poteto-mode/playbooks/trace-forensics.md) | Same in both | Same | Nothing changed from selected source. |
| [visual-parity](src/pstack-codex/skills/poteto-mode/playbooks/visual-parity.md) | Changed in Claude | Translated | No additional semantic drift identified. |
| [worktree-cleanup](src/pstack-codex/skills/poteto-mode/playbooks/worktree-cleanup.md) | Changed in Claude | Translated | Approved recoverable-archive exception; native evidence caveats above. |
