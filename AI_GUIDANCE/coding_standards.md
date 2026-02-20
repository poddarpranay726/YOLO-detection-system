# Coding Standards

This document defines implementation standards for maintaining clarity, safety, and change resilience.

The system prioritizes readability and correctness over clever abstractions.

---

## General Principles

- Prefer simple and explicit code.
- Avoid unnecessary abstraction.
- Do not introduce hidden side effects.
- Keep functions small and single-purpose.
- Avoid tightly coupling modules.

---

## API Layer

- Route handlers must remain thin.
- No business logic inside API routes.
- All request/response models must use Pydantic schemas.
- Explicitly validate all inputs.

---

## Service Layer

- All detection and caching logic must live in the service layer.
- Services should be deterministic where possible.
- Avoid modifying global state.
- Handle errors explicitly.

---

## Database Layer

- No direct database writes inside route handlers.
- Database schema changes require migration documentation.
- Avoid storing large binary objects inside the database.

---

## Error Handling

- Do not allow silent failures.
- Return structured and predictable error responses.
- Log unexpected states clearly.

---

The system must remain understandable even as new features are added.
