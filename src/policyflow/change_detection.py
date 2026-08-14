from __future__ import annotations

import hashlib
import re

from .models import ChangeStatus


_WHITESPACE_RE = re.compile(r"[ \t]+")


def normalise_text(value: str) -> str:
    """Apply conservative, deterministic normalisation before hashing.

    Policy-relevant wording must be preserved. This function only normalises
    line endings, trims trailing whitespace and collapses horizontal runs of
    spaces/tabs.
    """

    value = value.replace("\r\n", "\n").replace("\r", "\n")
    lines = [_WHITESPACE_RE.sub(" ", line).rstrip() for line in value.split("\n")]
    return "\n".join(lines).strip()


def content_hash(value: str) -> str:
    normalised = normalise_text(value)
    return hashlib.sha256(normalised.encode("utf-8")).hexdigest()


def classify_change(previous_hash: str | None, current_hash: str) -> ChangeStatus:
    if previous_hash is None:
        return ChangeStatus.NEW
    if previous_hash == current_hash:
        return ChangeStatus.UNCHANGED
    return ChangeStatus.CHANGED
