from __future__ import annotations

import pytest

from selection_sort_visualizer import iter_selection_sort, selection_sort


@pytest.mark.parametrize(
    ("input_values", "expected"),
    [
        ([], []),
        ([42], [42]),
        ([42, 23], [23, 42]),
        ([23, 42], [23, 42]),
        ([64, 34, 25, 12, 22, 11, 90], [11, 12, 22, 25, 34, 64, 90]),
        ([-5, -1, -89, 0, 3, 8], [-89, -5, -1, 0, 3, 8]),
        ([5, 3, 5, 3, 5], [3, 3, 5, 5, 5]),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
        ([2, 2, 2, 2, 2], [2, 2, 2, 2, 2]),
    ],
)
def test_selection_sort_returns_sorted_copy(input_values: list[int], expected: list[int]) -> None:
    original = input_values.copy()

    assert selection_sort(input_values) == expected
    assert input_values == original


def test_iter_selection_sort_finishes_with_sorted_values() -> None:
    steps = list(iter_selection_sort([4, 2, 3, 1]))

    assert steps
    assert list(steps[-1].values) == [1, 2, 3, 4]
    assert steps[-1].sorted_until == 4
