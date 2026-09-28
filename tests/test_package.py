import importlib.util
from pathlib import Path
import tempfile
import unittest
from zipfile import ZipFile

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("build", ROOT / "tools/build.py")
build = importlib.util.module_from_spec(spec)
spec.loader.exec_module(build)


class PackageTests(unittest.TestCase):
    def test_reproducible_archive_preserves_helpers_and_excludes_dependencies(self):
        with tempfile.TemporaryDirectory() as directory:
            a, b = Path(directory) / "a.zip", Path(directory) / "b.zip"
            self.assertEqual(build.build(a)["sha256"], build.build(b)["sha256"])
            with ZipFile(a) as archive:
                names = archive.namelist()
                self.assertIn("pstack-codex/.codex-plugin/plugin.json", names)
                self.assertIn("pstack-codex/skills/poteto-mode/scripts/resume.mjs", names)
                wrapper = archive.getinfo("pstack-codex/skills/poteto-mode/scripts/watch-pr/watch-pr")
                self.assertTrue((wrapper.external_attr >> 16) & 0o111)
                self.assertFalse(any("node_modules" in name for name in names))

    def test_symlink_cannot_pull_files_from_outside_the_package(self):
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "source"
            source.mkdir()
            external = Path(directory) / "private.txt"
            external.write_text("not part of the package")
            (source / "leak").symlink_to(external)
            with self.assertRaisesRegex(ValueError, "symlink"):
                build.build(Path(directory) / "out.zip", source)


if __name__ == "__main__":
    unittest.main()
