from __future__ import annotations

import argparse

from selection_sort import selection_sort


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Sort integers with selection sort.")
    parser.add_argument(
        "numbers",
        nargs="*",
        type=int,
        default=[64, 25, 12, 22, 11],
        help="Numbers to sort. Example: python main.py 5 3 1",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    print(selection_sort(args.numbers))


if __name__ == "__main__":
    main()
