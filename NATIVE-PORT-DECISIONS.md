# Native pstack-codex decision record

Recorded from the user interview on 2026-09-27. This document records approved
scope implemented in the native 0.4.0 source package, including the separately
approved audit corrections and combined PR extension below. The faithful 0.2.0 baseline
remains at commit `9550052`. See ADAPTATIONS.md for exact changes and VALIDATION.md
for completed checks and runtime limitations.

## Governing constraint

Keep original pstack with the pinned pstack-claude updates. Preserve workflow
scope, stages, roles, agent counts, panels, review requirements, verification,
and helper semantics except for the specific approved changes below. Every
additional change needs a concrete proposal, rationale, and explicit approval
under [AGENTS.md](AGENTS.md). Hstack is not an input.

## Interview decisions

| Decision | Approved scope | Approval in this conversation |
| --- | --- | --- |
| 1. Hosts | Target Codex desktop, CLI, and cloud. Check actual host capabilities and disclose gaps; support targeting is not proof that all hosts expose identical controls. | `1C` |
| 2. Native instructions | Write Codex instructions directly in affected skills and playbooks. Use small, task-specific references where useful; remove the mandatory general Claude-to-Codex mapping detour. | `go with A` after the organization options were explained |
| 3. Unsupported features | Prepare individual replacement proposals for Grok Bot UI, Benny webhooks, and other unavailable capabilities. Preserve them pending decisions. This approves proposals, not their implementation or removal. | `3C` |
| 4. Roles and counts | Preserve each skill's actual role contract. Reflect retains three perspectives and one synthesizer. How has no critics stage. Remove contradictory mapping claims without introducing stages or extra agents. | `ok looks good to me for now` after the role explanation |
| 5. Models | Use Sol for ordinary work and conclusions, Astra for strongest roles, and Astra/Sol/Luna for the existing explicit panels. Apply the Luna refinement below. | Acceptance of the proposed model table, followed by the Luna discussion and agreement that Sol inspects and determines conclusions |
| 6. Transcript evidence | Plan native Codex transcript support, including a scoped reader where necessary, preserving the original evidence requirements. | `A` in response to the native-transcript options |
| 7. Worktree cleanup | Allow recoverable archival without another confirmation when the worktree is no longer in use and all needed work is preserved. Destructive deletion still needs confirmation. | `7B.` after the difference from 7A was explained |
| 8. Unavailable model/effort | Report the limitation and ask for a replacement before continuing the affected step. Do not silently substitute a model or lower effort. | `8A` |
| 9. Message authorization | Send team/external messages only when already authorized by the user or an explicitly invoked workflow allowed by the host. Reuse existing authorization; otherwise draft and ask before sending. Preserve the specific customer-message pause. | `Agree` after the Slack/Teams examples distinguishing “fix and post an update” from “fix this bug” |

## Model details

The existing role sheet and its configuration intent remain; this is not a new
routing layer. Preserve existing user overrides and aliases.

| Existing work or role | Native default |
| --- | --- |
| Feature/refactoring, judgment/prose, How explainer, Why investigators/synthesizer, Reflect roles, Swarm workers | `gpt-6-sol` |
| Bug fix, performance issue, hillclimb, strongest judgment | `gpt-6-astra` |
| Arena runners, Architect runners, Interrogate reviewers | `gpt-6-astra`, `gpt-6-sol`, `gpt-6-luna` under each skill's existing panel rules |
| Arena cross-judge pool | Same three-model pool; still one judge selected under the existing rules |
| How explorer; existing per-feature source readers in maintain-verification-skill; clearly scoped, already-delegated retrieval work | `gpt-6-luna` with `max` effort |

All Luna assignments request `max`, including its participation in existing
panels. Luna does not support `ultra`. No change to Sol or Astra effort was
agreed; retain the configured/session effort. Model and effort availability
remain host-dependent, with decision 8 governing unavailable choices.

Sol inspects decisive source evidence and determines conclusions; a Luna summary
is not a substitute for that inspection. Do not add a compulsory scouting stage
before ordinary reads. Keep Why investigators and Reflect tooling on Sol because
their existing work includes interpretation. The retrieval refinement does not
remove Luna from the approved explicit panels. Representative validation is
still needed before claiming the assignments work reliably.

## Worktree boundary for decision 7B

The approved change relaxes only the extra confirmation for recoverable archival.
It does not make unfinished or active work eligible for cleanup.

- Reuse a suitable free checkout before creating another. Separate concurrent
  writers need separate physical checkouts and explicit checkout ownership.
- Before archival, verify no ongoing task or process needs the checkout and
  account for existing changes. Preserve primary, pinned, shared, and in-use
  worktrees.
- Prefer managed archive tooling where available. It saves tracked files and
  non-ignored untracked files. Preserve any needed ignored files separately first.
- Report what was archived. A merged PR alone is not a reason to archive.
- Where recoverable managed archival is unavailable, do not treat 7B as
  permission to delete unsaved work or invent a substitute cleanup procedure.

This is an expressly approved departure from the inherited pause before cleaning
up a worktree containing uncommitted changes.

## Evidence and implementation boundaries

Transcript access stays within the relevant chat/workspace and selected
topic/time window. A summary or truncated history response cannot establish
exact tool-use or file-read claims. Preserve Reflect's existing digest fallback
and distinguish it from full transcript evidence. Verify any native reader
against the actual supported record format; changing a Claude transcript path
alone is insufficient.

Keep the pinned source provenance and exact reconstruction patch. Declare native
translations and approved behavioral exceptions individually. Evolve fidelity
checks to allow those declared changes while detecting unrelated workflow drift;
do not merely replace expected hashes with whatever the edited files contain.

The previous baseline validation does not validate the forthcoming native port.
This interview does not authorize installation, publication, personal
configuration edits, or live PR/CI/shipping actions.

## Remaining proposals

Unapproved proposals remain outside the active package in
[PROPOSALS.md](PROPOSALS.md). The external-message wording conflict is resolved
by decision 9; host and user authorization continues to govern execution.
Optional prompt simplifications and unsupported-feature replacements are not
implicitly approved by this decision record.

## Approved audit corrections — 2026-09-28

The user approved the five concrete audit proposals with: "agree proceed with
the five." These are decision 10:

1. Route Automate-me and Reflect authoring through Codex `skill-creator`,
   preserving approval, drafting, validation and iteration requirements.
2. Restore reuse of an existing poteto delegate through native follow-up controls.
3. Remove the obsolete general-mapping detour from all 31 optional prompt wrappers.
4. Retain the recurring automation identity and explicitly end or suspend it at
   the workflow's existing completion, stop, hold and terminal conditions.
5. Make the plan template defer merge authority to its selected execution playbook.

The user also said: "for the three, make it as autonomous as original pstack,
ok, and why are we removing verification skill and invocation rules changed?
explain the last one". This is decision 11: restore original Autopilot-full's
owner-merge authority under the operator's full-autonomy grant and the root's
clean verdict. Preserve operator-named items, explicit interaction review gates,
state-then-wait, and Autopilot-stack's operator landing. Keep the stronger Claude
shipping checks and durable resume storage. Update affected routing and guide
text to match; do not rewrite upstream historical notices.

The verification skills remain bundled. Setup's removed optional creation offer,
the inherited invocation-policy changes and the two changed principles are
explanation-only in this request; they are not approved for alteration. These
approvals change the source package, not permission to merge a live PR, install
or publish the plugin, or create a live recurring automation for testing.

## Approved combined PR review workflow — 2026-09-28

Decision 12. The user explicitly requested:

> ok let's combine all 3 into one on the PR skill. show-me + show-me-your-work + visual-PR so it produces PR i can context with visual contexts, outlines and evidence trail

Extend the existing `make-pr-easy-to-review` entry point with HumanLayer show-me
visual conventions and visual-pr's concise structural outline, while reusing
pstack show-me-your-work for the canonical trail, transcript audit and independent
different-model review. Keep pstack's short PR body sections; link a readable
appendix with decisions, tested revisions, proof links, review flags and gaps.
Begin logging when PR work begins; distinguish recovered facts from historical
reasons that were never recorded. Publish and refresh one owned appendix per PR.
Early ready PRs may show pending proof and review until those steps run.

Route normal PR creation, both Autopilots, the multi-phase checklist and shipping
refresh through this entry point. Keep the standalone trail skill unchanged for
other uses. Preserve existing role/panel counts, code review and verification
requirements, forge choice, stack bases, readiness, history-rewrite consent,
babysit triggers and merge authority. Do not import HumanLayer's explicit-only
invocation policy or replace pstack's body template. No other HumanLayer skills
are approved. Retain its pinned source attribution and MIT license.

Rationale: the reviewer should see why the change exists, how its structure
changes, where to start reading, and what evidence supports it in one PR workflow.
The readable appendix keeps this context accessible without inflating the squash
commit body or publishing raw private transcripts. This is a deliberate approved
extension, not a claim that upstream already combined these three skills.

Version 0.4.0 is a source-package update. This request does not authorize a live
PR, comment, installation, publication, push, merge or automation for testing.

## Public GitHub distribution — 2026-09-28

Decision 13. The user requested: "great. Now this pstack-codex is ready. Let's open a new github package public with this skil".

Publish the approved pstack-codex source as the public `huankoh/pstack-codex`
repository with a versioned 0.4.0 ZIP release. Set the plugin homepage, repository
and interface website to that repository, preserving upstream attribution.
Prepare portable public documentation, a root MIT license and selected validation
evidence. Start the public repository with a clean source snapshot; keep local
research, private runtime state and abandoned development history out of it.
No skill procedure, model choice, invocation policy or shipping gate changes.
This approval authorizes publication, not installation on the user's machine.
