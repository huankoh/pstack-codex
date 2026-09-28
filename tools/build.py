#!/usr/bin/env python3
"""Build a deterministic plugin archive from the canonical source tree."""
import argparse
import hashlib
import json
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "src/pstack-codex"
EXCLUDED = {"node_modules", "__pycache__", ".DS_Store"}


def package_files(source=SOURCE):
    for path in sorted(source.rglob("*")):
        relative = path.relative_to(source)
        if any(part in EXCLUDED for part in relative.parts):
            continue
        if path.is_symlink():
            raise ValueError(f"package symlink is not supported: {relative}")
        if path.is_file():
            yield relative.as_posix(), path


def build(destination, source=SOURCE):
    destination = Path(destination)
    destination.parent.mkdir(parents=True, exist_ok=True)
    files = list(package_files(source))
    with ZipFile(destination, "w", compression=ZIP_DEFLATED, compresslevel=9) as archive:
        for name, path in files:
            info = ZipInfo(f"pstack-codex/{name}", (1980, 1, 1, 0, 0, 0))
            info.create_system = 3
            info.compress_type = ZIP_DEFLATED
            mode = 0o755 if path.stat().st_mode & 0o111 else 0o644
            info.external_attr = (0o100000 | mode) << 16
            archive.writestr(info, path.read_bytes(), compress_type=ZIP_DEFLATED, compresslevel=9)
    return {"path": str(destination.resolve()), "files": len(files),
            "sha256": hashlib.sha256(destination.read_bytes()).hexdigest()}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT / "dist/pstack-codex.zip")
    args = parser.parse_args()
    print(json.dumps(build(args.output), indent=2))
