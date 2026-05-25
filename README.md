# Selection Sort Visualizer

[![Python CI](https://img.shields.io/github/actions/workflow/status/itkrivoshei/selection-sort-visualizer-python/python-ci.yml?branch=main&style=flat-square)](https://github.com/itkrivoshei/selection-sort-visualizer-python/actions/workflows/python-ci.yml)
[![License: MIT](https://img.shields.io/github/license/itkrivoshei/selection-sort-visualizer-python?style=flat-square)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.10%2B-blue?style=flat-square&logo=python&logoColor=white)](pyproject.toml)

Interactive Python visualizer for the selection sort algorithm.

Live demo: [selection-sort-visualizer-python.streamlit.app](https://selection-sort-visualizer-python.streamlit.app/)

## Project Scope

Small educational Python app for visualizing selection sort. It demonstrates reusable algorithm logic, input parsing, Streamlit UI, Plotly visualization, tests, Ruff, Dependabot, and GitHub Actions CI.

## Tech Stack

| Area | Tools |
|---|---|
| Language | Python 3.10+ |
| UI | Streamlit |
| Visualization | Plotly |
| Testing / quality | Pytest, Ruff |
| CI/CD | GitHub Actions |
| Dependency updates | Dependabot |
| Deployment | Streamlit Community Cloud |

## Algorithm

| Property | Value |
|---|---|
| Algorithm | Selection sort |
| Time complexity | `O(n²)` |
| Auxiliary space | `O(1)` |
| Stable by default | No |
| Practical use | Educational visualization |

## Install

```bash
git clone git@github.com:itkrivoshei/selection-sort-visualizer-python.git
cd selection-sort-visualizer-python
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[app,dev]"
```

## Run

```bash
streamlit run streamlit_app.py
```

Run the CLI example:

```bash
python main.py 64 25 12 22 11
```

## Verify

Run the same checks used by CI:

```bash
python -m ruff check .
python -m ruff format --check .
python -m pytest -q
```

## CI/CD

GitHub Actions validates dependency installation, Ruff, and Pytest on pushes and pull requests to `main`.

Dependabot checks Python and GitHub Actions dependencies weekly and is auto-merged after successful CI.

## Project Files

| File | Purpose |
|---|---|
| [`streamlit_app.py`](streamlit_app.py) | Streamlit interface and Plotly chart rendering |
| [`main.py`](main.py) | CLI entry point |
| [`src/selection_sort_visualizer/sorting.py`](src/selection_sort_visualizer/sorting.py) | Selection sort implementation and step generator |
| [`src/selection_sort_visualizer/parser.py`](src/selection_sort_visualizer/parser.py) | Input parsing and validation |
| [`tests/test_sorting.py`](tests/test_sorting.py) | Unit tests for sorting behavior |
| [`tests/test_streamlit_app.py`](tests/test_streamlit_app.py) | Tests for Streamlit-facing helpers |
| [`pyproject.toml`](pyproject.toml) | Project metadata, dependencies, Ruff, and Pytest config |
| [`.github/workflows/python-ci.yml`](.github/workflows/python-ci.yml) | CI workflow |
| [`.github/dependabot.yml`](.github/dependabot.yml) | Weekly dependency updates |
| [`LICENSE`](LICENSE) | MIT license |

## Deployment

Streamlit Community Cloud uses:

```text
Main file path: streamlit_app.py
Python version: runtime.txt
Dependencies: requirements.txt
```

## License

This project is licensed under the [MIT License](LICENSE).
