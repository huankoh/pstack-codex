# Combined PR workflow provenance

User-approved extension, 2026-09-28: combine show-me, show-me-your-work and visual-pr into the PR skill for visual context, outlines and an evidence trail.

- **pstack / pstack-claude:** the existing make-pr-easy-to-review skill, Opening a PR body conventions, and show-me-your-work decision logging, transcript audit and independent review remain the foundation. Their pinned versions are recorded in the repository's source lock.
- **HumanLayer show-me:** visual forms and compact presentation adapted in [Visual outlines](visual-outline.md).
- **HumanLayer visual-pr:** full-diff context gathering, structural change outlines, local description files, publishing and readback adapted into the combined workflow. Its fixed description template and HumanLayer cloud links are replaced by pstack's body sections and actual forge/local artifact links. Its explicit-only invocation policy is not imported; the existing PR skill remains selectable when relevant.

HumanLayer source: [humanlayer/skills at ca7c8088db69e315a8b2deea43820270457f8f3c](https://github.com/humanlayer/skills/tree/ca7c8088db69e315a8b2deea43820270457f8f3c), specifically `plugins/show-me/skills/show-me/SKILL.md` and `plugins/visual-pr/skills/visual-pr/SKILL.md`. Copyright (c) 2026 HumanLayer. The [MIT license](../../../THIRD_PARTY_LICENSES/HumanLayer.txt) is included in full.

Only this combined PR extension is approved. The standalone pstack trail skill remains available for non-PR work. No other HumanLayer skill is imported.
