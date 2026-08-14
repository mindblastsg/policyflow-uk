from __future__ import annotations

from datetime import UTC, datetime
from hashlib import sha256
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

from policyflow.change_detection import content_hash
from policyflow.models import CollectedItem


FCA_PUBLICATIONS_URL = "https://www.fca.org.uk/publications"
USER_AGENT = "PolicyFlow-UK/0.1 (+https://github.com/mindblastsg/policyflow-uk)"


def _document_id(url: str) -> str:
    digest = sha256(url.encode("utf-8")).hexdigest()[:20]
    return f"fca:{digest}"


def _looks_like_publication_detail(href: str) -> bool:
    parts = [part for part in href.strip("/").split("/") if part]
    return len(parts) >= 3 and parts[0] == "publications"


def parse_publication_index(
    html: str,
    *,
    observed_at: datetime | None = None,
) -> list[CollectedItem]:
    """Parse publication-detail links from a captured FCA publications page.

    This intentionally performs minimal interpretation. It identifies likely
    publication detail links and preserves their title/URL as the current
    observable representation of the item in the index.
    """

    observed_at = observed_at or datetime.now(UTC)
    soup = BeautifulSoup(html, "html.parser")
    by_url: dict[str, CollectedItem] = {}

    for anchor in soup.find_all("a", href=True):
        href = str(anchor.get("href", "")).split("#", 1)[0].strip()
        if not _looks_like_publication_detail(href):
            continue

        title = " ".join(anchor.stripped_strings).strip()
        if not title:
            continue

        canonical_url = urljoin(FCA_PUBLICATIONS_URL, href)
        raw_text = f"{title}\n{canonical_url}"
        item = CollectedItem(
            source_id="fca_publications",
            document_id=_document_id(canonical_url),
            title=title,
            canonical_url=canonical_url,
            observed_at=observed_at,
            raw_text=raw_text,
            content_hash=content_hash(raw_text),
        )

        existing = by_url.get(canonical_url)
        if existing is None or len(item.title) > len(existing.title):
            by_url[canonical_url] = item

    return sorted(by_url.values(), key=lambda item: item.canonical_url)


def collect_publications(
    *,
    limit: int | None = None,
    timeout_seconds: float = 20.0,
    session: requests.Session | None = None,
) -> list[CollectedItem]:
    client = session or requests.Session()
    response = client.get(
        FCA_PUBLICATIONS_URL,
        headers={"User-Agent": USER_AGENT},
        timeout=timeout_seconds,
    )
    response.raise_for_status()

    items = parse_publication_index(response.text)
    return items if limit is None else items[:limit]
