# Contributing to PolicyFlow UK

PolicyFlow is an experimental research infrastructure project. Contributions are welcome, especially around source adapters, legal/regulatory ontology, data quality, temporal modelling and reproducibility.

## Good first contributions

- add or improve an official-source collector;
- contribute a small historical policy-flow fixture;
- improve source parsing without changing semantics;
- add tests for change detection or schema validation;
- document a policy-process edge case;
- identify an incorrect or ambiguous relationship type.

## Contribution principles

### Preserve provenance

Every captured observation should retain enough information to trace it back to its source. Do not replace source evidence with a summary.

### Separate observation from interpretation

A regulator publishing a consultation is an observable event. A conclusion that the consultation is likely to increase costs for a sector is derived analysis. They belong in different fields/layers.

### Do not rewrite history

PolicyFlow is temporal. Previously observed versions should not be deleted just because a source later changes.

### Prefer canonical sources

Use official government, parliamentary, legislative and regulator sources wherever possible. Secondary sources may be useful for research but should not silently become authoritative state.

## Pull requests

Please include:

1. what changed;
2. why it changed;
3. which source(s) or fixtures are affected;
4. tests or validation performed;
5. any ontology or backwards-compatibility implications.

## Data and licensing

Source data may have its own copyright, licensing and reuse terms. Contributors are responsible for identifying source-specific conditions and should avoid committing large copyrighted document corpora when a canonical URL, hash and reproducible retrieval mechanism are sufficient.

## Safety and scope

PolicyFlow is research infrastructure, not legal, regulatory or investment advice. Do not present experimental scores, classifications or model outputs as authoritative conclusions.
