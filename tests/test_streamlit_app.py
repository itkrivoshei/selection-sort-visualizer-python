from __future__ import annotations

from selection_sort_visualizer import SortStep
from streamlit_app import build_chart, marker_colors, step_progress_label, step_summary


def test_marker_colors_highlights_sorted_prefix() -> None:
    step = SortStep(
        values=(3, 1, 2),
        current_index=1,
        comparison_index=2,
        smallest_index=1,
        sorted_until=1,
    )

    colors = marker_colors(step)

    assert colors[0] != colors[1]
    assert len(colors) == 3


def test_step_summary_marks_completed_sort() -> None:
    step = SortStep(values=(1, 2, 3), sorted_until=3)

    assert step_summary(step, step_number=5) == "Sorting complete."


def test_step_summary_marks_no_swap_pass() -> None:
    step = SortStep(values=(1, 2, 3), current_index=0, smallest_index=0, sorted_until=1)

    assert step_summary(step, step_number=3) == (
        "No swap needed: the current value is already in the sorted position."
    )


def test_step_progress_label_includes_sorted_prefix() -> None:
    step = SortStep(values=(1, 2, 3), sorted_until=2)

    assert step_progress_label(step, step_number=4, total_steps=8) == (
        "Step 4 of 7 · sorted prefix: 2/3"
    )


def test_build_chart_returns_one_bar_trace() -> None:
    step = SortStep(values=(3, 1, 2))

    figure = build_chart(step)

    assert len(figure.data) == 1
    assert list(figure.data[0].y) == [3, 1, 2]
