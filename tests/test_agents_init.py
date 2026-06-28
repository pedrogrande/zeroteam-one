"""Smoke tests — verify all agents initialize without errors."""


def test_web_search_agent_initializes():
    """WebSearch agent should construct without errors."""
    from agents.web_search import web_search

    assert web_search is not None
    assert web_search.id == "web-search"


def test_code_search_agent_initializes():
    """CodeSearch agent should construct without errors."""
    from agents.code_search import code_search

    assert code_search is not None
    assert code_search.id == "code-search"


def test_agno_support_agent_initializes():
    """Agno Support agent should construct without errors."""
    from agents.agno_support import agno_support_agent

    assert agno_support_agent is not None
    assert agno_support_agent.id == "agno-support-agent"


def test_guardrails_module_imports():
    """The guardrails module should be importable for future use.

    Hooks are currently disabled on all agents to avoid interfering
    with prompt review/improvement workflows. The implementation is
    kept in app/guardrails.py for later activation.
    """
    from app.guardrails import (
        default_pre_hooks,
        make_file_path_validator,
        validate_citations_from_tools,
    )

    # Verify the factory functions work
    hooks = default_pre_hooks(enable_pii=True, mask_pii=True)
    assert len(hooks) == 2  # PromptInjection + PII

    hooks_no_pii = default_pre_hooks(enable_pii=False)
    assert len(hooks_no_pii) == 1  # PromptInjection only

    # Verify the post-hook factories are callable
    assert callable(validate_citations_from_tools)
    assert callable(make_file_path_validator)


def test_all_agents_have_tool_call_limit():
    """All agents should have a bounded tool_call_limit."""
    from agents.agno_support import agno_support_agent
    from agents.code_search import code_search
    from agents.web_search import web_search

    for agent in [web_search, code_search, agno_support_agent]:
        assert agent.tool_call_limit is not None, f"{agent.id} missing tool_call_limit"
        assert agent.tool_call_limit > 0, f"{agent.id} has non-positive tool_call_limit"
