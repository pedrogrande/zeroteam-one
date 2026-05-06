"""
Run Eval Cases
==============

    python -m evals                # run all cases
    python -m evals --case <name>  # run one case

Each case runs the agent via agno's ``AccuracyEval`` (when
``expected_output`` is set) and ``ReliabilityEval`` (when
``expected_tool_calls`` is set). Both log to Postgres through
``eval_db`` — connect your AgentOS at os.agno.com to see history.

Exit 0 on all-pass, non-zero on any failure or error.
"""

import asyncio
from dataclasses import dataclass

import typer
from agno.eval import AccuracyEval, ReliabilityEval
from rich.console import Console
from rich.table import Table

from evals.cases import CASES, Case, eval_db

app = typer.Typer(add_completion=False, no_args_is_help=False, pretty_exceptions_show_locals=False)
console = Console()


@dataclass
class CaseOutcome:
    name: str
    accuracy_passed: bool | None = None
    accuracy_score: float | None = None
    reliability_passed: bool | None = None
    error: str | None = None

    @property
    def passed(self) -> bool:
        if self.error:
            return False
        checks = [c for c in (self.accuracy_passed, self.reliability_passed) if c is not None]
        return bool(checks) and all(checks)


def _run_accuracy(case: Case) -> tuple[bool | None, float | None, str | None]:
    if case.expected_output is None:
        return None, None, None
    try:
        # arun() is required: workspace context tools are async-only.
        result = asyncio.run(
            AccuracyEval(
                name=case.name,
                agent=case.agent,
                input=case.input,
                expected_output=case.expected_output,
                db=eval_db,
            ).arun(print_summary=False, print_results=True)
        )
    except Exception as exc:
        return False, None, f"accuracy: {type(exc).__name__}: {exc}"
    if result is None or not result.results:
        return False, None, "accuracy: judge returned no result"
    score = float(result.avg_score)
    return score >= case.accuracy_threshold, score, None


def _run_reliability(case: Case) -> tuple[bool | None, str | None]:
    if case.expected_tool_calls is None:
        return None, None
    try:
        response = asyncio.run(case.agent.arun(input=case.input, stream=False))
        result = ReliabilityEval(
            name=case.name,
            agent_response=response,
            expected_tool_calls=list(case.expected_tool_calls),
            allow_additional_tool_calls=case.allow_additional_tool_calls,
            db=eval_db,
        ).run(print_results=True)
    except Exception as exc:
        return False, f"reliability: {type(exc).__name__}: {exc}"
    if result is None:
        return False, "reliability: returned no result"
    return result.eval_status == "PASSED", None


def run_case(case: Case) -> CaseOutcome:
    acc_passed, acc_score, acc_err = _run_accuracy(case)
    rel_passed, rel_err = _run_reliability(case)
    err = "; ".join(e for e in (acc_err, rel_err) if e) or None
    return CaseOutcome(
        name=case.name,
        accuracy_passed=acc_passed,
        accuracy_score=acc_score,
        reliability_passed=rel_passed,
        error=err,
    )


def _accuracy_cell(o: CaseOutcome) -> str:
    if o.accuracy_passed is None:
        return "[dim]—[/dim]"
    score = f"{o.accuracy_score:.1f}/10" if o.accuracy_score is not None else "—"
    style = "green" if o.accuracy_passed else "red"
    tag = "PASS" if o.accuracy_passed else "FAIL"
    return f"[{style}]{score} {tag}[/{style}]"


def _reliability_cell(o: CaseOutcome) -> str:
    if o.reliability_passed is None:
        return "[dim]—[/dim]"
    style = "green" if o.reliability_passed else "red"
    tag = "PASS" if o.reliability_passed else "FAIL"
    return f"[{style}]{tag}[/{style}]"


@app.callback(invoke_without_command=True)
def main(
    ctx: typer.Context,
    case: str = typer.Option(None, "--case", help="Run only this case by name"),
) -> None:
    """Run the eval suite, or one case with --case <name>."""
    if ctx.invoked_subcommand is not None:
        return

    cases = list(CASES)
    if case:
        cases = [c for c in cases if c.name == case]
        if not cases:
            console.print(f"[red]no case named[/red] {case!r}")
            console.print(f"  [dim]available:[/dim] {', '.join(c.name for c in CASES)}")
            raise typer.Exit(2)

    outcomes: list[CaseOutcome] = []
    for i, c in enumerate(cases, 1):
        console.rule(f"[bold]{c.name}[/bold]  [dim]{c.agent.id} · {i}/{len(cases)}[/dim]")
        outcomes.append(run_case(c))

    table = Table(title="Eval Summary", title_style="bold sky_blue1", show_header=True, header_style="bold")
    table.add_column("Case", overflow="fold")
    table.add_column("Accuracy")
    table.add_column("Reliability")
    table.add_column("Status")
    for o in outcomes:
        status = "[green]PASS[/green]" if o.passed else "[red]FAIL[/red]"
        table.add_row(o.name, _accuracy_cell(o), _reliability_cell(o), status)

    console.print()
    console.print(table)

    passed = sum(1 for o in outcomes if o.passed)
    failed = len(outcomes) - passed
    summary = f"[green]{passed}/{len(outcomes)} passed[/green]"
    if failed:
        summary += f", [red]{failed} failed[/red]"
    console.print(f"\n{summary}")

    for o in outcomes:
        if o.error:
            console.print(f"  [dim]{o.name}:[/dim] [red]{o.error}[/red]")

    raise typer.Exit(0 if failed == 0 else 1)


if __name__ == "__main__":
    app()
