from datetime import UTC, datetime

from policyflow.change_detection import content_hash
from policyflow.models import ChangeStatus, CollectedItem
from policyflow.pipeline import event_from_observation, observe_items


def _item(text: str) -> CollectedItem:
    return CollectedItem(
        source_id="fca_publications",
        document_id="fca:test",
        title="Example publication",
        canonical_url="https://www.fca.org.uk/publications/example",
        observed_at=datetime(2026, 8, 14, 12, 0, tzinfo=UTC),
        raw_text=text,
        content_hash=content_hash(text),
    )


def test_new_item_creates_source_level_event() -> None:
    item = _item("new text")
    observations, state = observe_items([item], {})

    observation = observations[0]
    assert observation.change_status is ChangeStatus.NEW
    assert state[item.document_id] == item.content_hash

    event = event_from_observation(item, observation)
    assert event is not None
    assert event.event_type == "source_item_detected"
    assert event.evidence_refs == [observation.observation_id]


def test_unchanged_item_does_not_create_event() -> None:
    item = _item("same text")
    observations, _ = observe_items([item], {item.document_id: item.content_hash})

    assert observations[0].change_status is ChangeStatus.UNCHANGED
    assert event_from_observation(item, observations[0]) is None


def test_changed_item_creates_changed_event() -> None:
    item = _item("new text")
    observations, _ = observe_items(
        [item],
        {item.document_id: content_hash("old text")},
    )

    assert observations[0].change_status is ChangeStatus.CHANGED
    event = event_from_observation(item, observations[0])
    assert event is not None
    assert event.event_type == "source_item_changed"
