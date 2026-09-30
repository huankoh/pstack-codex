#!/usr/bin/env python3
"""Validate package compatibility and fidelity to the pinned upstream union."""
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import stat
import sys
from urllib.parse import unquote

import yaml

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "src/pstack-codex"
EXCLUDED = {"node_modules", "__pycache__", ".DS_Store"}
HASH = re.compile(r"[0-9a-f]{64}\Z")
FRONTMATTER = re.compile(r"\A---\n(.*?)\n---\n", re.S)
PLAYBOOK_PREFIX = "skills/poteto-mode/playbooks/"
NATIVE_APPROVALS = {"native-runtime", "models", "luna-retrieval", "transcripts", "archive", "availability", "messages", "audit-corrections", "original-merge-authority", "combined-pr", "publication", "sol-6.1"}


def digest(data):
    return hashlib.sha256(data).hexdigest()


def safe_relative(name):
    path = PurePosixPath(name)
    return bool(name) and not path.is_absolute() and ".." not in path.parts and path.as_posix() == name


def reverse_native_edits(data, edits):
    """Reverse exact reviewed edits, leaving every other source byte protected.

    Offsets refer to Unicode characters in the pinned source, not edited output.
    Each edit has its original text, replacement text, rationale and approval ID.
    Updating an output hash alone cannot authorize an additional workflow edit.
    """
    text = data.decode("utf-8")
    if not isinstance(edits, list) or not edits:
        raise ValueError("native edits must be a nonempty list")
    parts, native_cursor, original_end, delta = [], 0, 0, 0
    for edit in edits:
        if not isinstance(edit, dict):
            raise ValueError("native edit must be an object")
        start, before, after = edit.get("start"), edit.get("before"), edit.get("after")
        if type(start) is not int or start < original_end or not isinstance(before, str) or not isinstance(after, str) or before == after:
            raise ValueError("invalid or overlapping native edit")
        if edit.get("approval") not in NATIVE_APPROVALS or not isinstance(edit.get("reason"), str) or not edit["reason"].strip():
            raise ValueError("native edit needs a recognized approval and rationale")
        native_start = start + delta
        if native_start < native_cursor or native_start > len(text) or not text.startswith(after, native_start):
            raise ValueError("native edit replacement differs from declaration")
        parts.extend((text[native_cursor:native_start], before))
        native_cursor = native_start + len(after)
        original_end = start + len(before)
        delta += len(after) - len(before)
    parts.append(text[native_cursor:])
    return "".join(parts).encode("utf-8")


def package_inventory(source):
    """Use the same dependency exclusions as the distributable builder."""
    files, errors = {}, []
    for path in sorted(source.rglob("*")):
        name = path.relative_to(source).as_posix()
        if any(part in EXCLUDED for part in path.relative_to(source).parts):
            continue
        if path.is_symlink():
            errors.append(f"package symlink is not supported: {name}")
        elif path.is_file():
            files[name] = path
    return files, errors


def fidelity_report(source=SOURCE, lock_path=ROOT / "sources.lock.json"):
    """Check bytes, modes, inventory, and independently pinned skill bodies.

    A compatibility hash permits only recorded bytes. Schema 2 retains the
    adapter-preamble-only body contract. Schema 3 also permits individually
    declared native edits, which must reverse exactly to the pinned source.
    Neither a new output hash nor a rationale alone authorizes workflow drift.
    """
    source, lock_path = Path(source), Path(lock_path)
    result = {key: [] for key in ("unchanged", "adapted", "different", "missing", "generated", "unexpected", "errors")}
    errors = result["errors"]
    try:
        lock = json.loads(lock_path.read_text())
    except (OSError, ValueError) as error:
        errors.append(f"cannot read source lock: {error}")
        return result
    if lock.get("schema") not in {2, 3}:
        errors.append("source lock must use fidelity schema 2 or 3")
    imported = lock.get("files", {})
    compatibility = lock.get("compatibility", {})
    generated = lock.get("generated_files", {})
    translations = lock.get("native_translations", {})
    if translations and lock.get("schema") != 3:
        errors.append("native translations require fidelity schema 3")
    inventory, inventory_errors = package_inventory(source)
    errors.extend(inventory_errors)
    for name in sorted(set(compatibility) - set(imported)):
        errors.append(f"compatibility entry has no imported source: {name}")
    for name in sorted(set(translations) - (set(imported) & set(compatibility))):
        errors.append(f"native translation needs imported source and compatibility entry: {name}")
    for name in sorted(set(generated) & set(imported)):
        errors.append(f"file is both generated and imported: {name}")
    declared = set(imported) | set(generated)
    for name in sorted(set(inventory) - declared):
        result["unexpected"].append(name)
        errors.append(f"undeclared package file: {name}")
    for name, entry in sorted(imported.items()):
        start_errors = len(errors)
        if not safe_relative(name):
            errors.append(f"unsafe imported path: {name}")
            continue
        baseline_hash = entry.get("sha256", "")
        if entry.get("source") not in lock.get("sources", {}) or not HASH.fullmatch(baseline_hash):
            errors.append(f"invalid provenance: {name}")
        mode = entry.get("mode")
        if mode not in {"100644", "100755"}:
            errors.append(f"invalid source mode: {name}")
        adaptation = compatibility.get(name)
        expected_hash = baseline_hash
        if adaptation is not None:
            expected_hash = adaptation.get("sha256", "")
            if not adaptation.get("reason", "").strip() or not HASH.fullmatch(expected_hash):
                errors.append(f"invalid compatibility declaration: {name}")
        path = inventory.get(name)
        if path is None:
            result["missing"].append(name)
            errors.append(f"missing imported source: {name}")
            continue
        data = path.read_bytes()
        actual_hash = digest(data)
        baseline_data = None
        if name in translations:
            try:
                baseline_data = reverse_native_edits(data, translations[name])
                if digest(baseline_data) != baseline_hash:
                    errors.append(f"native edits do not reconstruct pinned upstream: {name}")
            except (UnicodeError, ValueError) as error:
                errors.append(f"{name}: {error}")
        if actual_hash != expected_hash:
            errors.append(f"{'compatibility' if adaptation is not None else 'upstream'} hash mismatch: {name}")
        if mode in {"100644", "100755"} and stat.S_IMODE(path.stat().st_mode) != (int(mode, 8) & 0o777):
            errors.append(f"source mode mismatch: {name}")
        if name.startswith(PLAYBOOK_PREFIX) and actual_hash != baseline_hash and name not in translations:
            errors.append(f"playbook differs from pinned upstream: {name}")
        if name.endswith("/SKILL.md"):
            body_hash = entry.get("skill_body_sha256", "")
            if not HASH.fullmatch(body_hash):
                errors.append(f"missing or invalid baseline skill-body hash: {name}")
            try:
                text = (baseline_data if baseline_data is not None else data).decode("utf-8")
                front = FRONTMATTER.match(text)
                if front is None:
                    raise ValueError("missing frontmatter")
                body = text[front.end():]
                preamble = adaptation.get("body_preamble") if adaptation and baseline_data is None else None
                if preamble is not None:
                    if not preamble or body.count(preamble) != 1:
                        raise ValueError("declared adapter preamble must occur exactly once")
                    body = body.replace(preamble, "", 1)
                if digest(body.strip().encode()) != body_hash:
                    errors.append(f"skill body differs from pinned upstream: {name}")
            except (UnicodeError, ValueError) as error:
                errors.append(f"{name}: {error}")
        if len(errors) > start_errors:
            result["different"].append(name)
        elif actual_hash == baseline_hash:
            result["unchanged"].append(name)
        else:
            result["adapted"].append(name)
    for name, entry in sorted(generated.items()):
        if not safe_relative(name):
            errors.append(f"unsafe generated path: {name}")
            continue
        expected_hash = entry.get("sha256", "")
        if not entry.get("reason", "").strip() or not HASH.fullmatch(expected_hash):
            errors.append(f"invalid generated-file declaration: {name}")
        path = inventory.get(name)
        if path is None:
            result["missing"].append(name)
            errors.append(f"missing generated file: {name}")
            continue
        if digest(path.read_bytes()) != expected_hash:
            result["different"].append(name)
            errors.append(f"generated-file hash mismatch: {name}")
        else:
            result["generated"].append(name)
        mode = entry.get("mode", "100644")
        if mode not in {"100644", "100755"} or stat.S_IMODE(path.stat().st_mode) != (int(mode, 8) & 0o777):
            errors.append(f"generated-file mode mismatch: {name}")
    top_level = [name for name in inventory if re.fullmatch(r"skills/[^/]+/SKILL\.md", name)]
    all_skills = [name for name in inventory if name.endswith("/SKILL.md")]
    counts = {"top_level_skills": len(top_level),
              "additional_nested_skills": len(all_skills) - len(top_level),
              "playbooks": sum(name.startswith(PLAYBOOK_PREFIX) and name.endswith(".md") for name in inventory)}
    result["counts"] = counts
    for kind, actual in counts.items():
        expected = lock.get("expected", {}).get(kind)
        if not isinstance(expected, int) or expected != actual:
            errors.append(f"{kind} count mismatch: expected {expected}, found {actual}")
    return result


def validate(source=SOURCE, lock_path=ROOT / "sources.lock.json"):
    source = Path(source)
    errors = list(fidelity_report(source, lock_path)["errors"])
    inventory, _ = package_inventory(source)
    try:
        manifest = json.loads((source / ".codex-plugin/plugin.json").read_text())
        if manifest.get("name") != "pstack-codex" or manifest.get("skills") != "./skills/":
            errors.append("manifest identity or skills path mismatch")
        for key in ("skills", "hooks"):
            target = manifest.get(key)
            if isinstance(target, str) and not (source / target).exists():
                errors.append(f"manifest {key} target missing: {target}")
    except (OSError, ValueError) as error:
        errors.append(f"invalid plugin manifest: {error}")
    for name, path in inventory.items():
        if name.endswith("/SKILL.md"):
            try:
                text = path.read_text()
                front = FRONTMATTER.match(text)
                if front is None:
                    raise ValueError("missing frontmatter")
                fields = yaml.safe_load(front[1])
                if fields.get("name") != path.parent.name:
                    raise ValueError("skill name does not match directory")
                if not isinstance(fields.get("description"), str) or not fields["description"].strip():
                    raise ValueError("missing skill description")
                if set(fields) - {"name", "description", "license", "compatibility", "metadata", "allowed-tools"}:
                    raise ValueError("unsupported platform frontmatter")
            except (ValueError, AttributeError, UnicodeError, yaml.YAMLError) as error:
                errors.append(f"{name}: {error}")
        if not name.endswith(".md"):
            continue
        # Illustrative code blocks do not declare package dependencies.
        prose = re.sub(r"```.*?```", "", path.read_text(), flags=re.S)
        for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", prose):
            target = re.sub(r'\s+[\"\'].*[\"\']$', "", target).split("#", 1)[0]
            if not target or re.match(r"[a-z][a-z0-9+.-]*:", target, re.I) or any(c in target for c in "<>{}"):
                continue
            if not (path.parent / unquote(target)).exists():
                errors.append(f"broken reference: {name} -> {target}")
    return errors


if __name__ == "__main__":
    errors = validate()
    if errors:
        print("\n".join(errors), file=sys.stderr)
        raise SystemExit(1)
    report = fidelity_report()
    print(f"Validated {report['counts']['top_level_skills']} skills, {report['counts']['additional_nested_skills']} nested skills, "
          f"{report['counts']['playbooks']} faithful playbooks; {len(report['unchanged'])} unchanged and "
          f"{len(report['adapted'])} declared compatibility files, {len(report['generated'])} generated files; "
          "metadata, references, and exact inventory pass.")
