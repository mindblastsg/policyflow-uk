from __future__ import annotations

from datetime import datetime
from enum import StrEnum

from pydantic import BaseModel, ConfigDict, Field


class ChangeStatus(StrEnum):
    NEW = "NEW"
    CHANGED = "CHANGED"
    UNCHANGED = "UNCHANGED"


class SourceClass(StrEnum):
    AUTHORITATIVE_STATE = "authoritative_state"
    FORMAL_PROCESS = "formal_process"
    POLITICAL_SIGNAL = "political_signal"
    IMPACT_EVIDENCE = "impact_evidence"


class AssertionKind(StrEnum):
    SOURCE = "SOURCE"
    DERIVED = "DERIVED"
    MACHINE_EXTRACTED = "MACHINE_EXTRACTED"
    RESEARCHER = "RESEARCHER"
    HYPOTHESIS = "HYPOTHESIS"


class CollectedItem(BaseModel):
    """A minimally interpreted item emitted by a source collector."""

    model_config = ConfigDict(extra="forbid")

    source_id: str
    document_id: str
    title: str
    canonical_url: str
    observed_at: datetime
    raw_text: str
    content_hash: str


class Observation(BaseModel):
    """A point-in-time observation of a continuing source/document identity."""

    model_config = ConfigDict(extra="forbid")

    observation_id: str
    source_id: str
    document_id: str
    observed_at: datetime
    canonical_url: str
    content_hash: str
    change_status: ChangeStatus


class PolicyEvent(BaseModel):
    """Canonical event representation used by PolicyFlow v0.1."""

    model_config = ConfigDict(extra="forbid")

    event_id: str
    event_type: str
    observed_at: datetime
    source_class: SourceClass
    evidence_refs: list[str] = Field(min_length=1)
    assertion_kind: AssertionKind

    title: str | None = None
    actor_entity_id: str | None = None
    flow_id: str | None = None
    previous_state: str | None = None
    new_state: str | None = None
    published_at: datetime | None = None
    event_at: datetime | None = None
    effective_at: datetime | None = None
    topic_ids: list[str] = Field(default_factory=list)
    affected_entity_ids: list[str] = Field(default_factory=list)
    extraction_confidence: float | None = Field(default=None, ge=0, le=1)
    derived_by: str | None = None
    notes: str | None = None
