# Unapproved changes — not implemented

The active package is the faithful native Codex port with the individually approved changes. None of the following proposals is approved or implemented in it. Each would need its own concrete proposal, rationale, reviewable scope, and the user's explicit approval. This list is a record of deferred choices, not a request to approve them as a bundle. Approved native-port scope, including scoped transcript support, is recorded separately in [NATIVE-PORT-DECISIONS.md](NATIVE-PORT-DECISIONS.md).

| Potential change | Rationale | Tradeoff / baseline today |
| --- | --- | --- |
| Task-specific checkpoint namespaces | Concurrent tasks in one repository could retain distinct resume pointers. | Changes the upstream `resume.mjs` API and storage semantics; baseline uses the original shared locator. |
| Workspace/content drift checks when resuming | Detect edits made after a checkpoint and avoid treating stale state as current. | Adds fingerprint semantics and new rejection paths; baseline retains upstream verification behavior. |
| Broader checkpoint Markdown-link handling | The earlier prototype found gaps involving angle-bracket destinations, reference-style links, and local `file:` URLs. | Requires selecting and testing an explicit parsing contract; the prototype fix was reverted with the other custom helper changes. The baseline preserves upstream behavior. |
| Project-specific model sheets | The inherited setup has one shared sheet even when its rows load through a project AGENTS.md. | The native port makes that shared scope explicit. Separate project storage and precedence would change configuration semantics and need approval. |
| Selected hstack skills | A separately evaluated skill might fill a demonstrated need after baseline usage. | No hstack skill, routing code, or runtime layer is included. Name the exact skill and justify it before proposing import. |

The previous simplifications—reduced design/review requirements, fewer playbooks, custom project JSON model configuration, altered Comment Sicko rules, removed hook, and changed completion/retry defaults—are removed. They are not implicitly approved future work or recommended defaults. Any reconsideration starts with a new proposal.

## Approved message clarification (moved to implementation scope)

Status: approved by the user's `Agree` after the Slack/Teams examples. See decision 9 in [NATIVE-PORT-DECISIONS.md](NATIVE-PORT-DECISIONS.md). Implemented in the native port; this entry is retained as the proposal and rationale record and is an exception to the unapproved list above.

[Poteto mode, Autonomy](src/pstack-codex/skills/poteto-mode/SKILL.md#autonomy)
allows external actions including team chat without asking. The
[Never Block principle](src/pstack-codex/skills/principle-never-block-on-the-human/SKILL.md)
places external messages behind confirmation. These inherited instructions
disagree about whether an extra confirmation is required.

Proposed scope: reconcile only the message-authorization clauses in these two
skills with this rule:

> Send external messages only when the user has explicitly authorized the
> message or a workflow that includes it, or an explicitly invoked skill/plugin
> authorizes it under the host's rules. Reuse existing authorization; do not ask
> again for a message already covered. Otherwise prepare the message and ask
> before sending. Preserve the existing specific pause for customer messages.

Rationale: make the authorization boundary explicit and consistent while avoiding
repeated permission requests. This does not change ticket updates, evaluation
launches, or the other upstream pause gates. Host instructions remain binding
regardless of this proposal's approval status.

## Optional prompt changes to consider after native validation

The user-supplied [OpenAI prompting article](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra)
is guidance for evaluating instructions, not permission to simplify pstack.
Potential tensions to evaluate separately include broad Recall/Unslop triggers,
mandatory Architect exploration for code crossing a function boundary, verbatim
playbook checklists, and the Feature workflow's fixed stages. These are review
topics, not established defects or approved edits. Preserve them for the native
baseline. Any future proposal must name the exact change, rationale, and evidence.

## Unsupported-feature replacements

The user approved preparing individual proposals for Grok Bot UI, Benny webhook
integration, and other unavailable capabilities. No replacement, removal, or
automatic promotion of dormant skills has been approved. Each proposal must
identify the capability gap, concrete alternative, and effect on the upstream
workflow before requesting approval.


## Approved audit corrections and original merge authority

On 2026-09-28 the user approved the five concrete audit proposals and restored
original Autopilot-full merge authority, retaining the stronger shipping checks.
These are implemented in 0.3.1 and recorded as decisions 10-11 in
[NATIVE-PORT-DECISIONS.md](NATIVE-PORT-DECISIONS.md). See
[AUDIT-CORRECTIONS.md](AUDIT-CORRECTIONS.md) for scope and validation. The setup
verification offer, inherited invocation policies and principle changes were
explained; no alteration to those was approved or applied in this update.

## Approved combined visual PR workflow

Decision 12 (2026-09-28) implements the user's explicit request to combine
show-me, show-me-your-work and visual-pr in `make-pr-easy-to-review`. The proposal
is implemented in 0.4.0: compact visual briefing, reading order, and one linked
appendix with decision/evidence history and review flags. See
[NATIVE-PORT-DECISIONS.md](NATIVE-PORT-DECISIONS.md) for the exact approval and scope.
Other HumanLayer skills remain outside the package.
