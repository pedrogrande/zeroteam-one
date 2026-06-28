"""
App Settings
============

Shared runtime objects for the platform.
"""

from os import getenv

from agno.models.ollama import Ollama


def default_model() -> Ollama:
    """Fresh model instance per agent — avoids shared-state footguns.

    Model ID is configurable via the ``AGENT_MODEL_ID`` env var
    (default: ``glm-5.2:cloud``).
    """
    model_id = getenv("AGENT_MODEL_ID", "glm-5.2:cloud")
    return Ollama(id=model_id)
