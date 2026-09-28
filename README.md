# pstack-codex

Original pstack with the pinned pstack-claude updates, written directly for Codex
and local worktrees. The native package preserves upstream workflow scope,
stages, roles, panels, review requirements, and verification procedures. Version 0.4.0 adds the explicitly approved combined
PR review workflow described below.

The package is `src/pstack-codex`: **55 top-level skills, all 23 playbooks, and
3 nested Benny skills**. Hstack is not an input. Version 0.4.0 is the first public source release.
Installed behavior and live forge publication by the skills have not yet been validated.

## Sources

| Source | Pinned revision | Composition |
| --- | --- | --- |
| [Original pstack](https://github.com/cursor/plugins/tree/ecc249f1e306fc64ddf83c7bed16cacf7c2239db/pstack) | `ecc249f1e306fc64ddf83c7bed16cacf7c2239db` | Complete pstack subtree |
| [pstack-claude](https://github.com/michael-denyer/pstack-claude/tree/c02fd4922b25ee005f42042463d741d236c2c35e/plugins/pstack) | `c02fd4922b25ee005f42042463d741d236c2c35e` | Overlay shared paths; preserve original-only files |
| [HumanLayer skills](https://github.com/humanlayer/skills/tree/ca7c8088db69e315a8b2deea43820270457f8f3c) | `ca7c8088db69e315a8b2deea43820270457f8f3c` | Approved show-me/visual-pr composition and MIT license only |

The Claude port's upstream pin matches original pstack's subtree revision
`12d587d`. The 254-file package contains 109 byte-identical imported files,
134 declared native/approved edits, and 11 generated Codex files. The source
hashes stay pinned; fidelity validation reverses each declared edit to prove the
original content remains accounted for.

## Combined PR review workflow

[`make-pr-easy-to-review`](src/pstack-codex/skills/make-pr-easy-to-review/SKILL.md)
is the single entry point for a short PR briefing, a compact visual change
outline and reading order, and a linked appendix with decisions, tested revisions,
evidence and review flags. It starts the canonical trail when PR work starts;
existing PRs disclose missing history. Early PRs mark unfinished proof pending
and refresh the same appendix before handoff.

This is the extension approved in decision 12, adapting HumanLayer
[show-me and visual-pr](https://github.com/humanlayer/skills/tree/ca7c8088db69e315a8b2deea43820270457f8f3c)
with pstack show-me-your-work. Their plugins need not be installed. The standalone
trail skill, code-review requirements, forge choice, history-rewrite consent,
readiness and merge rules remain. See the [source notice](src/pstack-codex/skills/make-pr-easy-to-review/references/source-notice.md)
and bundled [HumanLayer MIT license](src/pstack-codex/THIRD_PARTY_LICENSES/HumanLayer.txt).

## Native Codex behavior

Skills now state Codex instructions directly. Small references cover delegation,
local worktrees, scheduled wakeups, and transcript evidence only where needed.
There is no required general platform-mapping read before executing a skill.

The approved audit corrections restore original Autopilot-full owner merges under
the full-autonomy grant and a clean root verdict, retaining stronger shipping
checks and operator-reserved/review-gated items. Native authoring, delegate reuse,
optional prompt entry points, scheduler shutdown and plan merge authority are
corrected. See [AUDIT-CORRECTIONS.md](AUDIT-CORRECTIONS.md).

The existing 17-role Markdown model sheet remains. Sol handles ordinary work and
conclusions, Astra handles strongest roles, and the existing explicit panels use
Astra/Sol/Luna. Existing How explorers and per-feature source readers use Luna at
`max`; Sol checks decisive evidence. Every Luna assignment requests `max`.
Unavailable requested models or efforts require a user choice before that step.
No provider routing layer or project JSON model configuration was added.

Concurrent repository writers receive separate physical checkouts and explicit
absolute paths. Managed worktree tooling is preferred where available. Unused
managed worktrees may be recoverably archived after needed work is preserved,
without another confirmation, as explicitly approved. Primary, pinned, shared,
and in-use worktrees remain protected.

History workflows use scoped Codex transcript evidence. The reader retains raw
records, tool calls/results, source lines, and evidence gaps. A summary is not
proof of exact actions. Reflect keeps its existing digest fallback.

The SessionStart hook retains startup/resume/clear/compact routing and the
`session hook: off` setting. It uses native `PLUGIN_ROOT` and Codex home. Actual
activation requires a supporting host, installation, and trust.

See [NATIVE-PORT-DECISIONS.md](NATIVE-PORT-DECISIONS.md) for the approvals and
[ADAPTATIONS.md](ADAPTATIONS.md) for every changed file. The exact reconstruction
patch is [patches/codex-compatibility.patch](patches/codex-compatibility.patch).

## Download and use

Download [pstack-codex-0.4.0.zip](https://github.com/huankoh/pstack-codex/releases/download/v0.4.0/pstack-codex-0.4.0.zip)
from the [v0.4.0 release](https://github.com/huankoh/pstack-codex/releases/tag/v0.4.0)
and extract it, or clone this repository:

```sh
git clone https://github.com/huankoh/pstack-codex.git
cd pstack-codex
```

Ask Codex to read `src/pstack-codex/skills/poteto-mode/SKILL.md` and apply it to
your task. For the standalone ZIP, the corresponding path is
`pstack-codex/skills/poteto-mode/SKILL.md`. The plugin manifest lives at
`src/pstack-codex/.codex-plugin/plugin.json` in this repository.
A checkout or ZIP extraction does not install the plugin or activate its hook.

For the combined visual PR workflow, use
[`make-pr-easy-to-review`](src/pstack-codex/skills/make-pr-easy-to-review/SKILL.md).
See the [local example PR](outputs/combined-pr-example/pr-body.md) and its evidence appendix.

## Use and limits

For source testing, give Codex the absolute path to a named skill's `SKILL.md`.
Start with `src/pstack-codex/skills/poteto-mode/SKILL.md` or a specific skill.
Source execution does not establish installed plugin discovery or hook activation.
[The package guide](src/pstack-codex/docs/guide/README.md) describes the workflows.

Desktop, CLI, and cloud are support targets, with actual capabilities checked at
the affected step. Identical tools, model controls, transcript access, scheduling,
or worktree features are not assumed. Grok Bot UI and Benny retain their original
external integration contracts and explicit prerequisites; their native webhook
and secret-handoff replacements are not approved. Benny remains dormant.

[VALIDATION.md](VALIDATION.md) separates completed checks from installation,
managed-worktree, all-host, and live PR/CI/shipping validation gaps.

## Development and reconstruction

Use Python with PyYAML, Bun, Node.js, Git, jq, and rg. Put Bun, Node, and rg on PATH
because helper tests launch subprocesses.

```sh
python3 tools/validate.py
python3 tools/provenance.py
python3 -m unittest discover -s tests -p 'test_*.py' -v
(cd src/pstack-codex/skills/poteto-mode/scripts && bun run typecheck)
bun test ./tests/*.test.mjs ./tests/*.test.ts \
  ./src/pstack-codex/skills/poteto-mode/scripts/watch-pr \
  ./src/pstack-codex/skills/poteto-mode/scripts/orch
python3 tools/build.py --output dist/pstack-codex-0.4.0.zip
```

For independent reconstruction, place the pinned repositories at
`work/repo-comparison/cursor-plugins`, `work/repo-comparison/pstack-claude`, and
`work/repo-comparison/humanlayer-skills-ca7c808`, then:

```sh
python3 tools/restore_baseline.py --output work/reconstructed-native-pstack-codex
```

The output must not exist. Reconstruction reads pinned Git objects, verifies their
hashes, applies the exact patch, and validates the result without overwriting the
active source or regenerating provenance from edited bytes.

## Change policy and history

[AGENTS.md](AGENTS.md) requires a concrete proposal, rationale, and explicit
approval for changes beyond faithful Codex compatibility. Remaining proposals are
in [PROPOSALS.md](PROPOSALS.md). Prompt simplifications are not part of this port.

The public Git history begins with this approved 0.4.0 snapshot. Earlier local
experiments and research checkouts are not part of the published repository.
Pinned upstream revisions, exact approval deltas and reconstruction instructions
preserve the source history without publishing abandoned local work.

## License and attribution

MIT. See [LICENSE](LICENSE), the bundled
[upstream notice](src/pstack-codex/NOTICE-pstack-claude.md),
[skills notice](src/pstack-codex/NOTICE-skills.md), and
[HumanLayer license](src/pstack-codex/THIRD_PARTY_LICENSES/HumanLayer.txt).
This is an independent Codex adaptation, not an official Cursor, Anthropic,
HumanLayer or OpenAI distribution.
