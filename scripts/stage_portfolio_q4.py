"""Stage a Q4-only subset of a portfolio company folder for cheap demo ingest.

For each input portco folder, symlinks into a staging directory:
  - every Q4_* file (annual FY rollup — one per year, what the resolver needs)
  - the most recent quarter file overall (so latest financials/thesis aren't
    stale if the year is mid-flight, e.g. Q1 2026)
  - any non-quarterly files untouched (e.g. Deal Materials/IC_Memo_Entry_*)

The PDF/DOCX twin pairs are kept; existing triage dedups them.

Usage:
  uv run python scripts/stage_portfolio_q4.py \\
      "/Users/gdeshayes/Downloads/02. Portfolio Companies/02. Vanguard Auto" \\
      data/_staged/vanguard_auto

Then:
  uv run python scripts/ingest_folder.py data/_staged/vanguard_auto --kind portfolio
"""

from __future__ import annotations

import argparse
import re
import shutil
import sys
from pathlib import Path

_QUARTER_RE = re.compile(r"Q([1-4])[_-](\d{4})", re.IGNORECASE)


def _quarter_key(path: Path) -> tuple[int, int] | None:
    m = _QUARTER_RE.search(path.name)
    if not m:
        return None
    q, y = int(m.group(1)), int(m.group(2))
    return (y, q)


def stage(src: Path, dst: Path) -> None:
    if not src.is_dir():
        sys.exit(f"source not a directory: {src}")
    if dst.exists():
        sys.exit(f"destination already exists, refusing to overwrite: {dst}")

    all_files = [p for p in src.rglob("*") if p.is_file()]
    quarter_files = [(p, _quarter_key(p)) for p in all_files]

    # latest quarter across the whole portco (any subfolder)
    dated = [(p, k) for p, k in quarter_files if k is not None]
    latest_key = max((k for _, k in dated), default=None)

    kept: list[Path] = []
    for p, k in quarter_files:
        if k is None:
            kept.append(p)  # non-quarterly (e.g. IC_Memo_Entry_*)
            continue
        _, q = k
        if q == 4 or k == latest_key:
            kept.append(p)

    dst.mkdir(parents=True)
    for p in kept:
        rel = p.relative_to(src)
        out = dst / rel
        out.parent.mkdir(parents=True, exist_ok=True)
        # copy rather than symlink — keeps sha1/path stable if originals move
        shutil.copy2(p, out)

    dropped = len(all_files) - len(kept)
    print(f"staged {len(kept)} files (dropped {dropped} intermediate quarters)")
    print(f"  latest quarter retained: Q{latest_key[1]} {latest_key[0]}" if latest_key else "")
    print(f"  → {dst}")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("src", type=Path, help="portco folder to subset")
    ap.add_argument("dst", type=Path, help="staging destination (must not exist)")
    args = ap.parse_args()
    stage(args.src.expanduser().resolve(), args.dst.expanduser().resolve())


if __name__ == "__main__":
    main()
