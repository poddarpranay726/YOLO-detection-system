# System Constraints

This document defines structural and architectural constraints that must not be violated.

These constraints protect correctness and prevent architectural drift.

---

## Architectural Boundaries

- API routes must not contain business logic.
- Detection logic must remain inside the service layer.
- Caching logic must not be removed or bypassed.
- Database access must be abstracted behind defined layers.

---

## Data Integrity

- Image identity must be determined using SHA256 content hashing.
- Filename-based caching is not permitted.
- Duplicate detection entries must be prevented through hash checks.

---

## State Management

- No global mutable state.
- No hidden shared state across modules.
- All state changes must be explicit.

---

## Extension Rules

- New features must not modify existing contracts silently.
- Adding new features must not require changes across unrelated modules.
- Schema updates must include documentation.

---

These constraints exist to preserve system stability as the codebase evolves.
