from __future__ import annotations

import re

DEFAULT_VALUES = "64, 25, 12, 22, 11, 90, 34"
MAX_ITEMS = 25


def parse_numbers(raw_value: str, *, max_items: int = MAX_ITEMS) -> list[int]:
    """Parse comma, space, or newline separated integers from text input."""

    tokens = [token for token in re.split(r"[\s,]+", raw_value.strip()) if token]
    if not tokens:
        msg = "Enter at least one number."
        raise ValueError(msg)

    try:
        values = [int(token) for token in tokens]
    except ValueError as error:
        msg = "Only integers are supported. Use values such as: 64, 25, 12, 22."
        raise ValueError(msg) from error

    if len(values) > max_items:
        msg = f"Use {max_items} numbers or fewer for a readable visualization."
        raise ValueError(msg)

    return values
