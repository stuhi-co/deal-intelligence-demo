"""File source abstractions.

LocalFolderSource walks a local directory. Production swaps this for BoxSource
(OAuth JWT + Events API polling) — same Protocol, no other module changes.
"""

from __future__ import annotations

import hashlib
from datetime import datetime
from pathlib import Path
from typing import Iterator, Protocol

from .schemas import FileRef


_SYSTEM_PATTERNS = (".~lock", ".DS_Store", "Thumbs.db", "~$")


def _is_system_file(name: str) -> bool:
    return any(name.startswith(p) or name == p for p in _SYSTEM_PATTERNS)


def _sha1_of(path: Path, chunk_size: int = 1 << 20) -> str:
    h = hashlib.sha1()
    with path.open("rb") as f:
        while chunk := f.read(chunk_size):
            h.update(chunk)
    return h.hexdigest()


class Source(Protocol):
    """A source of files for ingestion. iter_files yields FileRefs."""

    root: Path

    def iter_files(self) -> Iterator[FileRef]: ...


class LocalFolderSource:
    """v1 source. Walks a local folder, skips system/lock files at the iterator."""

    def __init__(self, root: Path):
        self.root = Path(root).resolve()
        if not self.root.is_dir():
            raise ValueError(f"Source root is not a directory: {self.root}")

    def iter_files(self) -> Iterator[FileRef]:
        for abs_path in sorted(self.root.rglob("*")):
            if not abs_path.is_file():
                continue
            if _is_system_file(abs_path.name):
                continue
            stat = abs_path.stat()
            yield FileRef(
                path=str(abs_path.relative_to(self.root)),
                abs_path=abs_path,
                size_bytes=stat.st_size,
                mtime=datetime.fromtimestamp(stat.st_mtime),
                sha1=_sha1_of(abs_path),
            )


# Production-only stub. Documented here so the swap surface is visible.
#
# class BoxSource:
#     """OAuth JWT server-to-server auth. Recursive folder traversal via Box SDK.
#     ACL capture from box_collaborators. Events API polling for incremental sync.
#     Returns FileRefs with abs_path replaced by a (box_file_id, content_loader) tuple.
#     """
#     ...
