"""CH03 Parallelization educational baseline — stdlib-only.

Based on concept of independent concurrent tasks in Antonio Gulli,
Agentic Design Patterns, Chapter 3 (user-provided original PDF 48–62).
This is original educational code, not a copied book listing.
No network, LLM calls, paid APIs, or side effects.
"""
from __future__ import annotations

import asyncio
from dataclasses import dataclass
from time import perf_counter
from typing import Awaitable, Callable


@dataclass(frozen=True)
class ResearchResult:
    subject: str
    content: str


@dataclass(frozen=True)
class Report:
    results: tuple[ResearchResult, ...]
    elapsed_seconds: float


async def research(subject: str, delay_seconds: float = 0.01) -> ResearchResult:
    """Pretend to wait for an external knowledge source."""
    if delay_seconds < 0:
        raise ValueError("delay_seconds must be nonnegative")
    await asyncio.sleep(delay_seconds)
    return ResearchResult(subject=subject, content=f"Сведения по теме «{subject}»")


async def sequential_research(
    subjects: tuple[str, ...], delay_seconds: float = 0.01
) -> Report:
    start = perf_counter()
    results: list[ResearchResult] = []
    for subject in subjects:
        results.append(await research(subject, delay_seconds))
    return Report(results=tuple(results), elapsed_seconds=perf_counter() - start)


async def concurrent_research(
    subjects: tuple[str, ...], delay_seconds: float = 0.01
) -> Report:
    """Start independent tasks concurrently; preserve input order.

    A TaskGroup fails the group if any child fails; this prevents treating
    an incomplete set as a complete report.
    Python >= 3.11.
    """
    start = perf_counter()
    async with asyncio.TaskGroup() as group:
        tasks = [group.create_task(research(s, delay_seconds)) for s in subjects]
    results = tuple(task.result() for task in tasks)
    return Report(results=results, elapsed_seconds=perf_counter() - start)


async def main() -> None:
    subjects = ("Марс", "Венера", "Юпитер")
    sequential = await sequential_research(subjects, 0.15)
    concurrent = await concurrent_research(subjects, 0.15)
    assert sequential.results == concurrent.results
    print("Последовательно:", round(sequential.elapsed_seconds, 3), "с")
    print("Конкурентно:   ", round(concurrent.elapsed_seconds, 3), "с")
    print("Результаты:", [r.subject for r in concurrent.results])
    print("Примечание: время зависит от среды; улучшение не гарантировано.")


if __name__ == "__main__":
    asyncio.run(main())
