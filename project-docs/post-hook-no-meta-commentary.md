# Post-Hook Design: `validate_no_meta_commentary()`

**Status:** Design only — not implemented. Implementation deferred until the
ThinkingPartner agent is registered in `app/main.py`.

## Purpose

Enforce Delivery Rule 1 ("capabilities are invisible until they produce value")
as a hard constraint on ThinkingPartner agent output. The rule is currently
advisory (in the skill and instructions); this post-hook makes it mechanical.

## Contract

### Signature

```python
def validate_no_meta_commentary(run_output: RunOutput) -> None
```

Lives in `app/guardrails.py` alongside `validate_citations_from_tools` and
`make_file_path_validator`. Plain function in `post_hooks` (not a
`BaseGuardrail` subclass) — consistent with the existing output-validation
pattern.

### Detection pattern

Regex scan of `str(run_output.content)` for meta-commentary phrases at
sentence boundaries:

- "I notice"
- "Would you like"
- "It might be worth"
- "Based on your previous"
- "As a thinking partner"
- "I'm surfacing"
- "I should mention"
- "It's worth pointing out"
- "An alternative framing could be" (when appended, not structurally embedded)

### Failure action

Raise `OutputCheckError` with `check_trigger=CheckTrigger.OUTPUT_NOT_ALLOWED`
and a message listing the detected phrases.

### False-positive mitigation

Phrases like "I notice" can appear in legitimate direct answers (e.g., quoting
the user). Mitigation: only flag when the phrase appears at the start of a
sentence or after a sentence boundary (`.`, `!`, `?`, newline), not mid-quote
or inside backtick-quoted text.

**Known limitation:** sentence-boundary detection won't catch every edge case.
If the false-positive rate is unacceptable in practice, escalate to an
LLM-as-judge post-hook (more accurate, higher latency/cost).

## Wiring

When the ThinkingPartner agent is registered, add to its constructor:

```python
from app.guardrails import validate_no_meta_commentary

thinking_partner = Agent(
    ...
    post_hooks=[validate_no_meta_commentary],
)
```

Not wired now — no ThinkingPartner agent is registered in `app/main.py`.

## Future tests

Add to `tests/test_guardrails.py`:

- `test_validate_no_meta_commentary_detects_violations` — content with
  "I notice..." at sentence start raises `OutputCheckError`.
- `test_validate_no_meta_commentary_passes_clean_output` — content with no
  meta-commentary phrases passes without raising.
- `test_validate_no_meta_commentary_ignores_quoted_text` — "I notice"
  inside backticks or a quoted user message does not raise.
