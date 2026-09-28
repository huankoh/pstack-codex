<EXTREMELY_IMPORTANT>
You have pstack.

Invoke the `pstack-codex:poteto-mode` skill and follow its instructions when a task meets any of these:

- it touches more than one file, or changes a signature other files call
- it involves a design or architecture choice
- it is a bug whose cause is not yet known, or a performance issue

It routes to the right pstack skill from there. For smaller tasks, such as a contained change to one file with an obvious test, a question, or a one-line edit, work directly and verify on the real artifact.

When the intent is already specific, enter that skill directly: `pstack-codex:tdd`, `pstack-codex:architect`, `pstack-codex:how`, `pstack-codex:why`, `pstack-codex:arena`, `pstack-codex:interrogate`.

User instructions (AGENTS.md, direct requests) take precedence. Other session-start mandates, such as superpowers, still apply. Their skill checks run as before, and when a task meets the criteria above they route implementation through poteto-mode.
</EXTREMELY_IMPORTANT>
