"""
Actors API Router
=================

FastAPI router for actor CRUD.
"""

from __future__ import annotations

from typing import Optional
from uuid import uuid4

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

from api.deps import get_db_session
from api.schemas import ActorCreateRequest, ActorResponse
from tasks.domain import Actor
from tasks.repository import ActorRepository

router = APIRouter(prefix="/actors", tags=["actors"])


def _get_actor_repo(session: Session = Depends(get_db_session)) -> ActorRepository:
    return ActorRepository(session)


def _model_to_response(model) -> ActorResponse:
    return ActorResponse(
        actor_id=str(model.actor_id),
        actor_type=model.actor_type,
        display_name=model.display_name,
        trust_score=model.trust_score,
        reputation_score=model.reputation_score,
        public_key=model.public_key,
    )


@router.post("", response_model=ActorResponse, status_code=status.HTTP_201_CREATED)
def create_actor(
    request: ActorCreateRequest,
    repo: ActorRepository = Depends(_get_actor_repo),
) -> ActorResponse:
    """Create a new actor."""
    actor = Actor(
        actor_id=request.actor_id or str(uuid4()),
        actor_type=request.actor_type,
        display_name=request.display_name,
        trust_score=request.trust_score,
        reputation_score=request.reputation_score,
        public_key=request.public_key,
    )
    model = repo.create_actor(actor)
    return _model_to_response(model)


@router.get("", response_model=list[ActorResponse])
def list_actors(
    limit: int = Query(50, ge=1, le=500),
    offset: int = Query(0, ge=0),
    repo: ActorRepository = Depends(_get_actor_repo),
) -> list[ActorResponse]:
    """List actors."""
    models = repo.list_actors(limit=limit, offset=offset)
    return [_model_to_response(m) for m in models]


@router.get("/{actor_id}", response_model=ActorResponse)
def get_actor(
    actor_id: str,
    repo: ActorRepository = Depends(_get_actor_repo),
) -> ActorResponse:
    """Get an actor by ID."""
    model = repo.get_actor(actor_id)
    if model is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Actor not found: {actor_id}")
    return _model_to_response(model)


@router.patch("/{actor_id}", response_model=ActorResponse)
def update_actor(
    actor_id: str,
    trust_score: Optional[float] = Query(None),
    repo: ActorRepository = Depends(_get_actor_repo),
) -> ActorResponse:
    """Update an actor's trust score."""
    if trust_score is not None:
        model = repo.update_trust_score(actor_id, trust_score)
        if model is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Actor not found: {actor_id}")
        return _model_to_response(model)
    raise HTTPException(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        detail="No update fields provided",
    )
