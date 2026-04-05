# FastAPI Backend

## REST API Folder Structure

```text
backend/src/backend/
├── __init__.py
├── main.py                  # Entry point: initializes FastAPI app
├── api/                     # API Route handlers
│   ├── __init__.py
│   ├── deps.py              # Dependencies (Auth, DB sessions)
│   └── v1/                  # Versioning folder
│       ├── __init__.py
│       ├── api.py           # Main router that aggregates all v1 endpoints
│       └── endpoints/       # Individual resource routes
│           ├── __init__.py
│           └── items.py
├── db/                      # Database metadata, connection, and session.
│   ├── __init__.py
│   └── base.py
├── core/                    # Global config (pydantic settings, security)
│   ├── __init__.py
│   └── config.py
├── models/                  # Database models
│   ├── __init__.py
│   └── user.py
├── repositories/            # Raw CRUD/queries
│   ├── __init__.py
│   └── user.py
├── schemas/                 # Pydantic models (Request/Response validation)
│   ├── __init__.py
│   └── user.py
└── services/                # Business logic
    ├── __init__.py
    └── crud_user.py
```
