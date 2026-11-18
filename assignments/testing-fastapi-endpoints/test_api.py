import pytest
from fastapi.testclient import TestClient

from api import app

client = TestClient(app)


def test_health_endpoint_returns_ok():
    response = client.get("/health")

    # TODO: Assert the status code and JSON response.
    pytest.fail("Complete the health endpoint assertions.")


def test_echo_endpoint_returns_message():
    response = client.post("/echo", json={"message": "hello"})

    # TODO: Assert the status code and echoed JSON response.
    pytest.fail("Complete the echo endpoint assertions.")


def test_echo_endpoint_requires_message():
    response = client.post("/echo", json={})

    # TODO: Assert that FastAPI returns HTTP 422.
    pytest.fail("Complete the validation error assertion.")


def test_unknown_endpoint_returns_not_found():
    response = client.get("/unknown")

    # TODO: Assert that the response status code is HTTP 404.
    pytest.fail("Complete the not-found assertion.")