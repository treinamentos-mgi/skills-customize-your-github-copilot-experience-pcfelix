# 📘 Assignment: Testing FastAPI Endpoints

## 🎯 Objective

Write automated tests for a small FastAPI application using `pytest` and FastAPI's `TestClient`. Verify successful responses as well as common HTTP error responses without starting a web server.

## 📝 Tasks

### 🛠️ Test successful API responses

#### Description

Use the provided `api.py` application and complete the tests for its health-check and echo endpoints.

#### Requirements

The completed tests must:

- Use `TestClient` to send requests directly to the FastAPI app.
- Verify that `GET /health` returns HTTP 200 and `{"status": "ok"}`.
- Verify that `POST /echo` returns HTTP 200 and the submitted message.

### 🛠️ Test validation and error responses

#### Description

Add tests for invalid input and a path that the application does not provide.

#### Requirements

The completed tests must:

- Verify that `POST /echo` without the required `message` field returns HTTP 422.
- Verify that a request to an unknown path returns HTTP 404.
- Run successfully with `pytest -q` from this assignment's directory.

Install the required packages and run the test suite with:

```bash
python -m pip install fastapi httpx pytest
pytest -q
```