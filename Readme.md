YOLO Detection System with Relational Logging and Content-Based Caching
Overview

This system performs object detection using YOLOv8 and stores detection results in a relational database. It implements SHA256-based content hashing to prevent redundant inference on duplicate images.

The goal of this system is correctness, simplicity, and change resilience rather than feature complexity.

Architecture

Frontend: React
Backend: FastAPI
Database: SQLite (relational)
Model: YOLOv8
Caching: SHA256 content-based hash

Flow:

Upload → Hash Image → Check Cache →
If exists → Return cached result
If not → Run YOLO → Store results → Return output

Key Technical Decisions
1. Service-Oriented Structure

Detection logic is separated from API routes to improve testability and reduce coupling.

2. Content-Based Caching

SHA256 hash ensures deterministic identity for images.
Prevents redundant computation.
Improves performance and reduces inference cost.

Tradeoff:
Minor changes to image produce new hash.

3. Relational Database Logging

Detection metadata stored in SQLite.
No image binary stored in DB.
Maintains normalized structure.

4. Interface Safety

FastAPI request validation.
Typed schemas.
Clear separation between layers.

Risks and Tradeoffs

SQLite not suitable for distributed scaling.

No authentication implemented.

Filesystem storage may need migration to cloud storage.

Hash-based caching assumes exact file equality.

Change Resilience

New detection models can be added in service layer.

Database can be migrated to PostgreSQL with minimal code changes.

Caching can be replaced with Redis without API changes.

Observability

Logs cache hits.

Deterministic file naming.

Structured API responses.

DB state verifiable independently.

AI Usage

AI was used for scaffolding boilerplate code.
All architectural decisions were manually reviewed.
Database schema and caching logic were intentionally designed and verified.

AI outputs were constrained using explicit guidance files included in this repository.

##How to Run

###Prerequisites

-Python 3.10 or higher

-Node.js 18 or higher

-npm

-Git

---

###Backend Setup

Open a terminal and navigate to the project root:

cd yolo-detection-system


Go to the backend folder:

```bash
cd backend
```


Create a virtual environment:

```bash
python -m venv venv
```


Activate the virtual environment:

**Windows**
```bash
venv\Scripts\activate
```


**Mac/Linux**
```bash
source venv/bin/activate
```


Install backend dependencies:

```bash
pip install -r requirements.txt
```

Start the FastAPI server:

```bash
uvicorn main:app --reload
```


The backend will run at:

http://127.0.0.1:8000


Interactive API documentation is available at:

http://127.0.0.1:8000/docs

###Frontend Setup

Open a new terminal.

Navigate to the frontend folder:

```bash
cd frontend
```


Install frontend dependencies:

```bash
npm install
```


Start the React development server:

```bash
npm start
```

The frontend will run at:

http://localhost:3000

### Application Behavior

- First image upload runs YOLO inference.
- Detection results are stored in SQLite.
- Re-uploading the same image returns the cached output.
- Caching is based on SHA256 content hashing.

### Database Location

The SQLite database file is created at:

```bash
backend/detections.db
```

It stores detection metadata including:
- image hash
- object name
- confidence score
- timestamp
