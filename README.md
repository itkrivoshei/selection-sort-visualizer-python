# Selection Sort Visualizer

[![Live app](https://img.shields.io/badge/live-Streamlit-ff4b4b?style=flat-square&logo=streamlit&logoColor=white)](https://selection-sort-visualizer-python.streamlit.app/)
[![Python CI](https://img.shields.io/github/actions/workflow/status/itkrivoshei/selection-sort-visualizer-python/python-ci.yml?branch=main&style=flat-square&label=python%20ci&logo=githubactions&logoColor=white)](https://github.com/itkrivoshei/selection-sort-visualizer-python/actions/workflows/python-ci.yml)
[![Python](https://img.shields.io/badge/Python-3.10%2B-3776ab?style=flat-square&logo=python&logoColor=white)](pyproject.toml)
[![Plotly](https://img.shields.io/badge/Plotly-charts-3f4f75?style=flat-square&logo=plotly&logoColor=white)](pyproject.toml)
[![License: MIT](https://img.shields.io/github/license/itkrivoshei/selection-sort-visualizer-python?style=flat-square)](LICENSE)

## [Open Streamlit App ->](https://selection-sort-visualizer-python.streamlit.app/)

Interactive Streamlit visualizer that turns selection sort into a step-by-step Plotly chart.

## Algorithm Lens

| Property | Value |
| --- | --- |
| Algorithm | Selection sort |
| Time complexity | `O(n^2)` |
| Auxiliary space | `O(1)` |
| Stability | Not stable by default |
| Visualization limit | `25` values for readable charts |

Each emitted `SortStep` captures the current index, comparison index, smallest candidate, swap state, sorted prefix, and full value list.

## App Features

- Accept comma, space, or newline separated integers.
- Validate input before rendering.
- Scrub through every algorithm state with a Streamlit slider.
- Color bars by sorted, current, compared, smallest, and unsorted states.
- Run the same sorting logic from a CLI entry point.

## Run Locally

```bash
git clone https://github.com/itkrivoshei/selection-sort-visualizer-python.git
cd selection-sort-visualizer-python
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[app,dev]"
streamlit run streamlit_app.py
```

CLI usage:

```bash
python main.py 64 25 12 22 11
```

## Quality Gate

```bash
python -m ruff check .
python -m ruff format --check .
python -m pytest -q
```

## Source Map

| Path | Purpose |
| --- | --- |
| `src/selection_sort_visualizer/sorting.py` | Sorting function and step iterator |
| `src/selection_sort_visualizer/parser.py` | Input parsing and validation |
| `streamlit_app.py` | Streamlit UI and Plotly chart rendering |
| `main.py` | CLI wrapper |
| `tests/` | Sorting, parser, and app-helper tests |

## Live App

https://selection-sort-visualizer-python.streamlit.app/

## License

[MIT](LICENSE)
