# Write and publish the review packet

The packet has two parts: a short PR body and one linked review appendix. Keep a local Markdown copy of each in the task's existing artifact directory, or an uncommitted `.audit/pr-<number-or-task-slug>/` directory. Keep `publication.json` beside them with the repository, PR URL/number, forge, base/head SHAs, appendix comment ID/URL, author identity and last published content hash. These files are working artifacts; do not accidentally include them in the implementation commit.

## Body

Use pstack's existing section order and roughly 40-line budget. This integrates HumanLayer's visual outline into pstack's briefing; it does not replace pstack's verification requirements with the HumanLayer template.

- **Why:** the user problem and chosen approach in one or two short paragraphs; link a relevant ticket when available.
- **Scope:** the main symbols and a short reading order, separating core behavior from generated/mechanical changes. Add one compact structural view from [Visual outlines](visual-outline.md), next to the sentence it explains. Choose a before/after diff, data/contract sketch, pseudocode, component/call tree or Mermaid diagram. Do not pad a trivial change with a large diagram.
- **Tradeoffs:** only material choices the reviewer would otherwise ask about. A recovered plausible rationale must be labeled an inference, never presented as a historical decision.
- **Blast Radius:** affected callers, compatibility, migrations or rollout risks. Carry forward material human notes.
- **Verification:** actual checks and outcomes, including failed, skipped or pending checks. Link the review appendix for the detailed decision and evidence trail. Link screenshots/video only when they support a specific claim.

Keep full SHAs, extensive reading lists, measurements, logs and review receipts in the appendix. A compact visual is part of the body budget, not an exemption from it. Preserve required repository template fields when applicable, while keeping prose concise.

## Appendix

Build a readable view from the canonical trail owned by [show-me-your-work](../../show-me-your-work/SKILL.md), source, commits and real receipts. This view can be refreshed; its source log remains append-only under that skill's rules. Keep the raw trail uncommitted where its caller requires that, including both Autopilots. Publish only relevant evidence and safe excerpts, never secrets or a private transcript dump.

Use these headings, omitting empty optional detail:

```markdown
<!-- pstack-codex:review-packet:v1 -->
## Review appendix

### Revision and coverage
Compared base: <branch and full SHA>. Head: <branch and full SHA>.
Evidence scope: <contemporaneous trail and run(s), or recovered facts with gaps>.
Stage: <initial / refreshed / final handoff; name pending work>.

### Reading order
<Core paths/symbols with commit-permanent source links; mechanical files last.>

### Decisions and outcomes
| Decision | Recorded reason or explicitly labeled inference | Evidence | Outcome |
| --- | --- | --- | --- |
<Relevant choices, rejected approaches, reverts and superseding corrections.>

### Verification evidence
| Claim | Check or observation | Revision tested | Result | Evidence |
| --- | --- | --- | --- | --- |
<Actual commands/scenarios, results and accessible artifact links.>

### Attention
Transcript audit: <complete / partial / unavailable / pending; exact scope and gaps>.
Trail review: <actual different model, reviewed scope and receipt; or pending/unavailable>.
<Flags tied to decisions/evidence. No flags only if the review actually returned that.>
<Unresolved risks, failed checks, missing history, and evidence available only locally.>
```

Fill the template with observed facts; remove unused placeholder rows. Never backdate reconstructed decisions. If the original log or full scoped transcript is missing, say which historical actions cannot be verified. The current run can audit its own review actions without claiming to have audited the implementation run. Do not hide a material failure or abandoned approach merely because a later attempt passed.

For each result, retain the revision actually tested. A push, rebase or retarget requires checking the current diff and which claims remain supported. Mark stale results historical or rerun the affected check under the caller's existing verification rules. An unchanged patch alone does not prove unchanged base behavior. Preserve valid receipts rather than inventing reruns. Diagrams must match the compared source; a source diagram is not a screenshot of a running application.

## Publication and refresh

1. **Prepare locally.** Save `pr-body.md` and `review-appendix.md`. For an early PR, explicitly mark outstanding tests, transcript audit and independent review pending. Do not delay an Autopilot's early ready PR for an end-of-run audit. Never equate a ready PR with completed verification.
2. **Respect the caller's write scope.** If asked only for a local draft, return files without forge writes. Otherwise use the forge already resolved by the caller for all PR operations. Keep supported tool syntax grounded in the installed tool's schema/help. If the selected forge cannot publish a comment, report the limitation and return the prepared appendix; do not silently switch forge or invent a remote link.
3. **Create once, update the same appendix.** A new PR must exist before posting its appendix. For an existing PR, read any saved publication identity and fetch the PR/comments, including pagination. Before editing, verify repository, PR, comment author and the exact marker above, plus the saved ID when available. If the ID is missing, recover it only from a single unambiguous owned marked comment. If several candidates exist, ownership is unclear, or saved identity contradicts live state, resolve that ambiguity before writing; do not overwrite a human comment or blindly create duplicates. If there is no existing marked comment and the read was complete, create one. A failed/timed-out write has an unknown outcome: read back and recover its identity before retrying. Re-read content before updates and retain substantive intervening human edits.
4. **Link it from the body.** Capture the actual returned appendix URL, persist the identity, then replace the body's pending appendix text with a Markdown link. Use structured body arguments or saved body files, never shell-interpolated multiline text. Preserve unrelated body content and required fields. Attach newly created PRs using the host's PR attachment tool when available.
5. **Verify the published result.** Read back the body and appendix and compare them with the intended files. Confirm the target base/head still matches; if it moved, refresh affected claims before final handoff. Check that evidence links resolve for the intended audience. Local paths, workstation-only HTML, nonexistent uploads and inaccessible private transcripts are not remote proof links. Use commit-permanent code links and real run/artifact URLs, or include a relevant safe excerpt with its source/revision and label its limits. If evidence can only be viewed locally, say so explicitly rather than implying the PR carries it.
6. **Refresh before delivery.** Update this same comment and the short body after verification or relevant changes. Retain material corrections and findings. Report any publication or audit gap; saving files is not proof of a published update. This packet changes neither the caller's review gates nor who can merge.

The final reply links the PR and appendix (or local files if unpublished), gives the reading order and actual verification outcome, and ends with show-me-your-work's Attention report. A completed review needs a real different-model receipt. A partial or pending review names the limitation; it cannot produce a clean claim.
