# pstack-codex

**Understand the code. Make a plan. Build it. Prove it works.**

pstack-codex gives Codex a set of engineering workflows for taking a task from an
idea to a change you can review. Start with **poteto-mode**: it chooses the right
playbook and brings in the other skills as needed.

This is a Codex adaptation of [Lauren Tan's pstack](https://github.com/cursor/plugins/tree/ecc249f1e306fc64ddf83c7bed16cacf7c2239db/pstack),
with the pinned [pstack-claude updates](https://github.com/michael-denyer/pstack-claude/tree/c02fd4922b25ee005f42042463d741d236c2c35e/plugins/pstack).
It keeps their engineering workflows and review requirements, adapts them to
Codex and local worktrees, and adds a combined visual PR workflow.

[Set it up](#set-it-up) · [Try it](#start-with-poteto-mode) · [Visual PRs](#prs-you-can-follow) · [Full guide](src/pstack-codex/docs/guide/README.md)

## What you get

- **A starting point for the whole task.** Poteto-mode routes investigation, design, implementation, review and delivery through the relevant playbooks.
- **Parallel work with clear ownership.** Concurrent coding agents work in separate local worktrees. Design and review workflows retain their independent perspectives.
- **Evidence you can inspect.** Decisions, checks, outcomes and gaps stay visible, including during long or unattended work.
- **PRs you can follow.** A short explanation, useful diagrams or code outlines, a reading order and a linked evidence trail.

The package contains **55 top-level skills, 23 playbooks and 3 nested Benny skills**.
You can use poteto-mode for the overall workflow or choose a specific skill.

## Set it up

Paste this into a Codex chat with access to your local files and terminal:

```text
Install https://github.com/huankoh/pstack-codex as a Codex plugin on this machine.
Use a Git checkout of tag v0.4.0. Read its README and use the built-in
plugin-creator skill if available, checking the installation commands supported
by my Codex host.

The plugin is at src/pstack-codex inside the repository. Its manifest is
src/pstack-codex/.codex-plugin/plugin.json. Install the whole plugin, including
its skills, references, helpers and hooks; do not install the skills separately.

This repository has no marketplace catalog. Register the existing plugin in my
personal marketplace. For a local copy, use ~/plugins/pstack-codex and an entry
in ~/.agents/plugins/marketplace.json whose source.path is ./plugins/pstack-codex.
Preserve the marketplace's actual name and other entries. Inspect any existing
installation first, preserve local changes, and avoid duplicate registrations.
Keep the supplied plugin files unchanged; do not scaffold over them.

Use the supported install flow. If the CLI supports it, install with
codex plugin add pstack-codex@<actual-marketplace-name> and verify with
codex plugin list. Otherwise, guide me through the app's Plugins Directory.
Report what is installed and any remaining manual step. Tell me when to refresh
or restart the app and start a new chat to confirm the skills are available.
Do not claim the session hook is active without checking support and trust.
```

This uses a personal marketplace because the repository currently ships plugin
source rather than its own marketplace catalog. The installation approach follows
[OpenAI's plugin setup guidance](https://developers.openai.com/plugins/build/plugins).
The prompt asks Codex to perform the setup; cloning or downloading alone does not
install the plugin.

Once it is installed, start a **new chat** and paste:

```text
Use pstack-codex's setup-pstack skill to configure it with me.
Check the models and reasoning levels available for subagents on this host.
Preserve my existing choices, explain the configuration scope, and ask before
changing them. Walk me through the session-hook choice and confirm what is
supported and trusted here. If a requested model is unavailable, let me choose
its replacement.
```

[Setup-pstack](src/pstack-codex/skills/setup-pstack/SKILL.md) handles model choices,
reasoning effort and the session-hook setting. The model sheet is shared across
projects; setup explains where its instructions will load before you confirm.

Prefer to download the files yourself? Get the
[v0.4.0 ZIP and checksum](https://github.com/huankoh/pstack-codex/releases/tag/v0.4.0).
The extracted plugin folder is `pstack-codex/`. From a repository clone, it is
`src/pstack-codex/`.

## Start with poteto-mode

Describe the task and ask for poteto-mode. For example:

```text
Use pstack-codex's poteto-mode to fix this bug. Reproduce it first, make the
change, and show me the evidence that it works.
```

```text
Use poteto-mode to add this feature. Work in a local worktree, verify the result,
and open a PR with a visual explanation and evidence trail.
```

```text
Use poteto-mode to explain how this subsystem works before we change it.
```

Poteto-mode brings in the relevant skills as the work progresses. You can also
ask for one directly:

| When you want to… | Ask for… |
| --- | --- |
| Understand how the code works | [how](src/pstack-codex/skills/how/SKILL.md) |
| Investigate why it was built that way | [why](src/pstack-codex/skills/why/SKILL.md) |
| Explore a design before implementing it | [architect](src/pstack-codex/skills/architect/SKILL.md) |
| Compare multiple implementation attempts | [arena](src/pstack-codex/skills/arena/SKILL.md) |
| Have independent models challenge a change | [interrogate](src/pstack-codex/skills/interrogate/SKILL.md) |
| Prepare a PR with visual context and evidence | [make-pr-easy-to-review](src/pstack-codex/skills/make-pr-easy-to-review/SKILL.md) |
| Keep a decision trail for longer work | [show-me-your-work](src/pstack-codex/skills/show-me-your-work/SKILL.md) |
| Get a plain explanation of the last response | [bro](src/pstack-codex/skills/bro/SKILL.md) |

For PR status or follow-up work, ask **poteto-mode to babysit the PR**. For ordinary
tasks, opening a PR does not automatically start babysitting or authorize a merge.

## PRs you can follow

The combined **make-pr-easy-to-review** skill brings together HumanLayer's
**show-me** and **visual-pr** conventions with pstack's **show-me-your-work** trail.
You do not need to install those other plugins or invoke three separate skills.

When poteto-mode works toward a PR, it starts recording meaningful decisions.
At PR creation and final handoff, the combined skill prepares:

| In the PR body | In the linked review appendix |
| --- | --- |
| Why the change exists and what it touches | Decisions, reasons and outcomes |
| A compact visual outline and where to start reading | Test results and the revisions they actually tested |
| Tradeoffs, risks and a short verification result | Evidence links, review flags and missing proof |

The visual can be a **call tree, control-flow sketch, Mermaid diagram, component
tree, code snippet or before/after diff**. The skill chooses the view that makes
the change easiest to understand.

Early PRs show unfinished checks as pending. Existing PRs with missing history
say what could be recovered and what could not. The same appendix is refreshed
as verification finishes or the relevant code changes.

[See an example PR body](outputs/combined-pr-example/pr-body.md) and its
[review appendix](outputs/combined-pr-example/review-appendix.md). These are local
fixture outputs, with real test receipts and explicitly recorded evidence gaps.

## Longer tasks and autonomous work

The existing playbooks still control how far the work goes:

- **Ordinary tasks:** use the relevant playbook, verify the work and prepare the PR. Ask separately for babysitting or shipping when needed.
- **Autopilot-full:** build and land independent PRs under your full-autonomy grant, after the required independent verification. Items reserved for you and explicit review gates still wait for you.
- **Autopilot-stack:** build and verify a sequence of PRs, then hand you the stack to review and land.

The visual PR workflow keeps the explanation and evidence current throughout.
It does not replace code review or change who may merge.

## Models and host support

The defaults use **Sol** for ordinary implementation and conclusions, **Astra**
for the strongest judgment roles, and **Luna at max effort** for selected context
retrieval. Existing multi-model panels use all three. Setup preserves user
overrides and checks actual availability before using a requested model or effort.

Local worktrees isolate concurrent writers. History-based skills use transcripts
scoped to the relevant work. Scheduled wakeups and the SessionStart hook require
host support; the hook also requires the host's trust. Grok Bot UI and the nested
Benny pack retain their separate integration prerequisites. Benny is dormant.

**Current status:** the source package, provenance and local fixtures have been
validated. Installed plugin discovery, host-specific behavior and live PR
publication by the combined skill have not yet been validated. See
[the validation record](VALIDATION.md) for what was checked and what remains.

## Where it comes from

The aim is a faithful Codex port. Upstream procedures, roles, panel sizes, review
requirements and helper behavior are preserved except for explicitly recorded
adaptations and approved changes.

| Source | Pinned version | Contribution |
| --- | --- | --- |
| [Original pstack](https://github.com/cursor/plugins/tree/ecc249f1e306fc64ddf83c7bed16cacf7c2239db/pstack) | `ecc249f` | The full pstack foundation |
| [pstack-claude](https://github.com/michael-denyer/pstack-claude/tree/c02fd4922b25ee005f42042463d741d236c2c35e/plugins/pstack) | `c02fd49` | Updates to shared files, retaining original-only material |
| [HumanLayer skills](https://github.com/humanlayer/skills/tree/ca7c8088db69e315a8b2deea43820270457f8f3c) | `ca7c808` | The approved show-me and visual-pr contribution |

For the exact changes, see [ADAPTATIONS.md](ADAPTATIONS.md),
[the decision record](NATIVE-PORT-DECISIONS.md), and
[the combined PR source notice](src/pstack-codex/skills/make-pr-easy-to-review/references/source-notice.md).
The [source lock](sources.lock.json) and [reconstruction patch](patches/codex-compatibility.patch)
account for every package file. Hstack is not an input.

<details>
<summary>For contributors: validation and reconstruction</summary>

The 254-file package contains 109 byte-identical imports, 134 declared
adaptations and 11 generated files. Validation reverses the declared edits back
to the pinned source, then checks package contents, permissions and links.

Use Python with PyYAML, Bun, Node.js, Git, jq and rg. Put Bun, Node and rg on PATH
because helper tests launch subprocesses.

```sh
python3 -m pip install -r requirements-dev.txt
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
`work/repo-comparison/humanlayer-skills-ca7c808`, then run:

```sh
python3 tools/restore_baseline.py --output work/reconstructed-native-pstack-codex
```

The destination must not exist. Reconstruction verifies the pinned Git objects,
applies the recorded patch and validates the result without changing the source.

[AGENTS.md](AGENTS.md) requires a concrete proposal, rationale and approval for
changes beyond the faithful baseline. Unapproved proposals stay in
[PROPOSALS.md](PROPOSALS.md). The public history begins with the approved 0.4.0
snapshot; earlier local experiments are not part of this repository.

</details>

## License and attribution

MIT. See [LICENSE](LICENSE), the bundled
[upstream notice](src/pstack-codex/NOTICE-pstack-claude.md),
[skills notice](src/pstack-codex/NOTICE-skills.md), and
[HumanLayer license](src/pstack-codex/THIRD_PARTY_LICENSES/HumanLayer.txt).
This is an independent Codex adaptation, not an official Cursor, Anthropic,
HumanLayer or OpenAI distribution.
