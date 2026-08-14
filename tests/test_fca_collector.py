from datetime import UTC, datetime
from pathlib import Path

from policyflow.collectors.fca import parse_publication_index


FIXTURE = Path(__file__).parent / "fixtures" / "fca_publications.html"


def test_parse_publication_index_extracts_unique_publication_links() -> None:
    html = FIXTURE.read_text(encoding="utf-8")
    observed_at = datetime(2026, 8, 14, 12, 0, tzinfo=UTC)

    items = parse_publication_index(html, observed_at=observed_at)

    assert len(items) == 2
    assert {item.title for item in items} == {
        "Example consultation paper",
        "Example policy statement",
    }
    assert all(item.source_id == "fca_publications" for item in items)
    assert all(item.observed_at == observed_at for item in items)
    assert all(item.content_hash for item in items)
