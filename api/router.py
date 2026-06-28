"""
API Router Aggregation
=====================

Aggregates all sub-routers into a single ``APIRouter`` with
``prefix="/api/v1"``. Mounted on the custom FastAPI ``base_app`` in
``app/main.py``.
"""

from fastapi import APIRouter

from api.actors import router as actors_router
from api.tasks import router as tasks_router

api_router = APIRouter(prefix="/api/v1")
api_router.include_router(tasks_router)
api_router.include_router(actors_router)
