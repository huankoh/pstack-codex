#!/usr/bin/env python3
"""Report pinned source fidelity and fail on undeclared package drift."""
import argparse
import json
from pathlib import Path

from validate import ROOT, SOURCE, fidelity_report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=SOURCE)
    parser.add_argument("--lock", type=Path, default=ROOT / "sources.lock.json")
    args = parser.parse_args()
    result = fidelity_report(args.source, args.lock)
    print(json.dumps(result, indent=2))
    return bool(result["errors"])


if __name__ == "__main__":
    raise SystemExit(main())
