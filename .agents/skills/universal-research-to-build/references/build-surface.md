# Build Surface

A build surface is a machine-readable model of externally observable interface/build behavior that can be projected into concrete formats.

## Core model

```text
Package/Module
  ├─ Type
  │   ├─ Field
  │   ├─ Enum
  │   └─ Constraint
  ├─ Function/Method
  │   ├─ Parameter
  │   ├─ Return
  │   └─ Error
  ├─ Event/Message
  ├─ Resource/Endpoint
  ├─ Dependency
  └─ Compatibility rule
```

## Metadata

Track where relevant:

- provenance and version
- platform/architecture
- visibility
- nullability/defaults/enums
- serialization and wire details
- lifecycle/threading constraints
- calling convention/ABI
- observed vs inferred
- confidence
- unsupported/unknown features
- verification method

## Projections

Support C/C++ headers, Python `def`/`.pyi`, TypeScript `.d.ts`, Rust/Go/Java/C#/Swift signatures, OpenAPI, AsyncAPI, GraphQL SDL, Protobuf, SQL, ABI/symbol reports, and build/config/deployment manifests.

## Compatibility matrix

Separate:

- syntax compatibility
- source compatibility
- binary/ABI compatibility
- protocol/wire compatibility
- behavioral compatibility
- version compatibility

Never infer a stronger compatibility class from weaker evidence.
