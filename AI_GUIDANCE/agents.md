# AI Agent Behavior Rules

This file defines constraints for any AI-assisted code generation within this repository.

The goal is to preserve architectural integrity, prevent unintended side effects, and maintain system correctness.

---

## Architectural Constraints

- Do not modify the database schema without an explicit migration plan.
- Do not bypass the service layer from API routes.
- All detection logic must remain inside the service layer.
- Do not move caching logic into the route handler.
- Do not introduce global mutable state.

---

## Interface Safety

- All new endpoints must use Pydantic schemas for request and response validation.
- Do not change existing API contracts without explicit documentation.
- Validate all external inputs.
- Do not remove type annotations.

---

## Caching Integrity

- Caching must remain SHA256 content-hash based.
- Do not replace content-hash caching with filename-based caching.
- Do not disable cache checks before inference.

---

## Code Quality

- Prefer clarity over cleverness.
- Keep functions small and single-purpose.
- Do not introduce unnecessary abstraction.
- Avoid tightly coupling new features with existing modules.

---

## AI Usage Policy

- AI-generated code must be reviewed before integration.
- AI must not invent database fields or schema changes.
- AI must suggest test cases when introducing new logic.
- AI must not silently change core behavior.

---

The system prioritizes correctness, simplicity, and change resilience over feature expansion.
