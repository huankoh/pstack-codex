# Current validation — pstack-codex 0.4.0 combined PR extension

Decision 13 updates only the three manifest repository URLs for public release.
The prior unpublished 0.4.0 ZIP is retained locally; [publication deltas](outputs/publication-deltas.json) record its hash and exact changes.

Decision 12 is the user's approved combination of show-me, show-me-your-work and
visual-pr. The source package now contains 55 top-level skills, 3 nested skills
and 23 playbooks. No skill was removed or added to the top-level inventory.

| Check | Result |
| --- | --- |
| Fidelity, metadata, links, inventory | Passed; 109 identical imports, 134 declared adaptations, 11 generated files |
| Official skill and plugin validation | Both edited skill schemas and plugin schema passed |
| Python fidelity/package tests | 21 passed |
| Targeted plan/shipping tests | 21 passed, 54 assertions |
| Independent static review | Astra found no workflow defects; release-document version finding corrected |
| Independent forward exercise | Sol drafted from an actual fixture diff/receipts and selected the expected actions in 9 edge cases |
| Example evidence | Baseline fails 1 of 3 tests, head passes 3; 24-line body and local appendix/source/receipt links checked |
| Exact approval scope | 11 existing files reverse to preserved 0.3.1 bytes, 4 declared additions; all other package bytes unchanged |
| Pinned reconstruction and extraction | Passed; reconstruction ZIP byte-identical to source ZIP; extracted package validates |

The forward cases cover early pending proof, repeat updates, ambiguous and wrong
comment ownership, stale base/head receipts, timed-out writes, unavailable forge
comment support, explanation-only requests and added trail rows after review.
This is simulated action selection, not a remote publication test. The local
example is synthetic and explicitly discloses missing original history and live
proof; its agent did not invent a completed audit or reviewer receipt.

No live PR or comment was created. No installation, push, merge, webhook, scheduler,
all-host or installed automatic-selection validation is claimed. Prior runtime
limits remain. Canonical logging helpers and implementation code did not change;
the full helper suite from 0.3.0 was not unnecessarily rerun.

Artifact: [pstack-codex-0.4.0.zip](https://github.com/huankoh/pstack-codex/releases/download/v0.4.0/pstack-codex-0.4.0.zip). SHA-256:
`24eb8faf906df077d2311452728f7b52f6c9b0edeffdeaa7f6a736ff0c2b7894`.

[Example PR body](outputs/combined-pr-example/pr-body.md) ·
[Review appendix](outputs/combined-pr-example/review-appendix.md) ·
[Machine-readable results](outputs/combined-pr-validation.json) ·
[Exact approved delta](outputs/combined-pr-deltas.json).
