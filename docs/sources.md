# Source registry v0.1

PolicyFlow should prefer official, canonical and machine-readable sources wherever available.

## Initial priority sources

### Financial Conduct Authority

- Publications: `https://www.fca.org.uk/publications`
- News and speeches: `https://www.fca.org.uk/news`
- Handbook: `https://www.handbook.fca.org.uk/`
- Financial Services Register: `https://register.fca.org.uk/`

Initial use:

- consultations;
- policy statements;
- discussion papers;
- finalised guidance;
- Handbook changes;
- regulatory signals and implementation material.

### GOV.UK / HM Treasury / HMRC

- GOV.UK: `https://www.gov.uk/`
- GOV.UK Content API: `https://content-api.publishing.service.gov.uk/`
- GOV.UK Search API: `https://www.search-api.publishing.service.gov.uk/`
- HM Treasury: `https://www.gov.uk/government/organisations/hm-treasury`
- HMRC: `https://www.gov.uk/government/organisations/hm-revenue-customs`

Initial use:

- consultations and calls for evidence;
- consultation responses;
- policy papers;
- speeches and announcements;
- Budget/fiscal-event documents;
- tax-policy development and guidance.

### UK Parliament

- Developer hub: `https://developer.parliament.uk/`
- Bills API: `https://bills-api.parliament.uk/`
- Hansard: `https://hansard.parliament.uk/`

Initial use:

- Bill stages;
- amendments;
- statutory-instrument parliamentary progress;
- written statements/questions;
- committee activity;
- political and scrutiny signals.

### UK legislation

- legislation.gov.uk: `https://www.legislation.gov.uk/`
- Developer information: `https://www.legislation.gov.uk/developer`

Initial use:

- Acts;
- statutory instruments;
- draft instruments where available;
- commencement and amendment relationships;
- canonical legal text and metadata.

### Prudential Regulation Authority / Bank of England

- PRA policy: `https://www.bankofengland.co.uk/prudential-regulation/policy`
- Bank of England: `https://www.bankofengland.co.uk/`

Initial use:

- consultation papers;
- policy statements;
- supervisory statements;
- prudential rule changes;
- official cost-benefit material;
- financial-system statistics.

## Later entity and impact sources

### Companies House

- Developer API: `https://developer.company-information.service.gov.uk/`

Potential use:

- company identity;
- company numbers;
- filings and corporate metadata;
- entity resolution.

### Office for National Statistics

- Developer portal: `https://developer.ons.gov.uk/`

Potential use:

- economic transmission variables;
- sector, labour-market, price and activity data.

### Office for Budget Responsibility

- Data: `https://obr.uk/data/`

Potential use:

- official policy costings;
- fiscal forecasts and outturn comparisons;
- tax and spending series.

## Source classes

Each source adapter should declare one of the following broad classes:

- `authoritative_state`
- `formal_process`
- `political_signal`
- `impact_evidence`

A source class describes how the source should be interpreted. It does not remove the need for record-level provenance or uncertainty.

## Licensing and reuse

Public accessibility does not imply unrestricted republication. Each collector should document relevant reuse/licensing terms before raw source material is persisted or redistributed at scale. Prefer canonical URLs, hashes and reproducible retrieval over unnecessarily mirroring large document corpora.
