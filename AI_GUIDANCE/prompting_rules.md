# AI Prompting Rules

This file defines how AI assistance should be used in this repository.

AI is used as a productivity tool, not as an authority.

---

## Prompt Design Rules

- Prompts must clearly specify architectural boundaries.
- Prompts must state that caching logic cannot be removed.
- Prompts must prohibit schema hallucination.
- Prompts must request type-safe implementations.

---

## Safety Rules

- AI must not invent new database fields.
- AI must not modify existing API behavior without explicit instruction.
- AI must not introduce global state.
- AI must not bypass validation layers.

---

## Review Rules

- All AI-generated code must be reviewed before integration.
- AI suggestions must be tested before merging.
- AI must suggest test cases when introducing logic changes.
- AI outputs must be checked for hidden side effects.

---

AI assistance must preserve correctness, simplicity, and change resilience.
