# PolicyFlow UK

**PolicyFlow UK is an open, event-driven research infrastructure for tracking how UK financial policy, regulation and legislation move through institutions and into the economy.**

Most regulatory databases are archives: they organise documents, rules and legal text. PolicyFlow starts from a different premise:

> **The useful object is the flow of change.**

A policy moves through states such as announcement, consultation, legislation, secondary legislation, regulator rulemaking, implementation and enforcement. Each transition is an event. PolicyFlow captures those events, links them into auditable flows, preserves the source evidence and makes the resulting history machine-readable.

```text
policy signal
    ↓
consultation
    ↓
proposal / bill / draft SI
    ↓
legislation
    ↓
regulator consultation
    ↓
final rule
    ↓
implementation
    ↓
economic exposure
```

## What PolicyFlow is trying to answer

- What changed today?
- Which policy processes are moving, slowing, branching or being withdrawn?
- What changed relative to the previous proposal?
- What is legally in force versus merely proposed or politically signalled?
- Which institutions, sectors and entities are affected?
- What is the evidence chain behind a machine-generated conclusion?
- Can policy velocity, friction, materiality and regulatory exposure be measured reproducibly?

## Design principles

1. **Flows, not archives.** Documents are evidence for events, not the primary product object.
2. **Append-only history.** Historical observations are preserved rather than silently overwritten.
3. **Provenance first.** Every derived claim should be traceable to source material.
4. **Fact and inference are separate.** Machine interpretation is never presented as authoritative law.
5. **Temporal by default.** `observed_at`, `published_at` and `effective_at` are different concepts.
6. **Official sources first.** Prefer public APIs and canonical government/regulator sources over scraping.
7. **Research reproducibility.** Schemas, methodology and test fixtures should be inspectable and reusable.
8. **Open infrastructure.** The core data model and collection framework are intended to be useful beyond one interface.

## Initial scope

The first release is deliberately narrow. It establishes:

- a canonical event and flow ontology;
- JSON Schemas for events, flows, entities and relationships;
- source/version hashing and change detection;
- a first FCA publication collector;
- a synthetic gold-standard example flow;
- deterministic tests around `NEW`, `CHANGED` and `UNCHANGED` observations;
- documented methodology and source-confidence rules.

The initial pipeline is:

```text
official FCA source
      ↓
collect publication index item
      ↓
preserve observable representation
      ↓
hash + compare
      ↓
NEW / CHANGED / UNCHANGED
      ↓
emit source-level PolicyFlow event
      ↓
validate against schema
```

Semantic classification such as `consultation_published` is intentionally a later stage. The collector itself only establishes what was observed and whether it changed.

## Quick start

Requires Python 3.12+.

```bash
git clone https://github.com/mindblastsg/policyflow-uk.git
cd policyflow-uk
python -m venv .venv
source .venv/bin/activate
python -m pip install -e '.[dev]'
pytest
```

Run the first live collector:

```bash
policyflow ingest fca --limit 50
```

The first run emits `NEW` observations and source-level events. A local hash-state file is written under `.policyflow/state/`. Running the same command again should produce no change events unless the observable FCA listing items changed.

To include unchanged observations:

```bash
policyflow ingest fca --limit 50 --include-unchanged
```

## Repository map

```text
AGENTS.md                 agent/research guardrails
docs/                     ontology, methodology, sources, research agenda
schemas/                  machine-readable core contracts
src/policyflow/           collector, models, state and event pipeline
data/examples/            synthetic gold-standard flow fixtures
tests/                    deterministic fixture-based regression tests
.github/workflows/        continuous integration
```

## Intended future source layers

- GOV.UK / HM Treasury / HMRC
- UK Parliament APIs
- legislation.gov.uk
- FCA publications and Handbook
- PRA / Bank of England policy publications
- Companies House and regulated-entity data
- ONS, OBR and Bank of England economic datasets

## Near-term roadmap

1. Preserve full raw source observations and document versions.
2. Add semantic event classification as a separately provenance-tracked stage.
3. Add GOV.UK/HMT and Parliament collectors.
4. Link events across institutions into the first real historical policy flows.
5. Add temporal/delta queries and measure policy velocity.
6. Only then begin the economic-exposure and market-materiality layer.

## Status

**Experimental / pre-alpha.** The ontology and interfaces will change as real policy flows are tested.

## Important note

PolicyFlow UK is an independent research project. It is not affiliated with or endorsed by HM Government, Parliament, the FCA, PRA, Bank of England, HMRC or any other public body. Nothing in this repository constitutes legal, regulatory or investment advice.

## Licence

MIT. See `LICENSE`.
