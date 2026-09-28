#!/usr/bin/env python3
"""Reconstruct the pinned package in a new directory, then verify its fidelity."""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess

from validate import ROOT, validate

CHECKOUTS = {
    "pstack": ROOT / "work/repo-comparison/cursor-plugins",
    "claude": ROOT / "work/repo-comparison/pstack-claude",
    "humanlayer": ROOT / "work/repo-comparison/humanlayer-skills-ca7c808",
}


def restore(destination):
    destination = Path(destination).absolute()
    if destination.exists():
        raise ValueError(f"output already exists: {destination}")
    lock = json.loads((ROOT / "sources.lock.json").read_text())
    imported = []
    for name, entry in lock["files"].items():
        source = entry["source"]
        revision = lock["sources"][source]["commit"]
        data = subprocess.check_output([
            "git", "-C", str(CHECKOUTS[source]),
            "show", f"{revision}:{entry['path']}",
        ])
        if hashlib.sha256(data).hexdigest() != entry["sha256"]:
            raise ValueError(f"pinned source hash mismatch: {name}")
        imported.append((name, entry, data))
    destination.mkdir(parents=True)
    for name, entry, data in imported:
        path = destination / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)
        path.chmod(int(entry["mode"], 8) & 0o777)
    # Absolute destination is intentional; all patch paths are plugin-relative.
    subprocess.run([
        "git", "apply", "--unsafe-paths", "--directory", str(destination),
        str(ROOT / "patches/codex-compatibility.patch"),
    ], cwd="/", check=True)
    errors = validate(source=destination)
    if errors:
        raise ValueError("reconstructed package failed validation:\n" + "\n".join(errors))
    return destination


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True,
                        help="new, nonexistent directory for reconstructed plugin")
    args = parser.parse_args()
    print(f"Reconstructed and validated {restore(args.output)}")
