# Set up pstack-codex

This page starts from the source package, then configures the model roles and runs a first task. Plugin installation and hook support depend on the Codex host.

## Install the plugin

This checkout is source, not an active installation. To try it, ask Codex to read [`skills/poteto-mode/SKILL.md`](../../skills/poteto-mode/SKILL.md) from this checkout and apply it to your task. If you install it through a host-supported Codex plugin flow, verify that the skills are discoverable. The bundled session hook routes tasks only on a host that supports it and after the user trusts it. A skills-only installation does not activate the hook.

## Pick your models

Run:

```text
/setup-pstack
```

[`/setup-pstack`](../../skills/setup-pstack/SKILL.md) detects the models you have access to, asks for a reasoning budget, shows you each role (code delegates, judgment, the review panels), and asks what you want. Answer the questions. It writes `${CODEX_HOME:-$HOME/.codex}/pstack-models.md`. Codex loads the model rows and `default effort` through `${CODEX_HOME:-$HOME/.codex}/AGENTS.md`; the hook reads `session hook` from the sheet when hook support and trust are present.

You only override what you care about. A role with no line in the rule keeps the skill's default. To restore a default, delete that role's line. A rerun of `/setup-pstack` keeps any role whose model differs from the default. An older sheet may pin earlier defaults; review its role values before re-running setup.

You might be wondering what happens if you use Auto. Set a role to `inherit-parent` or `auto` and pstack omits the subagent `model` field, so the subagent inherits your parent chat model. Both values mean the same thing, and neither is a model slug. For a panel role the value is a list, and one subagent runs per entry, so the list length sets the panel size. Setup also configures `swarm workers`, the default model for every `/swarm` worker unless a race names a model for each arm. The defaults are Sol for ordinary work and conclusions, Astra for strongest roles, and Astra/Sol/Luna for existing explicit panels. Luna requests `max` effort for its retrieval role and panel assignments. If the host cannot run a requested model or effort, choose a replacement before that affected step continues.

## Create verification when needed

The selected [`setup-pstack`](../../skills/setup-pstack/SKILL.md) workflow configures models and the session hook; it does not offer to create a verification skill automatically. Invoke [`create-verification-skill`](../../skills/create-verification-skill/SKILL.md) separately when your project needs a repeatable live check. It writes a project skill under `.agents/skills/verify/` and proves its first feature path before handoff. [Verify and ship](./06-verify-and-ship.md#create-a-project-verification-skill) explains when to use it.

After setup, start a new chat to check that the model instructions load. Verify the hook separately on hosts that support it; enabling a sheet line alone does not establish that the hook ran.

## Run your first task

Pick something real but small, and describe it the way you'd describe it to a colleague:

```text
/poteto-mode add a --json flag to this command. text output stays byte-identical. verify both.
```

Watch the todo list. Its first items are the matched playbook's steps copied in, the Feature playbook for this prompt. If `/poteto-mode` skips a step, the step stays in the list with `skip: <reason>`, so you can see what it chose not to do.

`poteto-mode` stays active across turns after invocation until you opt out. A supported and trusted session hook can additionally route startup and resumed sessions; without it, invoke the skill explicitly or use a standing `AGENTS.md` instruction.

Next: [Route work through `/poteto-mode`](./02-poteto-mode.md).
