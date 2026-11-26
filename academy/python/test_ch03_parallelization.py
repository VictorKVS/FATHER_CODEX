"""Offline unit tests for FATHER AI Academy CH03; Python >= 3.11."""
import asyncio
import unittest

try:
    from academy.python.ch03_parallelization import (
        concurrent_research, research, sequential_research
    )
except ModuleNotFoundError:
    from ch03_parallelization import concurrent_research, research, sequential_research


class ParallelizationLessonTests(unittest.IsolatedAsyncioTestCase):
    async def test_results_equal_and_preserve_order(self):
        items = ("Mars", "Venus", "Jupiter")
        a = await sequential_research(items, 0.001)
        b = await concurrent_research(items, 0.001)
        self.assertEqual(a.results, b.results)
        self.assertEqual([r.subject for r in b.results], list(items))

    async def test_empty_input(self):
        result = await concurrent_research((), 0)
        self.assertEqual(result.results, ())

    async def test_zero_delay(self):
        result = await concurrent_research(("A", "B"), 0)
        self.assertEqual(len(result.results), 2)

    async def test_negative_delay_rejected(self):
        with self.assertRaises(ValueError):
            await research("A", -1)

    async def test_child_failure_does_not_yield_partial_report(self):
        # A TaskGroup propagates failures instead of returning an incomplete report.
        with self.assertRaises(ExceptionGroup) as raised:
            await concurrent_research(("A", "B"), -1)
        self.assertTrue(any(isinstance(e, ValueError) for e in raised.exception.exceptions))

    async def test_elapsed_is_nonnegative(self):
        report = await sequential_research(("A",), 0)
        self.assertGreaterEqual(report.elapsed_seconds, 0)


if __name__ == "__main__":
    unittest.main()
