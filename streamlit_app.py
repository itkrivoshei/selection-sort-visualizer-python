from __future__ import annotations

import re

import plotly.graph_objects as go
import streamlit as st

from selection_sort import SortStep, iter_selection_sort, selection_sort

DEFAULT_VALUES = "64, 25, 12, 22, 11, 90, 34"
MAX_ITEMS = 25


def parse_numbers(raw_value: str) -> list[int]:
    """Parse comma, space, or newline separated integers from a text input."""

    tokens = [token for token in re.split(r"[\s,]+", raw_value.strip()) if token]
    if not tokens:
        msg = "Enter at least one number."
        raise ValueError(msg)

    values = [int(token) for token in tokens]
    if len(values) > MAX_ITEMS:
        msg = f"Use {MAX_ITEMS} numbers or fewer for a readable visualization."
        raise ValueError(msg)

    return values


def step_summary(step: SortStep, step_number: int, total_steps: int) -> str:
    """Create a compact explanation for the current algorithm state."""

    if step_number == 0:
        return "Initial input before sorting starts."
    if step.swapped:
        return "Swap completed: the smallest value found in this pass moved into place."
    if step.comparison_index is not None:
        return (
            f"Comparing index {step.comparison_index} with current smallest "
            f"index {step.smallest_index}."
        )
    if step_number == total_steps - 1:
        return "Sorting complete."
    return f"Starting pass at index {step.current_index}."


def build_chart(step: SortStep) -> go.Figure:
    """Build a Plotly bar chart for the selected sorting step."""

    values = list(step.values)
    marker_colors = []

    for index, _ in enumerate(values):
        if index < step.sorted_until:
            marker_colors.append("#22c55e")
        elif index == step.current_index:
            marker_colors.append("#f59e0b")
        elif index == step.comparison_index:
            marker_colors.append("#38bdf8")
        elif index == step.smallest_index:
            marker_colors.append("#ef4444")
        else:
            marker_colors.append("#64748b")

    figure = go.Figure(
        data=[
            go.Bar(
                x=list(range(len(values))),
                y=values,
                text=values,
                textposition="outside",
                marker_color=marker_colors,
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

    with st.sidebar:
        st.header("Input")
        raw_numbers = st.text_area(
            "Numbers",
            value=DEFAULT_VALUES,
            help="Use comma, space, or newline separated integers.",
        )
        st.caption(f"Limit: {MAX_ITEMS} values for readable charts.")

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
        st.plotly_chart(build_chart(step), use_container_width=True)
        st.info(step_summary(step, selected_step, len(steps)))

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
