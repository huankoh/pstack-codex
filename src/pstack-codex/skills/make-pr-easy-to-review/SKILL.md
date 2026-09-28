---
name: make-pr-easy-to-review
description: Prepare or update a PR with concise context, a visual change outline, and a linked decision and verification trail. Use when opening a PR, preparing work for review, or asked to make a PR easy to understand, show its evidence, tidy its description, clean up commits, or annotate the diff.
---

# Make PR Easy to Review

Prepare a PR so a reviewer can quickly understand the intent, important files, and risk. The default goal is reviewability without behavior changes.

This is the combined PR entry point: HumanLayer's **show-me** supplies visual conventions, **visual-pr** supplies the concise change outline, and pstack's **show-me-your-work** owns the evidence log and its review. Use the bundled references; those other plugins need not be installed.

## Workflow

1. **Keep the trail as work happens.** When a task is expected to produce a PR, start or reuse the canonical trail through [show-me-your-work](../show-me-your-work/SKILL.md). Follow its run ownership and append-only rules. If invoked after implementation, log the current review work and label earlier facts as recovered; do not invent historical decisions, timestamps, or reasons. Starting the trail does not open a PR early or change the caller's execution stages.
2. **Resolve the review target.** Use the explicit PR or current branch, its actual base (the parent branch for a stack child), and exact base/head revisions. Keep the caller's resolved forge. For a direct invocation, use the forge selection in [Opening a PR](../poteto-mode/playbooks/opening-a-pr.md). Inspect dirty work, commits, the complete diff and enough surrounding source to establish behavior and ownership; read the task intent, relevant artifacts, current description and existing review notes.
3. **Prepare the briefing.** Identify noisy history, unrelated or mixed mechanical/logic changes, missing tests and unclear reviewer entry points. Read [Visual outlines](references/visual-outline.md) and [Review packet](references/review-packet.md). Write the existing Why / Scope / Tradeoffs / Blast Radius / Verification sections, dropping empty ones. Within Scope, give the reviewer a reading order and the smallest useful visual. Keep the body around 40 lines; put detailed decisions, evidence and review flags in the linked appendix. Preserve useful human-authored context.
4. **Check the evidence.** Follow show-me-your-work's transcript audit and different-model trail review before final handoff. State missing evidence and pending review explicitly. Reuse a completed review only for the same trail and evidence scope; review new or superseding rows before claiming completion. The trail review does not replace code review, tests, live proof, swarm verdicts, or any existing shipping gate.
5. **Publish or return prepared files.** Save the body, appendix and publication identity locally as described in Review packet. When called to prepare a PR, return these files to the caller, which owns commit/push/create; after creation, publish the appendix and refresh the body's link. When invoked directly for an existing PR, update it within the user's request. If creation is requested and no PR exists, apply Opening a PR's worktree, cleanup, writing, title, commit, forge, base and readiness requirements once, then create and attach the PR and publish this packet. Do not dispatch back into this skill from that playbook: these steps already perform its review-packet work. A request to draft text or prepare locally remains local. Do not infer permission to commit or push merely from a request to explain an existing change.
6. **Refresh at the handoff.** Early ready PRs may have pending tests and trail review. Update the same packet after verification, after relevant code/base changes, and before final review or an already-authorized merge. Recheck base/head, evidence applicability, links and the published text. Do not label results from an old revision as current. Preserve all existing readiness, babysit and merge boundaries.

Return the PR URL and appendix link, a short reading order, verification outcome and unresolved gaps. For local preparation, return the saved files and say they were not published. End with the Attention report required by show-me-your-work; pending or unavailable review is not "No flags". Never invent a reviewer identity or receipt.

## History Cleanup

Only rewrite history when the user asks for it or agrees to the plan. Before rewriting:

```bash
gh pr view <PR> --json title,headRefName,baseRefName,state,commits
git fetch origin <headRefName> <baseRefName>
ORIGINAL_TREE=$(git rev-parse origin/<headRefName>^{tree})
```

Good commit groupings usually follow dependency order:

1. Schema/storage or generated API definitions.
2. Core logic.
3. Wiring and integration.
4. UI or surface behavior.
5. Tests.

After rewriting, verify content identity:

```bash
echo "Original tree: $ORIGINAL_TREE"
echo "Current tree:  $(git rev-parse HEAD^{tree})"
git diff origin/<headRefName> --stat
```

Do not push if the tree changed unintentionally.

## Reviewer Guidance

When code behavior should stay untouched, prefer PR description and review notes:

- Add a TL;DR that matches the actual diff.
- Separate core files from generated or mechanical files.
- Call out risky behavior changes, migration order, rollout plan, and test coverage.
- Link issue trackers, dashboards, or design docs when they explain intent.

## Guardrails

- Never hide meaningful behavior changes inside "cleanup".
- Do not bypass hooks unless the user explicitly asks.
- If the PR is too large to make reviewable with notes, recommend splitting instead of polishing around the problem.

Visuals explain structure; screenshots, logs and test receipts prove observed behavior. Do not present one as the other. Combining the skills does not authorize unrelated code changes, a history rewrite, force-push, or a merge.
