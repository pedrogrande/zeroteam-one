"""
API Dependencies
================

FastAPI dependencies for the task contract API.
"""

from typing import Generator

from sqlalchemy.orm import Session

from tasks.db import get_session
from tasks.repository import ActorRepository, ContractRepository


def get_db_session() -> Generator[Session, None, None]:
    """Yield a SQLAlchemy session. Closed after the request."""
    yield from get_session()


def get_contract_repo(session: Session = None) -> ContractRepository:
    """Get a ContractRepository. Used as a FastAPI dependency."""
    if session is None:
        # When used as a dependency, FastAPI injects the session
        # via get_db_session. This fallback is for manual use.
        from tasks.db import _get_session_factory

        session = _get_session_factory()()
    return ContractRepository(session)


def get_actor_repo(session: Session = None) -> ActorRepository:
    """Get an ActorRepository. Used as a FastAPI dependency."""
    if session is None:
        from tasks.db import _get_session_factory

        session = _get_session_factory()()
    return ActorRepository(session)
