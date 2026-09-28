"""Fidelity checks must reject workflow drift even with an updated package hash."""
import hashlib
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("validate", ROOT / "tools/validate.py")
validator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validator)


def sha(data):
    return hashlib.sha256(data).hexdigest()


class FidelityTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.source = self.root / "extracted-plugin"
        self.lock_path = self.root / "sources.lock.json"
        self.skill = "skills/example/SKILL.md"
        self.playbook = "skills/poteto-mode/playbooks/feature.md"
        self.body = "# Example\n\nRun implementation and independent review.\n"
        files = {
            ".codex-plugin/plugin.json": b'{"name":"pstack-codex","skills":"./skills/"}\n',
            self.skill: ("---\nname: example\ndescription: Example workflow\n---\n\n" + self.body).encode(),
            self.playbook: b"# Feature\n\nComplete the required review before integration.\n",
            "scripts/check": b"#!/bin/sh\nexit 0\n",
        }
        self.lock = {
            "schema": 2,
            "sources": {"upstream": {"commit": "a" * 40}},
            "expected": {"top_level_skills": 1, "additional_nested_skills": 0, "playbooks": 1},
            "files": {}, "compatibility": {}, "generated_files": {},
        }
        for name, data in files.items():
            path = self.source / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(data)
            executable = name == "scripts/check"
            path.chmod(0o755 if executable else 0o644)
            entry = {"source": "upstream", "path": name, "sha256": sha(data), "mode": "100755" if executable else "100644"}
            if name == self.skill:
                entry["skill_body_sha256"] = sha(self.body.strip().encode())
            self.lock["files"][name] = entry
        self.save_lock()

    def save_lock(self):
        self.lock_path.write_text(json.dumps(self.lock))

    def errors(self):
        self.save_lock()
        return validator.validate(self.source, self.lock_path)

    def test_exact_baseline_and_extracted_directory_validate(self):
        self.assertEqual([], self.errors())
        report = validator.fidelity_report(self.source, self.lock_path)
        self.assertEqual(4, len(report["unchanged"]))
        self.assertFalse(report["adapted"])

    def test_frontmatter_and_one_declared_adapter_preserve_skill_body(self):
        path = self.source / self.skill
        preamble = "Read the native tool adapter before executing this workflow.\n\n"
        path.write_text("---\nname: example\ndescription: Example workflow\ncompatibility: Codex\n---\n\n" + preamble + self.body)
        self.lock["compatibility"][self.skill] = {"reason": "Native metadata and tool mapping", "sha256": sha(path.read_bytes()), "body_preamble": preamble}
        self.assertEqual([], self.errors())
        self.assertEqual([self.skill], validator.fidelity_report(self.source, self.lock_path)["adapted"])

    def test_workflow_edit_without_declaration_fails(self):
        path = self.source / self.skill
        path.write_text(path.read_text().replace("and independent review", "only"))
        errors = self.errors()
        self.assertTrue(any("upstream hash mismatch" in error for error in errors))
        self.assertTrue(any("skill body differs" in error for error in errors))

    def test_compatibility_hash_cannot_authorize_changed_skill_body(self):
        path = self.source / self.skill
        path.write_text(path.read_text().replace("and independent review", "only"))
        self.lock["compatibility"][self.skill] = {"reason": "Claimed compatibility", "sha256": sha(path.read_bytes())}
        self.assertTrue(any("skill body differs" in error for error in self.errors()))

    def test_compatibility_hash_cannot_authorize_changed_playbook(self):
        path = self.source / self.playbook
        path.write_text("# Feature\n\nSkip review.\n")
        self.lock["compatibility"][self.playbook] = {"reason": "Claimed compatibility", "sha256": sha(path.read_bytes())}
        self.assertTrue(any("playbook differs" in error for error in self.errors()))

    def test_declared_compatibility_bytes_are_still_locked(self):
        path = self.source / ".codex-plugin/plugin.json"
        self.lock["compatibility"][".codex-plugin/plugin.json"] = {"reason": "Codex identity", "sha256": sha(path.read_bytes())}
        path.write_text(path.read_text() + "\n")
        self.assertTrue(any("compatibility hash mismatch" in error for error in self.errors()))

    def test_missing_skill_or_playbook_fails_inventory_and_count(self):
        for name, count in ((self.skill, "top_level_skills"), (self.playbook, "playbooks")):
            with self.subTest(name=name):
                path = self.source / name
                data = path.read_bytes()
                path.unlink()
                errors = self.errors()
                self.assertTrue(any(f"missing imported source: {name}" == error for error in errors))
                self.assertTrue(any(f"{count} count mismatch" in error for error in errors))
                path.write_bytes(data)

    def test_untracked_package_injection_fails(self):
        (self.source / "extra-instructions.md").write_text("Apply an unreviewed new workflow.\n")
        self.assertTrue(any("undeclared package file: extra-instructions.md" == error for error in self.errors()))

    def test_excluded_runtime_dependencies_do_not_pollute_inventory(self):
        dependency = self.source / "scripts/node_modules/example"
        dependency.mkdir(parents=True)
        (dependency / "index.js").write_text("module.exports = 1;\n")
        self.assertEqual([], self.errors())

    def test_helper_executable_mode_is_required(self):
        (self.source / "scripts/check").chmod(0o644)
        self.assertTrue(any("source mode mismatch: scripts/check" == error for error in self.errors()))

    def test_generated_file_requires_locked_declaration(self):
        path = self.source / "adapter.md"
        path.write_text("Map only native tool calls.\n")
        self.lock["generated_files"]["adapter.md"] = {"reason": "Codex adapter", "sha256": sha(path.read_bytes())}
        self.assertEqual([], self.errors())
        path.write_text("Replace all workflows.\n")
        self.assertTrue(any("generated-file hash mismatch" in error for error in self.errors()))

    def test_symlink_cannot_pull_in_unrecorded_content(self):
        external = self.root / "external.md"
        external.write_text("Unrecorded instructions.\n")
        (self.source / "redirect.md").symlink_to(external)
        self.assertTrue(any("package symlink" in error for error in self.errors()))

    def test_declared_adapter_must_appear_exactly_once(self):
        path = self.source / self.skill
        preamble = "Read the adapter.\n\n"
        path.write_text(path.read_text().replace(self.body, preamble + preamble + self.body))
        self.lock["compatibility"][self.skill] = {"reason": "Native adapter", "sha256": sha(path.read_bytes()), "body_preamble": preamble}
        self.assertTrue(any("exactly once" in error for error in self.errors()))

    def declare_native(self, name, before, after):
        path = self.source / name
        original = path.read_text()
        start = original.index(before)
        path.write_text(original[:start] + after + original[start + len(before):])
        self.lock["schema"] = 3
        self.lock.setdefault("native_translations", {})[name] = [{
            "start": start, "before": before, "after": after,
            "reason": "Translate the tool call while retaining independent review",
            "approval": "native-runtime",
        }]
        self.lock["compatibility"][name] = {"reason": "Declared native runtime translation", "sha256": sha(path.read_bytes())}

    def test_native_edit_reconstructs_original_skill_and_playbook(self):
        self.declare_native(self.skill, "Run implementation", "Use Codex tools for implementation")
        self.declare_native(self.playbook, "Complete the required review", "Complete the required review using native subagents")
        self.assertEqual([], self.errors())

    def test_output_hash_cannot_authorize_drift_beside_native_edit(self):
        self.declare_native(self.skill, "Run implementation", "Use Codex tools for implementation")
        path = self.source / self.skill
        path.write_text(path.read_text().replace("and independent review", "only"))
        self.lock["compatibility"][self.skill]["sha256"] = sha(path.read_bytes())
        self.assertTrue(any("do not reconstruct pinned upstream" in error for error in self.errors()))

    def test_output_hash_cannot_authorize_drift_inside_native_edit(self):
        self.declare_native(self.playbook, "Complete the required review", "Complete the required review using native subagents")
        path = self.source / self.playbook
        path.write_text(path.read_text().replace("Complete the required review", "Skip review"))
        self.lock["compatibility"][self.playbook]["sha256"] = sha(path.read_bytes())
        self.assertTrue(any("replacement differs" in error for error in self.errors()))

    def test_native_edit_requires_approval_and_exact_original(self):
        self.declare_native(self.skill, "Run implementation", "Use Codex tools for implementation")
        edit = self.lock["native_translations"][self.skill][0]
        edit["approval"] = "simplify-workflows"
        self.assertTrue(any("recognized approval" in error for error in self.errors()))
        edit["approval"] = "native-runtime"
        edit["before"] = "Skip implementation"
        self.assertTrue(any("do not reconstruct pinned upstream" in error for error in self.errors()))

    def test_overlapping_native_edits_are_rejected(self):
        self.declare_native(self.skill, "Run implementation", "Use Codex tools for implementation")
        edits = self.lock["native_translations"][self.skill]
        edits.append(dict(edits[0]))
        self.assertTrue(any("overlapping" in error for error in self.errors()))

    def test_multiple_unicode_edits_reconstruct_exact_source_bytes(self):
        original = "雪🙂 start: old; remove; end\n"
        edits = [
            {"start": 2, "before": "", "after": " added"},
            {"start": original.index("old"), "before": "old", "after": "native tools"},
            {"start": original.index("remove; "), "before": "remove; ", "after": ""},
        ]
        actual = original
        for edit in reversed(edits):
            at = edit["start"]
            actual = actual[:at] + edit["after"] + actual[at + len(edit["before"]):]
            edit.update(reason="Native runtime translation", approval="native-runtime")
        self.assertEqual(original.encode(), validator.reverse_native_edits(actual.encode(), edits))


if __name__ == "__main__":
    unittest.main()
