from __future__ import annotations

import plotly.graph_objects as go
import streamlit as st

from selection_sort_visualizer import (
    DEFAULT_VALUES,
    MAX_ITEMS,
    SortStep,
    iter_selection_sort,
    parse_numbers,
    selection_sort,
)

BAR_COLORS = {
    "sorted": "#22c55e",
    "current": "#f59e0b",
    "comparison": "#38bdf8",
    "smallest": "#ef4444",
    "default": "#64748b",
}


def step_summary(step: SortStep, step_number: int) -> str:
    """Create a compact explanation for the current algorithm state."""

    if step_number == 0:
        return "Initial input before sorting starts."
    if step.is_complete:
        return "Sorting complete."
    if step.swapped:
        return "Swap completed: the smallest value found in this pass moved into place."
    if step.comparison_index is not None:
        return (
            f"Comparing index {step.comparison_index} with current smallest "
            f"index {step.smallest_index}."
        )
    if step.current_index is not None and step.sorted_until > step.current_index:
        return "No swap needed: the current value is already in the sorted position."
    return f"Starting pass at index {step.current_index}."


def step_progress_label(step: SortStep, step_number: int, total_steps: int) -> str:
    """Return a compact progress label for the selected sorting step."""

    max_step = max(total_steps - 1, 0)
    sorted_count = min(step.sorted_until, len(step.values))
    return f"Step {step_number} of {max_step} · sorted prefix: {sorted_count}/{len(step.values)}"


def marker_colors(step: SortStep) -> list[str]:
    """Return bar colors for the current visualization step."""

    colors = []

    for index, _ in enumerate(step.values):
        if index < step.sorted_until:
            colors.append(BAR_COLORS["sorted"])
        elif index == step.current_index:
            colors.append(BAR_COLORS["current"])
        elif index == step.comparison_index:
            colors.append(BAR_COLORS["comparison"])
        elif index == step.smallest_index:
            colors.append(BAR_COLORS["smallest"])
        else:
            colors.append(BAR_COLORS["default"])

    return colors


def build_chart(step: SortStep) -> go.Figure:
    """Build a Plotly bar chart for the selected sorting step."""

    values = list(step.values)
    figure = go.Figure(
        data=[
            go.Bar(
                x=list(range(len(values))),
                y=values,
                text=values,
                textposition="outside",
                marker_color=marker_colors(step),
                hovertemplate="index=%{x}<br>value=%{y}<extra></extra>",
            )
        ]
    )
    figure.update_layout(
        title="Selection sort state",
        xaxis_title="Index",
        yaxis_title="Value",
        template="plotly_dark",
        margin={"l": 40, "r": 20, "t": 60, "b": 40},
        height=480,
        showlegend=False,
    )
    return figure


def render_sidebar() -> str:
    """Render sidebar controls and return raw input."""

    with st.sidebar:
        st.header("Input")
        raw_numbers = st.text_area(
            "Numbers",
            value=DEFAULT_VALUES,
            help="Use comma, space, or newline separated integers.",
        )
        st.caption(f"Limit: {MAX_ITEMS} values for readable charts.")
        st.divider()
        st.caption("Selection sort runs in O(n²) time and O(1) auxiliary space.")

    return raw_numbers


def main() -> None:
    st.set_page_config(
        page_title="Selection Sort Visualizer",
        page_icon="🔎",
        layout="wide",
    )

    st.title("Selection Sort Visualizer")
    st.caption(
        "Interactive Python demo showing how selection sort scans, selects, "
        "and swaps values step by step."
    )

    raw_numbers = render_sidebar()

    try:
        numbers = parse_numbers(raw_numbers)
    except ValueError as error:
        st.error(str(error))
        return

    steps = list(iter_selection_sort(numbers))
    sorted_numbers = selection_sort(numbers)

    left, right = st.columns([2, 1])

    with right:
        st.subheader("Result")
        st.code(str(sorted_numbers), language="python")
        st.metric("Input size", len(numbers))
        st.metric("Visualization steps", len(steps))

    with left:
        selected_step = st.slider(
            "Step",
            min_value=0,
            max_value=len(steps) - 1,
            value=0,
        )
        step = steps[selected_step]
        st.caption(step_progress_label(step, selected_step, len(steps)))
        st.plotly_chart(build_chart(step), use_container_width=True)
        st.info(step_summary(step, selected_step))

    st.subheader("Legend")
    st.markdown(
        "🟢 sorted prefix · 🟠 current position · 🔵 compared value · "
        "🔴 current smallest candidate · ⚪ unsorted values"
    )

    with st.expander("Algorithm notes"):
        st.markdown(
            "Selection sort repeatedly finds the smallest item in the unsorted "
            "part of the list and swaps it into the next sorted position. "
            "Its time complexity is **O(n²)**, so it is useful for learning "
            "algorithm mechanics rather than for production sorting."
        )


if __name__ == "__main__":
    main()
