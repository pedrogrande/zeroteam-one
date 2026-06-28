"""
Tests for the /tasks and /actors API endpoints
==============================================

Uses FastAPI's TestClient against a dedicated Postgres test database
(zeroedge-test-db on port 5433). The conftest creates/drops tables per
test for isolation — no SQLite, no column-type patching.
"""

from __future__ import annotations

from uuid import uuid4

from fastapi.testclient import TestClient

# ---------------------------------------------------------------------------
# Helper to create an actor
# ---------------------------------------------------------------------------


def _create_actor(client: TestClient) -> str:
    """Create an actor and return its ID."""
    actor_id = str(uuid4())
    resp = client.post(
        "/api/v1/actors",
        json={
            "actor_id": actor_id,
            "actor_type": "human",
            "display_name": "Test Actor",
        },
    )
    assert resp.status_code == 201, resp.text
    return actor_id


# ---------------------------------------------------------------------------
# Helper to create a minimal task contract document
# ---------------------------------------------------------------------------


def _make_task_document(actor_id: str) -> dict:
    return {
        "contract_id": str(uuid4()),
        "created_at": "2026-06-27T00:00:00+00:00",
        "contract_type": "one-off",
        "status": "draft",
        "actor_roles": [
            {
                "role_id": str(uuid4()),
                "contract_id": str(uuid4()),
                "actor_id": actor_id,
                "role_type": "requester",
            }
        ],
    }


# ---------------------------------------------------------------------------
# Actor tests
# ---------------------------------------------------------------------------


def test_create_actor(client):
    resp = client.post(
        "/api/v1/actors",
        json={
            "actor_type": "human",
            "display_name": "Jane Doe",
        },
    )
    assert resp.status_code == 201
    data = resp.json()
    assert data["display_name"] == "Jane Doe"
    assert data["actor_type"] == "human"
    assert data["actor_id"]


def test_list_actors(client):
    _create_actor(client)
    _create_actor(client)
    resp = client.get("/api/v1/actors")
    assert resp.status_code == 200
    assert len(resp.json()) >= 2


def test_get_actor(client):
    actor_id = _create_actor(client)
    resp = client.get(f"/api/v1/actors/{actor_id}")
    assert resp.status_code == 200
    assert resp.json()["actor_id"] == actor_id


def test_get_actor_not_found(client):
    resp = client.get(f"/api/v1/actors/{uuid4()}")
    assert resp.status_code == 404


# ---------------------------------------------------------------------------
# Task tests
# ---------------------------------------------------------------------------


def test_create_task(client):
    actor_id = _create_actor(client)
    resp = client.post(
        "/api/v1/tasks",
        json={
            "actor_id": actor_id,
            "contract_kind": "task",
            "contract_document": _make_task_document(actor_id),
        },
    )
    assert resp.status_code == 201, resp.text
    data = resp.json()
    assert data["version"] == "1.0.0"
    assert data["status"] == "draft"
    assert data["contract_id"]


def test_create_task_nonexistent_actor(client):
    """Creating a task with a non-existent actor should return 422."""
    resp = client.post(
        "/api/v1/tasks",
        json={
            "actor_id": str(uuid4()),
            "contract_kind": "task",
            "contract_document": _make_task_document(str(uuid4())),
        },
    )
    assert resp.status_code == 422


def test_list_tasks(client):
    actor_id = _create_actor(client)
    client.post(
        "/api/v1/tasks",
        json={
            "actor_id": actor_id,
            "contract_kind": "task",
            "contract_document": _make_task_document(actor_id),
        },
    )
    resp = client.get("/api/v1/tasks")
    assert resp.status_code == 200
    data = resp.json()
    assert data["total"] >= 1


def test_get_task(client):
    actor_id = _create_actor(client)
    create_resp = client.post(
        "/api/v1/tasks",
        json={
            "actor_id": actor_id,
            "contract_kind": "task",
            "contract_document": _make_task_document(actor_id),
        },
    )
    task_id = create_resp.json()["contract_id"]
    resp = client.get(f"/api/v1/tasks/{task_id}")
    assert resp.status_code == 200
    assert resp.json()["contract_id"] == task_id


def test_get_task_not_found(client):
    resp = client.get(f"/api/v1/tasks/{uuid4()}")
    assert resp.status_code == 404


def test_update_task_creates_new_version(client):
    actor_id = _create_actor(client)
    create_resp = client.post(
        "/api/v1/tasks",
        json={
            "actor_id": actor_id,
            "contract_kind": "task",
            "contract_document": _make_task_document(actor_id),
        },
    )
    task_id = create_resp.json()["contract_id"]

    # Update — should create version 1.0.1
    update_resp = client.patch(
        f"/api/v1/tasks/{task_id}",
        json={
            "actor_id": actor_id,
            "changes": {"contract_type": "recurring"},
        },
    )
    assert update_resp.status_code == 200, update_resp.text
    assert update_resp.json()["version"] == "1.0.1"

    # Version history should show 2 versions
    versions_resp = client.get(f"/api/v1/tasks/{task_id}/versions")
    assert versions_resp.status_code == 200
    assert len(versions_resp.json()) == 2


def test_transition_task(client):
    actor_id = _create_actor(client)
    create_resp = client.post(
        "/api/v1/tasks",
        json={
            "actor_id": actor_id,
            "contract_kind": "task",
            "contract_document": _make_task_document(actor_id),
        },
    )
    task_id = create_resp.json()["contract_id"]

    # Transition draft → open (valid)
    resp = client.post(
        f"/api/v1/tasks/{task_id}/transition",
        json={
            "actor_id": actor_id,
            "to_state": "open",
        },
    )
    assert resp.status_code == 200, resp.text
    assert resp.json()["status"] == "open"


def test_transition_task_invalid(client):
    actor_id = _create_actor(client)
    create_resp = client.post(
        "/api/v1/tasks",
        json={
            "actor_id": actor_id,
            "contract_kind": "task",
            "contract_document": _make_task_document(actor_id),
        },
    )
    task_id = create_resp.json()["contract_id"]

    # Transition draft → completed (invalid — must go through open first)
    resp = client.post(
        f"/api/v1/tasks/{task_id}/transition",
        json={
            "actor_id": actor_id,
            "to_state": "completed",
        },
    )
    assert resp.status_code == 422


def test_audit_trail(client):
    actor_id = _create_actor(client)
    create_resp = client.post(
        "/api/v1/tasks",
        json={
            "actor_id": actor_id,
            "contract_kind": "task",
            "contract_document": _make_task_document(actor_id),
        },
    )
    task_id = create_resp.json()["contract_id"]

    # Update to generate a second audit event
    client.patch(
        f"/api/v1/tasks/{task_id}",
        json={"actor_id": actor_id, "changes": {"contract_type": "recurring"}},
    )

    resp = client.get(f"/api/v1/tasks/{task_id}/audit")
    assert resp.status_code == 200
    events = resp.json()["events"]
    assert len(events) == 2  # create + update
    # Hash chain: second event should have previous_hash set
    assert events[0]["previous_hash"] is None
    assert events[1]["previous_hash"] is not None
    assert events[1]["previous_hash"] == events[0]["immutable_hash"]


def test_claim_task(client):
    actor_id = _create_actor(client)
    # Create a task and transition it to open
    create_resp = client.post(
        "/api/v1/tasks",
        json={
            "actor_id": actor_id,
            "contract_kind": "task",
            "contract_document": _make_task_document(actor_id),
        },
    )
    task_id = create_resp.json()["contract_id"]
    client.post(
        f"/api/v1/tasks/{task_id}/transition",
        json={"actor_id": actor_id, "to_state": "open"},
    )

    # Claim it
    resp = client.post(
        f"/api/v1/tasks/{task_id}/claim",
        json={"actor_id": actor_id},
    )
    assert resp.status_code == 200, resp.text
    assert resp.json()["status"] == "claimed"
