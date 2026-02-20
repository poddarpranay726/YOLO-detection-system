# Walkthrough – YOLO Detection System

This walkthrough explains the architecture, AI usage, risks, and extension strategy of the system.

The goal of this system is correctness, simplicity, and change resilience rather than feature expansion.

---

## 1. System Overview

This system performs object detection using YOLOv8.

It includes:

- A React frontend for image upload
- A FastAPI backend for inference
- A relational SQLite database for logging detection metadata
- SHA256-based content hashing to prevent redundant inference

The key architectural goal was to build a small, well-structured system that remains understandable as it evolves.

---

## 2. Architecture Overview

The system follows a layered structure:

Frontend → API Layer → Service Layer → Database → Model

### API Layer
- Handles HTTP requests
- Validates inputs using FastAPI and Pydantic
- Delegates logic to services

### Service Layer
- Handles detection logic
- Handles SHA256 hashing
- Implements caching logic
- Stores detection results

### Database Layer
- Stores detection metadata
- Does not store image binaries
- Uses relational schema for structure and integrity

This separation ensures that changes in one layer do not cascade across the system.

---

## 3. Content-Based Caching Design

To prevent redundant inference:

1. The image file is hashed using SHA256.
2. The hash acts as a deterministic identity.
3. Before running YOLO, the system checks the database for an existing record.
4. If found, the cached output image is returned.
5. If not found, YOLO runs and results are stored.

This approach improves efficiency and reduces compute cost.

Tradeoff:
- Minor changes to the image result in a new hash.

The caching logic is explicitly protected in AI guidance files to prevent accidental removal.

---

## 4. Database Design

The system uses SQLite for simplicity.

The database stores:

- Image hash
- Image name
- Detected object
- Confidence score
- Timestamp

Design decisions:
- No image binaries stored in database
- Relational schema ensures structure

---

## 5. AI Usage

AI was used for scaffolding and boilerplate generation.

However:

- Architectural decisions were manually reviewed.
- Caching logic was intentionally designed.
- Database schema was explicitly defined.
- AI outputs were constrained using AI_GUIDANCE rules.

AI was treated as an assistant, not an authority.

Risks of AI usage:
- Hallucinated schema fields
- Unintended architectural drift
- Hidden side effects

These risks were mitigated through explicit constraints and manual verification.

---

## 6. Correctness and Interface Safety

The system ensures correctness through:

- Deterministic SHA256 hashing
- Strict route validation using FastAPI
- Clear architectural boundaries
- Explicit separation of layers

Invalid states are minimized by design.

---

## 7. Change Resilience

The system is designed so that new features:

- Do not require modifications across unrelated modules
- Do not break API contracts silently
- Do not bypass caching logic

Examples:

- Adding authentication would involve adding a new model and middleware without altering detection logic.
- Replacing SQLite with cloud storage would not affect service logic.

---

## 8. Observability

The system includes:

- Clear logging for cache hits
- Deterministic file naming
- Structured API responses
- Inspectable database state

Failures are diagnosable through logs and database inspection.

---

## 9. Known Limitations

- SQLite is not suitable for distributed production systems.
- No authentication or rate limiting.
- File storage is local and not cloud-based.
- Hash-based caching depends on exact file equality.

These limitations were accepted to prioritize simplicity and clarity.

---

## 10. Extension Strategy

Future improvements could include:

- User authentication
- Redis-based caching
- Background inference queue
- Cloud storage for image files

Each of these extensions can be implemented without breaking core architectural boundaries.

---

The system prioritizes structure, safety, and maintainability over feature complexity.
