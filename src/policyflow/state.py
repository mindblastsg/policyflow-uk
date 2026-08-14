from __future__ import annotations

import json
from pathlib import Path


def load_hash_state(path: Path) -> dict[str, str]:
    if not path.exists():
        return {}
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise ValueError("State file must contain a JSON object")
    return {str(key): str(value) for key, value in payload.items()}


def save_hash_state(path: Path, state: dict[str, str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(dict(sorted(state.items())), indent=2) + "\n",
        encoding="utf-8",
    )
