from __future__ import annotations

from collections.abc import Iterable, Iterator
from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class SortStep:
    """Single immutable state emitted by the selection sort visualizer."""

    values: tuple[int, ...]
    current_index: int | None = None
    comparison_index: int | None = None
    smallest_index: int | None = None
    swapped: bool = False
    sorted_until: int = 0

    @property
    def is_complete(self) -> bool:
        """Return True when the emitted state represents a fully sorted list."""

        return self.sorted_until >= len(self.values)


def selection_sort(numbers: Iterable[int]) -> list[int]:
    """Return a sorted copy of *numbers* using the selection sort algorithm."""

    values = list(numbers)

    for current_index in range(len(values)):
        smallest_index = current_index

        for comparison_index in range(current_index + 1, len(values)):
            if values[comparison_index] < values[smallest_index]:
                smallest_index = comparison_index

        if smallest_index != current_index:
            values[current_index], values[smallest_index] = (
                values[smallest_index],
                values[current_index],
            )

    return values


def iter_selection_sort(numbers: Iterable[int]) -> Iterator[SortStep]:
    """Yield selection sort states for visualization."""

    values = list(numbers)

    yield SortStep(values=tuple(values))

    for current_index in range(len(values)):
        smallest_index = current_index

        yield SortStep(
            values=tuple(values),
            current_index=current_index,
            smallest_index=smallest_index,
            sorted_until=current_index,
        )

        for comparison_index in range(current_index + 1, len(values)):
            if values[comparison_index] < values[smallest_index]:
                smallest_index = comparison_index

            yield SortStep(
                values=tuple(values),
                current_index=current_index,
                comparison_index=comparison_index,
                smallest_index=smallest_index,
                sorted_until=current_index,
            )

        swapped = smallest_index != current_index
        if swapped:
            values[current_index], values[smallest_index] = (
                values[smallest_index],
                values[current_index],
            )

        yield SortStep(
            values=tuple(values),
            current_index=current_index,
            smallest_index=smallest_index,
            swapped=swapped,
            sorted_until=current_index + 1,
        )
