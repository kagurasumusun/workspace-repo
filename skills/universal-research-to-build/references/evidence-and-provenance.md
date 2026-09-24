# Evidence and Provenance

## Source record

```text
source_id
source_kind
locator
retrieved_at
observed_version
content_hash
authority
reliability
independence
freshness
directness
applicability
usefulness
rights_status
extraction_method
scope
notes
```

## Claim record

```text
claim_id
claim_text
source_ids[]
source_locators[]
support_level
confidence
contradicted_by[]
transformation
status
```

## Independence

Repeated copies, mirrors, or derivative summaries are not independent confirmations. Record source-family relationships when known.

## Conflicts

Retain competing assertions. A canonical choice requires an explicit resolution rule and provenance. Do not erase rejected assertions when they may matter to auditability.

## Absence

A retrieval failure is evidence about the route, not proof of nonexistence. Preserve distinct absence/access states.

## Derivation

For every material derived value record:

`inputs → transformation → output → parser/tool/model version`

Keep observed, inferred, estimated, and synthesized values distinct.
