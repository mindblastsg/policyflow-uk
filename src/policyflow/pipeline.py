from __future__ import annotations

from hashlib import sha256

from policyflow.change_detection import classify_change
from policyflow.models import (
    AssertionKind,
    ChangeStatus,
    CollectedItem,
    Observation,
    PolicyEvent,
    SourceClass,
)


def _stable_id(prefix: str, value: str) -> str:
    return f"{prefix}_{sha256(value.encode('utf-8')).hexdigest()[:24]}"


def observe_items(
    items: list[CollectedItem],
    previous_hashes: dict[str, str],
) -> tuple[list[Observation], dict[str, str]]:
    observations: list[Observation] = []
    next_state = dict(previous_hashes)

    for item in items:
        status = classify_change(previous_hashes.get(item.document_id), item.content_hash)
        observation_key = (
            f"{item.document_id}|{item.observed_at.isoformat()}|{item.content_hash}"
        )
        observations.append(
            Observation(
                observation_id=_stable_id("obs", observation_key),
                source_id=item.source_id,
                document_id=item.document_id,
                observed_at=item.observed_at,
                canonical_url=item.canonical_url,
                content_hash=item.content_hash,
                change_status=status,
            )
        )
        next_state[item.document_id] = item.content_hash

    return observations, next_state


def event_from_observation(
    item: CollectedItem,
    observation: Observation,
) -> PolicyEvent | None:
    """Create only source-level detection events.

    Semantic events such as `consultation_published` require a later,
    separately provenance-tracked classification stage.
    """

    if observation.change_status is ChangeStatus.UNCHANGED:
        return None

    event_type = (
        "source_item_detected"
        if observation.change_status is ChangeStatus.NEW
        else "source_item_changed"
    )
    event_key = f"{observation.observation_id}|{event_type}"

    return PolicyEvent(
        event_id=_stable_id("evt", event_key),
        event_type=event_type,
        observed_at=observation.observed_at,
        source_class=SourceClass.FORMAL_PROCESS,
        evidence_refs=[observation.observation_id],
        assertion_kind=AssertionKind.SOURCE,
        title=item.title,
        notes=(
            "Source-level detection only; no semantic policy classification has been inferred."
        ),
    )
