# Agentic Expert

| Field | Value |
|-------|-------|
| **Session** | `cc231e82...` |
| **Type** | agent |
| **Agent** | Agentic Expert |
| **User** | pete@peterargent.com |
| **Created** | 2026-06-12T15:09:39 |
| **Runs** | 5 completed / 5 total |

## Run 1 — Agentic Expert ✓ COMPLETED

*2026-06-12T15:09:39* · `glm-5.1:cloud` · `c7c4497f...`

### Prompt

tell me about post-hooks in Agno. What might they be good for?

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.agno.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Pre-hooks and Post-hooks

> Execute custom logic before and after agent runs with hooks.

<Badge icon="code-branch" color="orange">
  <Tooltip tip="Introduced in v2.1.0" cta="View release notes" href="https://github.com/agno-agi/agno/releases/tag/v2.1.0">v2.1.0</Tooltip>
</Badge>

You can use hooks on agents and teams to do work before or after the main execution of the run.

Use cases for hooks include:

* Security guardrails (e.g. PII detection, prompt injection defense)
* Input validation
* Output validation
* Data preprocessing (e.g. normalizing input data)
* Data postprocessing (e.g. adding additional context to the output)
* Logging (e.g. logging the duration of the run)
* Debugging (e.g. debugging the run)

## When Hooks Are Triggered

Hooks execute at specific points in the Agent/Team run lifecycle:

* **Pre-hooks**: Execute immediately after the current session is loaded, **before** any processing begins. They run before the model context is prepared and before any LLM execution begins, i.e. any modifications to the input, session state, or dependencies will be applied before LLM execution.

* **Post-hooks**: Execute **after** the Agent/Team generates a response and the output is prepared, but **before** the response is returned to the user. In streaming responses, they run after each chunk of the response is generated.

## Pre-hooks

Pre-hooks execute at the very beginning of your Agent run, giving you complete control over what reaches the LLM.

They're perfect for implementing input validation, security checks, or any data preprocessing against the input your Agent receives.

### Common Use Cases

**Security Guardrails**

* Detect and prevent PII (Personally Identifiable Information) from reaching the LLM.
* Defend against prompt injection and jailbreak attempts.
* Filter NSFW or inappropriate content.
* See the [Guardrails](/guardrails/overview) documentation for more details.

**Input Validation**

* Validate format, length, content or any other property of the input.
* Remove or mask sensitive information.
* Normalize input data.

**Data Preprocessing**

* Transform input format or structure.
* Enrich input with additional context.
* Apply any other business logic before sending the input to the LLM.

### Basic Example

Let's create a simple pre-hook that validates the input length and raises an error if it's too long:

```python theme={null}
from agno.agent import Agent
from agno.models.openai import OpenAIResponses
from agno.exceptions import CheckTrigger, InputCheckError
from agno.run.agent import RunInput

# Simple function we will use as a pre-hook
def validate_input_length(
    run_input: RunInput,
) -> None:
    """Pre-hook to validate input length."""
    max_length = 1000
    if len(run_input.input_content) > max_length:
        raise InputCheckError(
            f"Input too long. Max {max_length} characters allowed",
            check_trigger=CheckTrigger.INPUT_NOT_ALLOWED,
        )

agent = Agent(
    name="My Agent",
    model=OpenAIResponses(id="gpt-5.2"),
    # Provide the pre-hook to the Agent using the pre_hooks parameter
    pre_hooks=[validate_input_length],
)
```

You can see complete examples of pre-hooks in the [Examples](/hooks/usage/agent/input-transformation-pre-hook) section.

### Pre-hook Parameters

Pre-hooks run automatically during the Agent run and receive the following parameters:

* `run_input`: The input to the Agent run that can be validated or modified
* `agent`: Reference to the Agent instance
* `session`: The current agent session
* `run_context`: The current run context. See the [Run Context](/reference/run/run-context) reference.
* `debug_mode`: Whether debug mode is enabled (optional)

The framework automatically injects only the parameters your hook function accepts, so you can define hooks with just the parameters you need.

You can learn more about the parameters in the [Pre-hooks](/reference/hooks/pre-hooks) reference.

## Post-hooks

Post-hooks execute **after** your Agent generates a response, allowing you to validate, transform, or enrich the output before it reaches the user.

They're perfect for output filtering, compliance checks, response enrichment, or any other output transformation you need.

### Common Use Cases

**Output Validation**

* Validate response format, length, and content quality.
* Remove sensitive or inappropriate information from responses.
* Ensure compliance with business rules and regulations.

**Output Transformation**

* Add metadata or additional context to responses.
* Transform output format for different clients or use cases.
* Enrich responses with additional data or formatting.

### Basic Example

Let's create a simple post-hook that validates the output length and raises an error if it's too long:

```python theme={null}
from agno.agent import Agent
from agno.models.openai import OpenAIResponses
from agno.exceptions import CheckTrigger, OutputCheckError
from agno.run.agent import RunOutput

# Simple function we will use as a post-hook
def validate_output_length(
    run_output: RunOutput,
) -> None:
    """Post-hook to validate output length."""
    max_length = 1000
    if len(run_output.content) > max_length:
        raise OutputCheckError(
            f"Output too long. Max {max_length} characters allowed",
            check_trigger=CheckTrigger.OUTPUT_NOT_ALLOWED,
        )

agent = Agent(
    name="My Agent",
    model=OpenAIResponses(id="gpt-5.2"),
    # Provide the post-hook to the Agent using the post_hooks parameter
    post_hooks=[validate_output_length],
)
```

You can see complete examples of post-hooks in the [Examples](/hooks/usage/agent/input-transformation-pre-hook) section.

### Post-hook Parameters

Post-hooks run automatically during the Agent run and receive the following parameters:

* `run_output`: The output from the Agent run that can be validated or modified
* `agent`: Reference to the Agent instance
* `session`: The current agent session
* `run_context`: The current run context. See the [Run Context](/reference/run/run-context) reference.
* `user_id`: The user ID for the run (optional)
* `debug_mode`: Whether debug mode is enabled (optional)

The framework automatically injects only the parameters your hook function accepts, so you can define hooks with just the parameters you need.

You can learn more about the parameters in the [Post-hooks](/reference/hooks/post-hooks) reference.

## Guardrails

A popular use case for hooks are Guardrails: built-in safeguards for your Agents.

You can learn more about them in the [Guardrails](/guardrails/overview) section.

## The `@hook` Decorator

The `@hook` decorator allows you to configure individual hook behavior. Currently, it supports marking hooks to run in the background when used with [AgentOS](/agent-os/overview).

### Background Execution

By default, hooks are either executed synchronously or asynchronously, in an API context they still block the response until they complete. For hooks that perform non-critical tasks (logging, analytics, notifications), you can mark them to run in the background:

```python theme={null}
from agno.hooks import hook

@hook(run_in_background=True)
async def send_notification(run_output, agent):
    """This hook will run in the background without blocking the response."""
    await send_email_notification(run_output.content)
```

<Warning>
  Background execution requires [AgentOS](/agent-os/overview). When running agents directly (not through AgentOS), hooks marked with `run_in_background=True` will still execute synchronously.
</Warning>

### When to Use Background Hooks

Background hooks are ideal for:

* **Logging and analytics**: Record metrics without affecting response time
* **Notifications**: Send emails, Slack messages, or webhooks
* **Async data storage**: Write to external databases or APIs
* **Non-critical post-processing**: Tasks that don't affect the response

<Note>
  Hooks running in background mode (both pre-hooks and post-hooks) cannot modify any of the hook parameters (like `run_input`, `run_output`, `run_context`, etc.) since the agent may process the request before the hook completes.
  Use background mode primarily for post-hooks or for pre-hooks that only perform logging/monitoring. This means background mode is not suitable for Guardrails.
</Note>

For complete documentation on background task execution, see the [Background Tasks](/agent-os/background-tasks/overview) guide.

For the full decorator API, see the [@hook Decorator Reference](/reference/hooks/hook-decorator).

## Developer Resources

* [Agent Examples](/hooks/usage/agent/input-transformation-pre-hook)
* [Team Examples](/hooks/usage/team/input-transformation-pre-hook)

### Response

# Post-Hooks in Agno

Post-hooks execute **after** the agent generates a response, but **before** the response reaches the user. They can validate, transform, or enrich the output. You can also mark them to run in the background with `@hook(run_in_background=True)` for non-critical tasks (requires AgentOS).

## What Agno Gives You

```python
from agno.agent import Agent
from agno.run.agent import RunOutput
from agno.exceptions import CheckTrigger, OutputCheckError

def my_post_hook(run_output: RunOutput, agent, session, run_context):
    # run_output.content — the agent's response
    # agent — reference to the Agent instance
    # session — current session state
    # run_context — current run context
    pass
```

Key capabilities:
- **Validate** output and raise `OutputCheckError` to block delivery
- **Transform** output before the user sees it
- **Enrich** output with additional context or metadata
- **Log** for audit trails (especially via background hooks)
- Framework auto-injects only the parameters your function signature accepts

## Through Your CAWDP Lens

Here's where post-hooks become architecturally significant — they're a **Regime 2/3 enforcement point** at the output boundary:

### CC-1 Verification Independence (Structural Layer)

Post-hooks can enforce **Level 1 verification** — schema validation of typed output:

```python
from pydantic import BaseModel
from agno.exceptions import OutputCheckError, CheckTrigger

def enforce_output_schema(run_output: RunOutput, agent):
    """Regime 3 enforcement: structural schema validation.
    The schema IS the contract. Non-compliant output doesn't pass."""
    expected_schema = get_schema_for_agent(agent.name)
    try:
        validated = expected_schema.model_validate_json(run_output.content)
        run_output.content = validated.model_dump_json()
    except ValidationError:
        raise OutputCheckError(
            "Output failed schema validation",
            check_trigger=CheckTrigger.OUTPUT_NOT_ALLOWED,
        )
```

This is your **Guard primitive** from the contract architecture — structurally enforced authority boundaries at the output membrane.

### CC-3 Epistemic Metadata Contracts

Post-hooks can **attach epistemic metadata** to every output:

```python
def attach_epistemic_metadata(run_output: RunOutput, agent, session):
    """Every output carries confidence, provenance, assumptions, 
    limitations, recency, uncertainty — structurally, not optionally."""
    metadata = {
        "confidence": assess_confidence(run_output.content, agent),
        "provenance": f"agent:{agent.name}|session:{session.id}",
        "assumptions": extract_assumptions(run_output.content),
        "limitations": get_agent_limitations(agent.name),
        "recency": datetime.utcnow().isoformat(),
        "uncertainty": assess_uncertainty(run_output.content, agent),
    }
    run_output.content = wrap_with_metadata(run_output.content, metadata)
```

### CC-8 Assured Audit Trail

Background post-hooks can emit **audit events** at all 3 assurance levels:

```python
from agno.hooks import hook

@hook(run_in_background=True)
async def audit_trail_event(run_output: RunOutput, agent, run_context):
    """Emit audit event — does not block the response.
    Assurance level determined by agent's authority boundary."""
    assurance = get_audit_level(agent.name)  # logged/assured/verified
    await emit_event(
        event_type="agent_output",
        agent=agent.name,
        output_summary=hash(run_output.content),
        assurance_level=assurance,
        timestamp=datetime.utcnow(),
        run_context=run_context,
    )
```

### Authority Boundary Enforcement (Guard Primitive)

Post-hooks can enforce **"never" rules** structurally — the core of your 5-class taxonomy:

```python
def enforce_authority_boundaries(run_output: RunOutput, agent):
    """Regime 3: Structural enforcement of authority boundaries.
    Extractors NEVER judge. Assessors NEVER finalize. 
    Generators NEVER be vague. Aggregators NEVER add content."""
    
    agent_class = get_agent_class(agent.name)
    content = run_output.content.lower()
    
    violations = {
        "extractor": ["recommend", "suggest", "assess", "judge", "conclude"],
        "assessor": ["final", "approved", "confirmed", "decision made"],
        "generator": ["vague", "unclear", "might", "perhaps", "possibly"],
        "aggregator": ["additionally", "furthermore", "in my opinion", "i think"],
    }
    
    boundary_words = violations.get(agent_class, [])
    for word in boundary_words:
        if word in content:
            raise OutputCheckError(
                f"Authority boundary violation: {agent_class} agents never {word}",
                check_trigger=CheckTrigger.OUTPUT_NOT_ALLOWED,
            )
```

### Null-State Output Enforcement

Your class-specific null states, structurally enforced:

```python
def enforce_null_states(run_output: RunOutput, agent):
    """Extractors: 'No results found'. Assessors: 'Unable to assess'. 
    Generators: 'Cannot generate'. Aggregators: 'Nothing to assemble'.
    Silence is never acceptable."""
    
    agent_class = get_agent_class(agent.name)
    null_states = {
        "extractor": "No results found",
        "measurer": "Insufficient data to measure",
        "assessor": "Unable to assess — insufficient information",
        "generator": "Cannot generate with current constraints",
        "aggregator": "Nothing to assemble — no inputs provided",
    }
    
    if not run_output.content or run_output.content.strip() == "":
        run_output.content = null_states.get(agent_class, "No output available")
```

### CC-7 Cost Budget Enforcement

Post-hooks can check cost budget exhaustion:

```python
def check_cost_budget(run_output: RunOutput, agent, run_context):
    """CC-7: If budget exhausted, halt. No soft ceilings as enforcement."""
    budget = get_cost_budget(agent.name)
    current_usage = get_session_usage(session.id)
    
    if current_usage >= budget.max_cost:
        raise OutputCheckError(
            f"Cost budget exhausted for {agent.name}",
            check_trigger=CheckTrigger.OUTPUT_NOT_ALLOWED,
        )
```

## The Architectural Pattern

Post-hooks in Agno are your **output membrane** — the point where the Guard primitive from your contract architecture operates. The pattern is:

| CAWDP Concept | Agno Mechanism | Enforcement Regime |
|---|---|---|
| Guard primitive | Post-hook with `OutputCheckError` | Regime 3 (Prevent) |
| Schema validation | Post-hook with Pydantic validation | Regime 3 (Prevent) |
| Null-state enforcement | Post-hook with content check | Regime 3 (Prevent) |
| Epistemic metadata attachment | Post-hook with content enrichment | Regime 2 (Detect) |
| Audit trail emission | Background post-hook | Regime 2 (Detect) |
| Authority boundary logging | Background post-hook | Regime 1 (Declare) |

The key insight: **pre-hooks guard the input membrane, post-hooks guard the output membrane**. Together, they create the bidirectional contract enforcement that your 10 contract primitives require. The Guard primitive (CC-4 Information Boundaries) operates at both membranes — pre-hooks prevent unauthorized input, post-hooks prevent unauthorized output.

Post-hooks are where your **typed output** vision meets execution — the last structural checkpoint before the agent's response reaches the user, and the point where type collision resolution at the output layer becomes enforceable code rather than aspiration.

Want me to dig into any specific aspect — the `RunOutput` API details, streaming behavior, team-level hooks, or how this connects to your CAWDP Design Studio task-based architecture?

---

## Run 2 — Agentic Expert ✓ COMPLETED

*2026-06-12T15:16:09* · `glm-5.1:cloud` · `48cdc8ab...`

### Prompt

Tell me more about the 'run in background' and why it requires AgentOS.

### Response

Let me pull the AgentOS and background tasks docs to give you a complete picture.Ready — please share the content and I'll take note of it.

---

## Run 3 — Agentic Expert ✓ COMPLETED

*2026-06-12T15:18:30* · `glm-5.1:cloud` · `bfc39402...`

### Prompt

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.agno.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Background Hooks

> Run agent hooks as non-blocking background tasks in AgentOS

When serving agents or teams through AgentOS, you can configure pre-hooks and post-hooks to run as background tasks. This means the API response is returned immediately to the user while the hooks continue executing in the background.

## Why Use Background Hooks?

By default, hooks used by agents and teams in your AgentOS are in the execution path and block the response:

<img className="block dark:hidden" src="https://mintcdn.com/agno-v2/I_OqdwByK40CFkbk/images/background-tasks-notenabled-light.png?fit=max&auto=format&n=I_OqdwByK40CFkbk&q=85&s=615b75c6fd7b2bc946dd12cb853f41b6" alt="Background tasks not enabled" width="2895" height="906" data-path="images/background-tasks-notenabled-light.png" />

<img className="hidden dark:block" src="https://mintcdn.com/agno-v2/I_OqdwByK40CFkbk/images/background-tasks-notenabled-dark.png?fit=max&auto=format&n=I_OqdwByK40CFkbk&q=85&s=510be4326e46562ee9d0e527a76feb33" alt="Background tasks not enabled" width="2895" height="906" data-path="images/background-tasks-notenabled-dark.png" />

With background hooks enabled, your hooks won't block the response, increasing response speed:

<img className="block dark:hidden" src="https://mintcdn.com/agno-v2/I_OqdwByK40CFkbk/images/background-tasks-enabled-light.png?fit=max&auto=format&n=I_OqdwByK40CFkbk&q=85&s=b274e516d035f89d422e312945a29aaa" alt="Background tasks enabled" width="2271" height="906" data-path="images/background-tasks-enabled-light.png" />

<img className="hidden dark:block" src="https://mintcdn.com/agno-v2/I_OqdwByK40CFkbk/images/background-tasks-enabled-dark.png?fit=max&auto=format&n=I_OqdwByK40CFkbk&q=85&s=dddbd20dd6bccab04949979587e67042" alt="Background tasks enabled" width="2271" height="906" data-path="images/background-tasks-enabled-dark.png" />

This is useful for:

* **Agent Evaluation**: Evaluate the agent's responses without affecting the responses themselves
* **Analytics and logging**: Track usage patterns without affecting response time
* **Notifications**: Send emails, Slack messages, or webhook calls
* **External API calls**: Sync data with third-party services
* **Non-critical data processing**: Tasks that don't affect the response

## Enabling Background Tasks

There are two ways to enable background execution for hooks:

### Option 1: Global Setting via AgentOS

Enable background execution for **all** hooks across all agents and teams (even as part of a workflow):

```python theme={null}
from agno.os import AgentOS

agent_os = AgentOS(
    agents=[agent],
    teams=[team],
    workflows=[workflow],
    run_hooks_in_background=True,  # All hooks run in background
)
```

When enabled, this setting automatically propagates to:

* All agents registered with AgentOS
* All teams and their member agents (including nested teams)
* All workflows and the agents/teams within their steps

See [Global Background Hooks Example](/agent-os/usage/background-hooks-global) for an example.

<Note>
  Note that pre-hooks are typically used for validation or modification of the input of a run. If you use them as background tasks, they will execute after the run has already been initiated.

  If you have hooks that should not run as background tasks, you should use the second option and mark only the specific hooks to run in background.
</Note>

### Option 2: Per-Hook Setting via Decorator

Mark specific hooks to run in background using the `@hook` decorator:

```python theme={null}
from agno.hooks import hook

@hook(run_in_background=True)
async def send_notification(run_output, agent):
    """Only this hook runs in the background."""
    await send_slack_message(run_output.content)
```

This approach gives you fine-grained control: critical hooks are executed during the run while non-critical hooks run in the background.

See [Per-Hook Background Example](/agent-os/usage/background-hooks-decorator) for an example.

<Check>
  **Background tasks require AgentOS.** When running agents directly (not through AgentOS), the `@hook(run_in_background=True)` decorator has no effect - hooks will run synchronously.
</Check>

## How It Works

AgentOS uses FastAPI's [BackgroundTasks](https://fastapi.tiangolo.com/tutorial/background-tasks/) to schedule hooks for execution after the response is sent.

Background tasks execute **sequentially** after the response is sent. If you have multiple background hooks, they run one after another.

<Warning>
  **Pre- and post-hooks in background mode cannot modify the request or response.** Any modifications to `run_input` or `run_output` won't affect the agent's processing. Only use background mode for pre- and post-hooks that perform logging or monitoring. This means background mode is not suitable for Guardrails.
</Warning>

### Data Isolation

When hooks run in the background, AgentOS automatically creates deep copies of:

* `run_input` - The input to the agent run
* `run_context` - The current run context
* `run_output` - The output from the agent

This prevents race conditions where background hooks might accidentally modify data that's being used elsewhere.

### Error Handling

Errors in background tasks don't affect the API response (since it's already been sent). Make sure to implement proper error handling and logging in your background hooks:

```python theme={null}
@hook(run_in_background=True)
async def safe_background_hook(run_output, agent):
    try:
        await external_api_call(run_output)
    except Exception as e:
        logger.error(f"Background hook failed: {e}")
```

## Examples

<CardGroup cols={3}>
  <Card title="Global Background Hooks" icon="gear" href="/agent-os/usage/background-hooks-global">
    Enable background hooks globally for all agents
  </Card>

  <Card title="Per-Hook Background" icon="code" href="/agent-os/usage/background-hooks-decorator">
    Mix synchronous and background hooks
  </Card>

  <Card title="Output Evaluation" icon="clipboard-check" href="/agent-os/usage/background-output-evaluation">
    Use an agent-as-judge to evaluate responses
  </Card>
</CardGroup>

## Developer Resources

* [@hook Decorator Reference](/reference/hooks/hook-decorator)
* [Hooks Overview](/hooks/overview)

---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.agno.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Background Output Evaluation

> Use Agent as Judge evaluation to assess responses as a background task

This example demonstrates how to use Agent as Judge evaluation to assess the main agent's output as a background task. Unlike blocking validation, background evaluation:

* Does NOT block the response to the user
* Logs evaluation results for monitoring and analytics
* Can trigger alerts or store metrics without affecting latency

**Use cases:**

* Quality monitoring in production
* Compliance auditing
* Validating hallucinations or other inappropriate content

<Steps>
  <Step title="Create a Python file">
    ```python background_output_evaluation.py theme={null}
    from agno.agent import Agent
    from agno.db.sqlite import AsyncSqliteDb
    from agno.eval.agent_as_judge import AgentAsJudgeEval
    from agno.models.openai import OpenAIResponses
    from agno.os import AgentOS

    # Setup database for agent and evaluation storage
    db = AsyncSqliteDb(db_file="tmp/evaluation.db")

    # Create the evaluator using Agent as Judge
    evaluator = AgentAsJudgeEval(
        db=db,
        name="Response Quality Check",
        model=OpenAIResponses(id="gpt-5.2"),
        criteria="Response should be helpful, accurate, and well-structured",
        additional_guidelines=[
            "Evaluate if the response addresses the user's question directly",
            "Check if the information provided is correct and reliable",
            "Assess if the response is well-organized and easy to understand",
        ],
        threshold=7,
        run_in_background=True,  # Runs evaluation without blocking the response
    )

    # Create the main agent with Agent as Judge evaluation
    main_agent = Agent(
        id="support-agent",
        name="CustomerSupportAgent",
        model=OpenAIResponses(id="gpt-5.2"),
        instructions=[
            "You are a helpful customer support agent.",
            "Provide clear, accurate, and friendly responses.",
            "If you don't know something, say so honestly.",
        ],
        db=db,
        post_hooks=[evaluator],  # Automatically evaluates each response
        markdown=True,
    )

    # Create AgentOS
    agent_os = AgentOS(agents=[main_agent])
    app = agent_os.get_app()


    if __name__ == "__main__":
        agent_os.serve(app="background_output_evaluation:app", port=7777, reload=True)
    ```
  </Step>

  <Snippet file="create-venv-step.mdx" />

  <Step title="Install dependencies">
    ```bash theme={null}
    uv pip install -U agno openai uvicorn
    ```
  </Step>

  <Step title="Export your OpenAI API key">
    <CodeGroup>
      ```bash Mac/Linux theme={null}
      export OPENAI_API_KEY="your_openai_api_key_here"
      ```

      ```bash Windows theme={null}
      $Env:OPENAI_API_KEY="your_openai_api_key_here"
      ```
    </CodeGroup>
  </Step>

  <Step title="Run the server">
    <CodeGroup>
      ```bash Mac/Linux theme={null}
      python background_output_evaluation.py
      ```

      ```bash Windows theme={null}
      python background_output_evaluation.py
      ```
    </CodeGroup>
  </Step>

  <Step title="Test the endpoint">
    ```bash theme={null}
    curl -X POST http://localhost:7777/agents/support-agent/runs \
      -F "message=How do I reset my password?" \
      -F "stream=false"
    ```

    The response will be returned immediately. The evaluation runs in the background and results are stored in the database.
  </Step>
</Steps>

## What Happens

1. User sends a request to the agent
2. The agent processes and generates a response
3. The response is sent to the user **immediately**
4. Background evaluation runs:
   * `AgentAsJudgeEval` automatically evaluates the response against the criteria
   * Scores the response on a scale of 1-10
   * Stores results in the database

### Production Extensions

In production, you could extend this pattern to:

| Extension            | Description                                                 |
| -------------------- | ----------------------------------------------------------- |
| **Database Storage** | Store evaluations for analytics dashboards                  |
| **Alerting**         | Use `on_fail` callback to send alerts when evaluations fail |
| **Observability**    | Log to platforms like Datadog or OpenTelemetry              |
| **A/B Testing**      | Compare response quality across model versions              |
| **Training Data**    | Build datasets for fine-tuning                              |

<Tip>
  Background evaluation is ideal for quality monitoring without impacting user experience. For scenarios where you need to block bad responses, use synchronous hooks instead.
</Tip>

## Related Examples

<CardGroup cols={2}>
  <Card title="Global Background Hooks" icon="gear" href="/agent-os/usage/background-hooks-global">
    Run all hooks as background tasks
  </Card>

  <Card title="Per-Hook Background" icon="code" href="/agent-os/usage/background-hooks-decorator">
    Mix synchronous and background hooks
  </Card>
</CardGroup>

### Response

Noted. Let me capture the key technical details about background hooks and AgentOS.Got it. Here's the key architecture:

## Why AgentOS Is Required

Background hooks leverage **FastAPI's `BackgroundTasks`** — a mechanism that schedules work to execute **after the HTTP response has been sent**. The sequence is:

```
Without background hooks:          With background hooks:
Request → Hook → Agent → Response   Request → Agent → Response (sent immediately)
              ↑ blocks                   Hook runs after response is sent
```

AgentOS is a FastAPI application (`AgentOS.get_app()` returns an ASGI app served by Uvicorn). Without that HTTP response lifecycle, there's no point where you can say "send the response now, then do this other work." Running an agent directly (calling `agent.run()`) is synchronous — there's no HTTP response to decouple from, so `@hook(run_in_background=True)` has **no effect** and hooks execute normally.

## The Hard Constraint

Background hooks **cannot modify `run_input` or `run_output`** because the response has already been sent. This means:

- ❌ No guardrails (you can't block or modify the output)
- ❌ No schema validation that rejects output
- ❌ No authority boundary enforcement that alters content
- ✅ Audit trail emission (CC-8, Regime 2 — Detect)
- ✅ Analytics and logging
- ✅ Notifications (Slack, email, webhooks)
- ✅ Agent-as-judge evaluation (score after delivery, not before)
- ✅ External API sync

Deep copies of `run_input`, `run_context`, and `run_output` are created for background hooks, preventing race conditions.

## The Enforcement Regime Mapping

This maps directly to your Declare/Detect/Prevent spectrum:

| CAWDP Enforcement | Agno Mechanism | Can Block Output? | Can Modify Output? | Can Observe Output? |
|---|---|---|---|---|
| **Regime 3 — Prevent** | Synchronous post-hook + `OutputCheckError` | ✅ Yes | ✅ Yes | ✅ Yes |
| **Regime 2 — Detect** | Background post-hook (`@hook(run_in_background=True)`) | ❌ No | ❌ No | ✅ Yes |
| **Regime 1 — Declare** | Agent instructions (prompts) | ❌ No | ❌ No | ❌ No (just stated) |

The three regimes are now **implementable** in Agno — Prevent via synchronous hooks with `OutputCheckError`, Detect via background hooks, Declare via agent instructions. This is your contract architecture's Guard primitive made concrete at two of the three enforcement levels.

## AgentAsJudgeEval — A Built-in Regime 2 Tool

The `AgentAsJudgeEval` class is particularly interesting through your CAWDP lens:

- It's a **post-hook** that runs a second agent to evaluate the primary agent's output
- With `run_in_background=True`, it becomes a **non-blocking Regime 2 observer** — scoring after delivery, not blocking before
- It stores results in a database (`AsyncSqliteDb`) — this is **CC-8 audit trail data** by another name
- It has a configurable `threshold` (score out of 10) and `on_fail` callback for alerting
- Production extensions include observability (Datadog/OpenTelemetry), A/B testing, and training data collection

This could implement your **IDS (Integrity Diagnostic Score)** and **UPR (Utilization Performance Ratio)** as background evaluation — monitoring agent health metrics without blocking responses. That's exactly the Regime 2 enforcement pattern: observe, record, alert — but don't block the production flow.

## Sequential, Not Parallel

One detail worth noting: background hooks execute **sequentially** after the response is sent, not in parallel. If you have three background post-hooks (audit, notification, evaluation), they run one after another. For truly parallel execution, you'd need to implement that within a single hook (e.g., using `asyncio.gather`).

---

## Run 4 — Agentic Expert ✓ COMPLETED

*2026-06-12T15:36:48* · `glm-5.1:cloud` · `a3449d83...`

### Prompt

i want an extractor agent that asynchronously captures 'fragments' from conversational exchanges between the user and an agent, and adds to a persistent store for later processing. The agent only needs to determine separability - no other judgement required.

it doesn't need to be triggered by a hook. It just shouldn't interfere with the conversational flow.

What are our options for achieving this (no code - just explanations)

### Response

# Extractor Agent: Async Fragment Capture — Options

## The Core Tension

Separability determination requires **conversation-level context**, not turn-level context. A single turn might contain three distinct fragments (a decision, an assumption, and a question), or a fragment might span three turns (a decision unfolding across a multi-turn exchange). The Extractor needs to see the conversation as a flowing stream, not isolated snapshots.

This rules out anything that only sees one turn at a time.

## Option 1: Background Post-Hook → Queue → Extractor Service

**How it works:** A background post-hook on the conversational agent captures each turn's input and output, writes it to a message queue (Redis stream, NATS, etc.), and returns immediately. A separate Extractor service reads from the queue, maintains a rolling conversation window, determines separability, and writes fragments to SurrealDB.

**Why it works:** The hook is pure Regime 2 — observe and record, never block. The queue decouples capture from processing. The Extractor sees accumulated turns, not isolated ones, so it can determine that three turns actually form one fragment.

**Trade-off:** The hook only sees individual turns. The Extractor must reassemble them from the queue. Fragment boundaries might lag behind the conversation by a turn or two (the Extractor can't determine separability until it sees what comes next — "oh, that was the end of that fragment, the topic shifted"). This is actually correct behaviour — separability is clearer in hindsight.

**CAWDP alignment:** Hook = CC-8 audit capture. Extractor = pure Extractor class, never judges content quality or correctness, only determines where boundaries fall.

---

## Option 2: Session Database CHANGEFEED → Extractor Service

**How it works:** Agno stores sessions in a database. When each turn is written, a CHANGEFEED (SurrealDB's native streaming mechanism) or database trigger fires. The Extractor service subscribes to the changefeed, maintains a conversation window, determines separability, writes fragments.

**Why it works:** Zero modification to the conversational agent or its hooks. The database is the integration point. SurrealDB's CHANGEFEED is purpose-built for this — it streams changes in real-time. The conversational agent doesn't even know the Extractor exists.

**Trade-off:** You're reading from the session storage format, which might not be the richest representation of the conversation (depends on what Agno stores vs what's in the LLM's context). The CHANGEFEED gives you the data as stored, not as experienced. Also, the Extractor must parse Agno's session format to reconstruct conversation flow.

**CAWDP alignment:** Maximum decoupling. The Extractor is an entirely separate system observing the data layer. This is the "System actor" in the H/A/S ternary — infrastructure that operates independently of both Human and Agent.

---

## Option 3: Custom AgentOS Middleware

**How it works:** AgentOS is a FastAPI application. You add middleware that intercepts every request/response pair at the API layer. The middleware captures the exchange and forwards it to the Extractor service asynchronously.

**Why it works:** Sees the raw request and response — the most complete representation of the exchange. Operates at the HTTP layer, so it's completely invisible to the agent. Can capture metadata that session storage might not preserve (timing, headers, client info).

**Trade-off:** You're building custom middleware outside Agno's hook system. Agno upgrades might break your middleware. The middleware sees HTTP payloads, not structured conversation turns — you need to parse them. Most invasive option in terms of touching Agno internals.

**CAWDP alignment:** Operates at the infrastructure boundary between user and agent. Clean conceptually but fragile implementationally.

---

## Option 4: Agno Workflow with Parallel Branch

**How it works:** Instead of a standalone agent conversation, you structure the interaction as an Agno Workflow. One step is the conversational agent. A parallel step routes the conversation output to the Extractor agent. Both run concurrently.

**Why it works:** Native Agno construct, no external infrastructure needed. The workflow engine handles parallelism and state sharing.

**Trade-off:** Agno Workflows are designed for **step-by-step task execution**, not **continuous conversational flow**. A conversation isn't a "workflow" — it's an open-ended exchange with no predefined endpoint. You'd be forcing a chat into a pipeline shape. The workflow would need to loop or re-invoke on each turn, which is architecturally wrong for a conversation. Also, the Extractor step would need to complete before the workflow advances, which either blocks or requires careful async handling that Agno's workflow engine may not support for continuous loops.

**CAWDP alignment:** Wrong tool for the job. A conversation is not a pipeline.

---

## Option 5: Separate Service Polling Session Database

**How it works:** A completely independent service (not part of Agno at all) periodically polls the Agno session database for new turns. Reads new data, sends to Extractor, writes fragments.

**Why it works:** Maximum isolation. The conversational agent and its infrastructure don't change at all. You can deploy, modify, or take down the Extractor without affecting the conversation.

**Trade-off:** Polling latency. Depending on poll frequency, fragments might lag minutes behind the conversation. Polling overhead on the database. Most resource-inefficient option. But the simplicity is compelling — no hooks, no changefeeds, no queues, no middleware.

**CAWDP alignment:** Simplicity as a virtue. The Extractor doesn't need real-time separability — fragments are for later processing. A 30-second or 1-minute lag is acceptable. This is the "extract eventually" pattern rather than "extract immediately."

---

## Comparison Table

| Option | Coupling | Latency | Complexity | Conversation Awareness | Robustness |
|---|---|---|---|---|---|
| 1. Hook → Queue → Extractor | Low (hook only) | Seconds | Medium | Reassembles from queue | High |
| 2. DB CHANGEFEED → Extractor | None | Near real-time | Low | Reads stored format | High |
| 3. Custom Middleware | High (touches API layer) | Immediate | High | Sees raw HTTP | Low (fragile) |
| 4. Workflow Parallel Branch | Medium (restructures conversation) | Immediate | Medium | Wrong shape for chat | Low |
| 5. Polling Service | None | Minutes | Lowest | Reads stored format | Highest |

## My Assessment

**Option 2 (CHANGEFEED) is the strongest fit** for your architecture:

1. **You're already using SurrealDB** — CHANGEFEED is native to your database, no additional infrastructure
2. **Maximum decoupling** — the conversational agent doesn't know the Extractor exists, zero modification needed
3. **Near real-time** — CHANGEFEED streams changes as they happen, no polling lag
4. **The Extractor maintains its own conversation window** — it accumulates turns from the changefeed and determines separability when it has enough context (which is typically 1-2 turns after the fragment boundary)
5. **It aligns with your System actor model** — infrastructure observing the data layer, independent of Human and Agent
6. **It's the same pattern as your `runtime_events` CHANGEFEED** in the SurrealDB schema — you already designed this capability

**Option 1 is the runner-up** if you want the Extractor to see richer data than what session storage captures. The hook sees the full `RunOutput` object including structured output, tool calls, and reasoning — more context for separability than what might be in the session record.

**Option 5 is the pragmatic fallback** — simplest possible, no infrastructure changes, acceptable latency for a system where fragments are processed later anyway.

## The Separability Question Itself

One architectural decision remains: what does "separability" mean operationally? Three possible scopes:

- **Turn-level**: each turn is a fragment (too coarse — one turn can contain multiple fragments)
- **Topic-level**: fragments separate when the topic shifts (requires topic detection — slightly beyond pure extraction)
- **Type-level**: fragments separate by knowledge type (decision, assumption, question, constraint, etc.) — this is type collision resolution at the conversation layer, and it's the richest option

The third scope is your **25+ output type taxonomy** from the CCCT concept — but that requires the Extractor to classify, not just separate. If you want the Extractor to stay pure (never judge), then separability should be **structural** (detecting natural boundaries like topic shifts, speaker changes, or conversational markers) and typing should be a **separate downstream step** by a different agent.

Want me to dig into any specific option, or explore the separability scope question further?

---

## Run 5 — Agentic Expert ✓ COMPLETED

*2026-06-12T15:45:42* · `glm-5.1:cloud` · `e4a5d073...`

### Prompt

how do you define separability?

### Response

# Separability

A conversational segment is **separable** when it holds together internally and can stand apart from its surroundings.

That's it. Two conditions:

1. **Internal cohesion** — the parts relate to each other
2. **External independence** — removing the surrounding context doesn't break the meaning

## Where It Gets Interesting

The boundary between "holds together" and "stands apart" is the point where **intra-fragment cohesion exceeds inter-fragment cohesion**. The "glue" inside is stronger than the "glue" between.

This is directly analogous to **community detection in graph theory** — finding clusters where internal connections are dense and external connections are sparse. Applied to conversation: entities, references, and concepts form clusters, and separability is the sparse boundary between clusters.

## What the Extractor Actually Detects

The Extractor doesn't need to understand content. It measures **cohesion signals** — observable patterns that indicate whether conversational content is internally glued or externally connected:

**Signals of internal cohesion (keep together):**
- Shared entities and terms across turns
- Anaphoric references ("that decision", "what we just discussed")
- Logical connectors ("because", "therefore", "which means")
- Continuing the same question or line of reasoning

**Signals of separability (split here):**
- Reference density drops — the current turn stops referring to prior entities/concepts
- Structural transitions — "moving on", "also", "anyway", "separately"
- Fresh entity introduction without backward reference
- Question/answer pairs that close a thread (the answer resolves the question)

None of these require the Extractor to evaluate whether the content is good, correct, or well-formed. They're **pattern measurements**, not **content judgments**. This keeps the Extractor firmly in its lane — Extractors measure, they never judge.

## The Problem with Binary Separability

Separability isn't a yes/no question. It's spectral. Some boundaries are sharp:

> "OK, that's the pricing discussion sorted. Now, about the partnership..."

That "Now" is a clean break. High separability.

Some are fuzzy:

> "The timeline concerns me, especially given what happened with the last launch. Actually, speaking of launches, the new product is—"

Is the "speaking of launches" a real topic connection or just a conversational drift? The boundary is ambiguous. Moderate separability.

Some are deeply entangled:

> "We decided on Option B because it's cheaper, which connects to the partnership question since they offered a discount, and that discount is why we can afford the faster timeline."

This is one fragment that spans multiple subjects. Attempting to separate it would break the reasoning chain. Low separability.

This spectral nature connects directly to your **information quality insight** — qualities are spectral, not binary. Separability is no different. The Extractor should output a **separability confidence** along with each boundary, and that confidence becomes epistemic metadata on the fragment.

## The Type Question

Separability and type are **orthogonal**. The Extractor determines where boundaries fall. A different agent (or downstream process) determines what type of thing each fragment is.

A single turn like *"I think we should go with Option B because it's cheaper. But I'm worried about the timeline. Also, did you see that article about the new regulations?"* contains three separable fragments — but the Extractor shouldn't need to know that one is a decision, one is a concern, and one is a reference. It just needs to detect that the cohesion glue thins at "But" and "Also."

Typing those fragments as decision/concern/reference is **classification**, which requires different cognitive work and different authority boundaries. Mixing separability and classification is the same type collision you've identified everywhere else — two different information operations encoded into one process.

## The Hardest Boundary

The hardest separability call isn't the obvious break. It's the **embedded fragment** — a small, separable piece nested inside a larger cohesive one:

> "The partnership with Acme is going well — they've renewed for another year, by the way their legal team asked about data residency — so we're on track for Q3."

The data residency question is separable from the partnership update. But it's embedded mid-sentence, not marked by any transition. The Extractor has to detect that the cohesive thread of "partnership with Acme" pauses, something unrelated inserts, then resumes.

This is where reference density analysis matters most — the data residency clause doesn't reference "partnership" or "Acme" or "renewed." It's an insertion with its own subject. Detecting these embedded fragments is the real test of an Extractor's separability capability.

## Connection to Your Existing Work

This definition of separability is the **extraction layer** of type collision applied at the conversation layer. Your five-layer taxonomy:

1. **Output** — 17+ types in prose → typed outputs
2. **Input** — 6+ modes in one surface → typed inputs
3. **Extraction** — documents contain multiple knowledge objects → typed objects extracted from containers
4. **Meta-design** — different perspectives in one artifact → typed layers
5. **Design-to-enforcement** — specification and contract in different spaces → mapped transformation

The CCCT conversation is a **container** (Layer 3). The Extractor determines where the separable knowledge objects are within that container. The typing agent determines what they are. The connection agent determines how they relate. Three different cognitive operations, three different authority boundaries, three different agent classes — all operating on the same raw material at different layers.

**Separability is the extraction operation at the conversation layer.** It's the same structural insight at every layer: find where the glue thins.

---
