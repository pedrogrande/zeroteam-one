"""Tests for app/guardrails.py — guardrail and post-hook logic."""

from pathlib import Path
from unittest.mock import MagicMock

import pytest


def test_default_pre_hooks_returns_list():
    """default_pre_hooks should return a non-empty list."""
    from app.guardrails import default_pre_hooks

    hooks = default_pre_hooks()
    assert isinstance(hooks, list)
    assert len(hooks) >= 1  # at least PromptInjectionGuardrail


def test_default_pre_hooks_pii_toggle():
    """enable_pii flag should control PIIDetectionGuardrail inclusion."""
    from agno.guardrails import PIIDetectionGuardrail

    from app.guardrails import default_pre_hooks

    with_pii = default_pre_hooks(enable_pii=True)
    without_pii = default_pre_hooks(enable_pii=False)

    assert any(isinstance(h, PIIDetectionGuardrail) for h in with_pii)
    assert not any(isinstance(h, PIIDetectionGuardrail) for h in without_pii)


def test_default_pre_hooks_mask_pii():
    """mask_pii flag should be passed through to PIIDetectionGuardrail."""
    from agno.guardrails import PIIDetectionGuardrail

    from app.guardrails import default_pre_hooks

    hooks = default_pre_hooks(enable_pii=True, mask_pii=True)
    pii_guard = next(h for h in hooks if isinstance(h, PIIDetectionGuardrail))
    assert pii_guard.mask_pii is True


def test_make_file_path_validator_detects_missing():
    """File path validator should flag non-existent paths."""
    from agno.exceptions import OutputCheckError

    from app.guardrails import make_file_path_validator

    validator = make_file_path_validator(Path("/tmp/nonexistent_workspace"))
    mock_output = MagicMock()
    mock_output.content = "The function is in `nonexistent/path/file.py`"

    with pytest.raises(OutputCheckError):
        validator(mock_output)


def test_make_file_path_validator_passes_existing():
    """File path validator should pass when paths exist."""
    from app.guardrails import make_file_path_validator

    # Use a real path — the tests directory itself
    validator = make_file_path_validator(Path(__file__).resolve().parents[1])
    mock_output = MagicMock()
    mock_output.content = "The config is in `pyproject.toml`"
    mock_output.tools = []

    # Should not raise — pyproject.toml exists at repo root
    validator(mock_output)
