# Heterogeneous Adapters

Use the narrowest parser that preserves the most semantics, then emit the neutral model.

## Source categories

Text/Markdown/logs; CSV/TSV; XLSX; JSON/JSONL; XML; HTML; PDF; image-derived data; APIs/databases; source trees; C/C++ headers; Python/.pyi; TypeScript/.d.ts; Rust/Go/Java/C#/Swift/etc.; ELF/Mach-O/PE/.def/symbol maps; HAR/network traces; GraphQL/Protobuf/AsyncAPI/OpenAPI; SQL/build/config/deployment manifests; runtime observations/test traces.

## Adapter contract

```json
{
  "source_id":"...",
  "source_record_id":"...",
  "source_locator":"...",
  "raw_hash":"...",
  "record_type":"...",
  "raw":{},
  "parsed":{},
  "parse_warnings":[],
  "observed_or_inferred":"observed"
}
```

## Unknown formats

Use:

`content signature → filename clues → structure → semantics → candidate adapters → specialized adapter → neutral record`

Do not discard unknown formats merely because no built-in parser exists.
