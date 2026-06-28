"""
Guardrails
==========

Shared guardrail and post-hook definitions for all agents.
Supports the lab's "responsible agentic AI" mandate by enforcing
input safety (prompt injection, PII, moderation) and output
integrity (citation grounding, file-path verification).
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import Callable

from agno.exceptions import CheckTrigger, OutputCheckError
from agno.guardrails import PIIDetectionGuardrail, PromptInjectionGuardrail
from agno.run.agent import RunOutput

# ---------------------------------------------------------------------------
# Pre-hook guardrails (input validation)
# ---------------------------------------------------------------------------


def default_pre_hooks(*, enable_pii: bool = True, mask_pii: bool = False) -> list:
    """Return a list of pre-hook guardrails for input validation.

    Args:
        enable_pii: If True, include PIIDetectionGuardrail.
        mask_pii: If True, PII is masked in the input rather than raising
            an error. Useful for user-facing teams with a LearningMachine
            that captures profile data — masking lets the run proceed
            with sanitized input instead of blocking.
    """
    hooks: list = [PromptInjectionGuardrail()]
    if enable_pii:
        hooks.append(PIIDetectionGuardrail(mask_pii=mask_pii))
    return hooks


# ---------------------------------------------------------------------------
# Post-hook validators (output validation — plain functions, NOT BaseGuardrail)
# ---------------------------------------------------------------------------


def validate_citations_from_tools(run_output: RunOutput) -> None:
    """Post-hook: ensure any URL cited in the response appeared in tool results.

    Prevents the agent from hallucinating sources that were never fetched.
    Raises OutputCheckError if cited URLs are not grounded in tool output.
    """
    response_content = str(run_output.content or "")

    # Collect all URLs from tool execution results
    tool_urls: set[str] = set()
    if run_output.tools:
        for tool_exec in run_output.tools:
            result_str = str(getattr(tool_exec, "result", "") or "")
            tool_urls.update(re.findall(r'https?://[^\s"\'<>]+', result_str))

    # Find all URLs cited in the response
    cited_urls: set[str] = set(re.findall(r'https?://[^\s"\'<>]+', response_content))

    unverified = cited_urls - tool_urls
    if unverified:
        raise OutputCheckError(
            f"Response cites URLs not found in tool results: {unverified}",
            check_trigger=CheckTrigger.OUTPUT_NOT_ALLOWED,
        )


def make_file_path_validator(workspace_root: Path) -> Callable[[RunOutput], None]:
    """Create a post-hook function bound to a specific workspace root.

    Ensures file paths cited in the response actually exist under
    ``workspace_root``. Prevents the CodeSearch agent from fabricating
    file paths.

    Usage:
        post_hooks=[make_file_path_validator(Path("/app"))]
    """

    def _validator(run_output: RunOutput) -> None:
        response_content = str(run_output.content or "")

        # Find all backtick-quoted paths in the response (e.g. `app/main.py`)
        cited_paths = re.findall(r"`([^`]+\.\w+)`", response_content)

        missing: list[str] = []
        for cited in cited_paths:
            # Skip URLs and non-path strings (no path separator)
            if cited.startswith("http") or ("/" not in cited and "\\" not in cited):
                continue
            candidate = workspace_root / cited
            if not candidate.exists():
                missing.append(cited)

        if missing:
            raise OutputCheckError(
                f"Response cites file paths that do not exist in the workspace: {missing}",
                check_trigger=CheckTrigger.OUTPUT_NOT_ALLOWED,
            )

    return _validator
