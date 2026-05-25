# Selection Sort Visualizer

[![Python CI](https://img.shields.io/github/actions/workflow/status/itkrivoshei/selection-sort-visualizer-python/python-ci.yml?branch=main&style=flat-square)](https://github.com/itkrivoshei/selection-sort-visualizer-python/actions/workflows/python-ci.yml)
[![License: MIT](https://img.shields.io/github/license/itkrivoshei/selection-sort-visualizer-python?style=flat-square)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.10%2B-blue?style=flat-square&logo=python&logoColor=white)](pyproject.toml)
[![Streamlit demo](https://img.shields.io/badge/demo-Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)](https://selection-sort-visualizer-python.streamlit.app/)

Interactive Python visualizer for the selection sort algorithm.

The project demonstrates a small but complete Python application: reusable algorithm logic, input parsing, Streamlit UI, Plotly visualization, automated tests, linting, formatting checks, Dependabot updates, Streamlit Community Cloud deployment, and GitHub Actions CI.

## Live Demo

Open the Streamlit app:

https://selection-sort-visualizer-python.streamlit.app/

## Quick Links

| Resource | Link |
|---|---|
| Live demo | [Streamlit app](https://selection-sort-visualizer-python.streamlit.app/) |
| Streamlit app entry point | [`streamlit_app.py`](streamlit_app.py) |
| CLI entry point | [`main.py`](main.py) |
| Sorting logic | [`src/selection_sort_visualizer/sorting.py`](src/selection_sort_visualizer/sorting.py) |
| Input parser | [`src/selection_sort_visualizer/parser.py`](src/selection_sort_visualizer/parser.py) |
| Algorithm tests | [`tests/test_sorting.py`](tests/test_sorting.py) |
| Streamlit tests | [`tests/test_streamlit_app.py`](tests/test_streamlit_app.py) |
| CI workflow | [`.github/workflows/python-ci.yml`](.github/workflows/python-ci.yml) |
| Dependabot config | [`.github/dependabot.yml`](.github/dependabot.yml) |
| License | [`LICENSE`](LICENSE) |

## Features

- Step-by-step selection sort visualization
- Custom integer input using commas, spaces, or new lines
- Interactive step slider
- Color-coded algorithm states
- Compact explanation for each sorting step
- Reusable sorting module separated from the UI
- CLI example for running the algorithm from the terminal
- Automated CI with Ruff and Pytest
- Auto-merge Dependabot pull requests after successful CI

## Tech Stack

| Area | Tools |
|---|---|
| Language | Python 3.10+ |
| UI | Streamlit |
| Visualization | Plotly |
| Testing | Pytest |
| Linting / formatting | Ruff |
| CI | GitHub Actions |
| Dependency updates | Dependabot |
| Deployment | Streamlit Community Cloud |

## Algorithm Scope

Selection sort repeatedly scans the unsorted part of the list, finds the smallest value, and swaps it into the next sorted position.

| Property | Value |
|---|---|
| Time complexity | `O(n²)` |
| Auxiliary space | `O(1)` |
| Stable by default | No |
| Practical use | Educational visualization |

## Install

Clone the repository:

```bash
git clone git@github.com:itkrivoshei/selection-sort-visualizer-python.git
cd selection-sort-visualizer-python
```

Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

On Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Install the app and development dependencies:

```bash
python -m pip install --upgrade pip
python -m pip install -e ".[app,dev]"
```

## Run

Run the Streamlit app:

```bash
streamlit run streamlit_app.py
```

Run the CLI example:

```bash
python main.py 64 25 12 22 11
```

No build step is required.

## Verify

Run the same checks used by CI:

```bash
python -m ruff check .
python -m ruff format --check .
python -m pytest -q
```

## CI/CD

The GitHub Actions workflow runs on pushes and pull requests to `main`.

It checks:

- dependency installation
- Ruff linting
- Ruff formatting
- Pytest tests

Dependabot checks Python and GitHub Actions dependencies weekly. Dependabot pull requests are automatically squash-merged only after the CI workflow finishes successfully.

## Project Structure

```text
.
├── .github/
│   ├── dependabot.yml
│   └── workflows/
│       ├── dependabot-auto-merge.yml
│       └── python-ci.yml
├── src/
│   └── selection_sort_visualizer/
│       ├── __init__.py
│       ├── parser.py
│       └── sorting.py
├── tests/
│   ├── test_sorting.py
│   └── test_streamlit_app.py
├── main.py
├── streamlit_app.py
├── requirements.txt
├── runtime.txt
├── pyproject.toml
└── README.md
```

## Key Files

| File | Purpose |
|---|---|
| [`streamlit_app.py`](streamlit_app.py) | Streamlit interface and Plotly chart rendering |
| [`main.py`](main.py) | Small CLI entry point |
| [`src/selection_sort_visualizer/sorting.py`](src/selection_sort_visualizer/sorting.py) | Selection sort implementation and step generator |
| [`src/selection_sort_visualizer/parser.py`](src/selection_sort_visualizer/parser.py) | Input parsing and validation |
| [`tests/test_sorting.py`](tests/test_sorting.py) | Unit tests for sorting behavior |
| [`tests/test_streamlit_app.py`](tests/test_streamlit_app.py) | Tests for Streamlit-facing helpers |
| [`.github/workflows/python-ci.yml`](.github/workflows/python-ci.yml) | CI workflow for linting, formatting checks, and tests |
| [`.github/workflows/dependabot-auto-merge.yml`](.github/workflows/dependabot-auto-merge.yml) | Dependabot auto-merge after green CI |
| [`.github/dependabot.yml`](.github/dependabot.yml) | Weekly dependency update checks |

## Deployment

Streamlit Community Cloud uses:

```text
Main file path: streamlit_app.py
Python version: runtime.txt
Dependencies: requirements.txt
```

`requirements.txt` installs the package with app dependencies:

```text
-e .[app]
```

## License

This project is licensed under the [MIT License](LICENSE).
