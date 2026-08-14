# PolicyFlow ontology v0.1

PolicyFlow represents policy as a temporal process rather than a collection of documents.

## Core objects

### Observation

A record that PolicyFlow retrieved a source at a particular time.

An observation answers: **what did the source look like when we saw it?**

Minimum properties:

- `observation_id`
- `source_id`
- `observed_at`
- `canonical_url`
- `content_hash`
- `raw_ref` or preserved raw payload

Observations are append-only.

### Document

A source artefact with continuing identity across versions, for example a consultation paper, Bill, statutory instrument, policy statement or Handbook provision.

A document answers: **what artefact is this?**

A document may have many observations/versions.

### Event

A material occurrence at a point in time or over a defined interval.

An event answers: **what happened?**

Examples:

- consultation published;
- consultation closed;
- government response published;
- Bill introduced;
- amendment agreed;
- SI laid;
- SI made;
- rule amended;
- commencement date reached;
- policy delayed;
- proposal withdrawn.

Events should reference their evidence.

### Flow

A coherent policy/regulatory process composed of related events.

A flow answers: **what process are these events part of?**

Flows can branch, merge, pause, restart or terminate. They are not assumed to be linear.

Example:

```text
announcement
   ↓
consultation
   ↓
response
   ├── draft SI
   │      ↓
   │    final SI
   │
   └── FCA consultation
          ↓
       policy statement
          ↓
       handbook rule
```

### Entity

A participant in, source of, target of or economically exposed party to a flow.

Initial entity types:

- `institution`
- `organisation`
- `company`
- `sector`
- `regulated_activity`
- `financial_product`
- `legal_instrument`
- `policy_topic`

### Relationship

A typed edge between objects.

Initial relationship vocabulary:

- `AMENDS`
- `REPEALS`
- `COMMENCES`
- `MADE_UNDER`
- `AUTHORISED_BY`
- `IMPLEMENTS`
- `RESPONDS_TO`
- `CONSULTS_ON`
- `SUPERSEDES`
- `REFERENCES`
- `DEFINES`
- `APPLIES_TO`
- `AFFECTS`
- `REQUIRES`
- `PROHIBITS`
- `PERMITS`
- `EXEMPTS`

Every relationship should carry provenance and a relationship status:

- `source_explicit`
- `human_confirmed`
- `machine_suggested`

## Policy state model

The initial state vocabulary is intentionally broad:

```text
IDEA
ANNOUNCED
UNDER_REVIEW
CONSULTATION
PROPOSED
LEGISLATING
MADE
IMPLEMENTING
IN_FORCE
AMENDED
DELAYED
WITHDRAWN
REPEALED
SUPERSEDED
```

Flows are not required to visit every state.

## Time model

PolicyFlow must distinguish:

- `observed_at`: when PolicyFlow saw the information;
- `published_at`: when the source says the information was published;
- `event_at`: when the represented event occurred;
- `effective_at`: when a legal/regulatory change takes effect;
- `valid_from` / `valid_to`: interval during which a state or relationship is valid.

This distinction is required for historical reconstruction and eventual event studies.

## Evidence and derivation

A claim may be:

- `SOURCE`: explicitly present in authoritative/formal source material;
- `DERIVED`: deterministically computed from source material;
- `MACHINE_EXTRACTED`: probabilistic extraction/classification;
- `RESEARCHER`: human research judgement;
- `HYPOTHESIS`: deliberately unconfirmed research proposition.

PolicyFlow must never silently promote a machine-extracted or hypothesis field into `SOURCE`.

## Future investor/economic layer

The core ontology should support, but not yet assume, relationships such as:

```text
policy event
  ↓
regulated activity
  ↓
financial product / business process
  ↓
company / sector
  ↓
revenue, cost, capital, volume or pricing channel
  ↓
security / economic variable
```

This layer should remain derived analysis, separate from the legal truth layer.
