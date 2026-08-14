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

The first release is deliberately narrow. It will establish:

- a canonical event and flow ontology;
- JSON Schemas for events, flows, entities and relationships;
- source/version hashing and change detection;
- a first FCA publication collector;
- a small gold-standard example flow;
- deterministic tests around `NEW`, `CHANGED` and `UNCHANGED` observations;
- documented methodology and source-confidence rules.

The initial milestone is:

```text
official FCA source
      ↓
collect publication
      ↓
preserve raw observation
      ↓
hash + compare
      ↓
NEW / CHANGED / UNCHANGED
      ↓
emit PolicyFlow event
      ↓
validate against schema
```

## Intended future source layers

- GOV.UK / HM Treasury / HMRC
- UK Parliament APIs
- legislation.gov.uk
- FCA publications and Handbook
- PRA / Bank of England policy publications
- Companies House and regulated-entity data
- ONS, OBR and Bank of England economic datasets

## Status

**Experimental / pre-alpha.** The ontology and interfaces will change as real policy flows are tested.

## Important note

PolicyFlow UK is an independent research project. It is not affiliated with or endorsed by HM Government, Parliament, the FCA, PRA, Bank of England, HMRC or any other public body. Nothing in this repository constitutes legal, regulatory or investment advice.

## Licence

The project is intended to be open source. See `LICENSE` once the initial v0.1 scaffold lands.
