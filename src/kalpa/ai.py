"""Append a row to docs/ai-log.md: every use of a coding or chat assistant, one line each."""
from __future__ import annotations

from datetime import date

from kalpa.logs import DOCS, _append_row


def log(asked: str, did: str, who="", tool="", n=""):
    _append_row(DOCS / "ai-log.md", "What we asked", [n, date.today().isoformat(), who, tool, asked, did])
