from __future__ import annotations

import argparse
import json
from pathlib import Path

from policyflow.collectors.fca import collect_publications
from policyflow.models import ChangeStatus
from policyflow.pipeline import event_from_observation, observe_items
from policyflow.state import load_hash_state, save_hash_state


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="policyflow")
    subparsers = parser.add_subparsers(dest="command", required=True)

    ingest = subparsers.add_parser("ingest", help="Run a source collector")
    ingest_subparsers = ingest.add_subparsers(dest="source", required=True)

    fca = ingest_subparsers.add_parser("fca", help="Collect FCA publication index items")
    fca.add_argument(
        "--state",
        type=Path,
        default=Path(".policyflow/state/fca-publications.json"),
        help="Path to local hash state",
    )
    fca.add_argument("--limit", type=int, default=None)
    fca.add_argument(
        "--include-unchanged",
        action="store_true",
        help="Emit unchanged observations as well as changes",
    )
    return parser


def _emit(kind: str, payload: dict[str, object]) -> None:
    print(json.dumps({"record_type": kind, **payload}, sort_keys=True))


def _run_fca(args: argparse.Namespace) -> int:
    previous = load_hash_state(args.state)
    items = collect_publications(limit=args.limit)
    observations, next_state = observe_items(items, previous)
    by_document = {item.document_id: item for item in items}

    changes = 0
    for observation in observations:
        if args.include_unchanged or observation.change_status is not ChangeStatus.UNCHANGED:
            _emit("observation", observation.model_dump(mode="json"))

        event = event_from_observation(by_document[observation.document_id], observation)
        if event is not None:
            changes += 1
            _emit("event", event.model_dump(mode="json"))

    save_hash_state(args.state, next_state)
    print(
        json.dumps(
            {
                "record_type": "run_summary",
                "source": "fca_publications",
                "items_seen": len(items),
                "changes_emitted": changes,
                "state_path": str(args.state),
            },
            sort_keys=True,
        )
    )
    return 0


def main() -> int:
    parser = _build_parser()
    args = parser.parse_args()

    if args.command == "ingest" and args.source == "fca":
        return _run_fca(args)

    parser.error("Unsupported command")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
