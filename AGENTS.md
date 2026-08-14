# AGENTS.md

This repository is research infrastructure. Agents must preserve auditability and must not optimise away provenance.

## Non-negotiable rules

1. Never discard source material that has already been ingested.
2. Preserve canonical source URLs and retrieval timestamps.
3. Keep `observed_at`, `published_at` and `effective_at` separate.
4. Never present LLM inference as authoritative law, regulation or government policy.
5. Label derived fields with method, model/version where relevant, confidence and evidence.
6. Historical observations are append-only. Corrections create new records or explicit supersession links.
7. Prefer official APIs and canonical public sources over scraping or secondary reporting.
8. A document is evidence. An event is a change. A flow is an ordered/related set of events.
9. Do not silently create causal relationships. Machine-suggested relationships must be distinguishable from confirmed relationships.
10. Deterministic extraction and parsing should be preferred where possible. Use probabilistic models only where they add clear value.
11. All schemas and ontology changes require documentation and tests.
12. Research reproducibility takes precedence over UI convenience.

## Source confidence

Use the following conceptual hierarchy:

- `authoritative_state`: legislation, final regulator rules and canonical legal sources.
- `formal_process`: consultations, government responses, parliamentary stages, regulator policy statements.
- `political_signal`: speeches, debates, written statements and similar indicators.
- `derived_analysis`: PolicyFlow calculations, classifications, entity mappings and model output.

Never collapse these categories into one undifferentiated confidence score.

## Coding conventions

- Python 3.12+.
- Type annotations required for public functions.
- Keep collectors small and source-specific.
- Raw source retrieval must be separable from interpretation.
- Hash normalised bytes/text deterministically for change detection.
- Tests must not depend on live external services unless explicitly marked as integration tests.
- Fixtures should use small captured samples and document their provenance.

## AI usage

LLMs may assist with classification, relationship suggestion, summarisation and change interpretation. They must not be the sole mechanism for determining whether an authoritative source changed.

Every AI-derived output should be capable of carrying:

- `derived_by`
- `model`
- `model_version`
- `prompt_version`
- `confidence`
- `evidence_refs`
- `created_at`

## Project thesis

PolicyFlow is not an AI search layer over regulatory documents. Its purpose is to create an auditable, temporal representation of **how policy moves** and, later, how those movements propagate into economic and market exposure.
