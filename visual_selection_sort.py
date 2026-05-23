from __future__ import annotations

from selection_sort import iter_selection_sort


def print_selection_sort_steps(numbers: list[int]) -> None:
    """Print selection sort states in the terminal."""

    for index, step in enumerate(iter_selection_sort(numbers), start=1):
        print(
            f"step={index:02d} values={list(step.values)} "
            f"current={step.current_index} comparison={step.comparison_index} "
            f"smallest={step.smallest_index} swapped={step.swapped}"
        )


if __name__ == "__main__":
    print_selection_sort_steps([64, 25, 12, 22, 11])
