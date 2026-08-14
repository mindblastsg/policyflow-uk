# Methodology v0.1

PolicyFlow is designed to reconstruct policy movement as it was observable through public sources at a given point in time.

## 1. Source acquisition

Collectors retrieve canonical public sources and preserve enough information to reproduce the observation:

- source identifier;
- canonical URL;
- retrieval timestamp;
- HTTP metadata where useful;
- raw or minimally transformed content;
- deterministic content hash.

Collectors should not perform semantic interpretation during retrieval.

## 2. Version and change detection

For each continuing document/source object, compare the current normalised content hash with the latest stored observation.

Classification:

- `NEW`: no previous observation for the document identity;
- `CHANGED`: a previous observation exists and the content hash differs;
- `UNCHANGED`: a previous observation exists and the hash is identical.

Normalisation must be deterministic and documented. Cosmetic boilerplate should only be removed when doing so cannot erase policy-relevant meaning.

## 3. Event creation

An observation does not automatically equal a material policy event.

Deterministic source metadata should be used first. Where interpretation is required, PolicyFlow may create a machine-suggested event containing:

- event type;
- event time;
- actor;
- candidate flow;
- source evidence;
- extraction confidence;
- extraction method/version.

Machine-suggested events must remain distinguishable from source-explicit or human-confirmed events.

## 4. Flow matching

Events may be attached to an existing flow using explicit identifiers, citations, titles, policy names, legal references and other deterministic signals. Probabilistic matching may suggest links, but it must not silently establish causality.

Possible outcomes:

- attach to confirmed flow;
- suggest attachment with confidence;
- create candidate new flow;
- leave unclassified.

## 5. Delta analysis

PolicyFlow should eventually answer not only what a new publication says, but what changed relative to the previous stage.

Delta analysis may include:

- scope widened/narrowed;
- implementation accelerated/delayed;
- threshold changed;
- affected population changed;
- obligation added/removed;
- exemption added/removed;
- implementation probability increased/decreased;
- financial/economic impact estimate changed.

The source text and previous version must remain available alongside the derived delta.

## 6. Confidence model

Do not use one universal confidence score for everything.

At minimum keep separate:

- `source_confidence`: authority of the underlying source category;
- `extraction_confidence`: confidence in machine extraction/classification;
- `relationship_confidence`: confidence that two objects are related;
- `impact_confidence`: confidence in downstream economic interpretation.

Authoritative legal state can have high source confidence while a downstream company-impact inference remains low confidence.

## 7. Reproducibility

Every derived record should be capable of pointing to:

- evidence object(s);
- algorithm/model used;
- relevant version;
- timestamp of derivation;
- input record identifiers.

Historical runs should not be silently recomputed in place when models change.

## 8. Research posture

The system should make uncertainty visible. Failed classifications, unmatched events and ambiguous relationships are useful research outputs rather than errors to hide.

The initial goal is not comprehensive UK coverage. It is to demonstrate that a small number of policy flows can be reconstructed faithfully, queried temporally and extended into reproducible research variables.
