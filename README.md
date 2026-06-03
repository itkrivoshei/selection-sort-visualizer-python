<div align="center">

# Selection Sort Visualizer

Interactive Python app that turns selection sort into a step-by-step Streamlit and Plotly visualization.

[![Live app](https://img.shields.io/badge/live-Streamlit-ff4b4b?style=for-the-badge&logo=streamlit&logoColor=white&labelColor=0f172a)](https://selection-sort-visualizer-python.streamlit.app/)
[![Python CI](https://img.shields.io/github/actions/workflow/status/itkrivoshei/selection-sort-visualizer-python/python-ci.yml?branch=main&style=for-the-badge&label=ci&logo=githubactions&logoColor=white&labelColor=0f172a)](https://github.com/itkrivoshei/selection-sort-visualizer-python/actions/workflows/python-ci.yml)
[![CodeQL](https://img.shields.io/github/actions/workflow/status/itkrivoshei/selection-sort-visualizer-python/codeql.yml?branch=main&style=for-the-badge&label=codeql&logo=github&logoColor=white&labelColor=0f172a)](https://github.com/itkrivoshei/selection-sort-visualizer-python/actions/workflows/codeql.yml)
[![Python](https://img.shields.io/badge/Python-3.10%2B-3776ab?style=for-the-badge&logo=python&logoColor=white&labelColor=0f172a)](pyproject.toml)
[![Plotly](https://img.shields.io/badge/Plotly-charts-3f4f75?style=for-the-badge&logo=plotly&logoColor=white&labelColor=0f172a)](pyproject.toml)
[![License](https://img.shields.io/github/license/itkrivoshei/selection-sort-visualizer-python?style=for-the-badge&labelColor=0f172a)](LICENSE)

</div>

## Algorithm Lens

| Property            | Value                           |
| ------------------- | ------------------------------- |
| Algorithm           | Selection sort                  |
| Time complexity     | `O(n^2)`                        |
| Auxiliary space     | `O(1)`                          |
| Stability           | Not stable by default           |
| Visualization limit | `25` values for readable charts |

Each emitted `SortStep` captures the current index, comparison index, smallest candidate, swap state, sorted prefix, and full value list.

## Features

- Accept comma, space, or newline separated integers.
- Validate input before rendering.
- Scrub through every algorithm state with a Streamlit slider.
- Color bars by sorted, current, compared, smallest, and unsorted states.
- Run the same sorting logic from a CLI entry point.
- Keep algorithm logic separated from UI rendering and input parsing.

## Tech Stack

| Area      | Tools                                                                    |
| --------- | ------------------------------------------------------------------------ |
| App UI    | [Streamlit](https://streamlit.io/)                                       |
| Charts    | [Plotly](https://plotly.com/python/)                                     |
| Language  | [Python 3.10+](https://www.python.org/)                                  |
| Packaging | [`pyproject.toml`](pyproject.toml)                                       |
| Quality   | [Ruff](https://docs.astral.sh/ruff/), [pytest](https://docs.pytest.org/) |
| Security  | [CodeQL](https://codeql.github.com/)                                     |
| Hosting   | [Streamlit Community Cloud](https://streamlit.io/cloud)                  |

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

| Path                                                                                   | Purpose                                 |
| -------------------------------------------------------------------------------------- | --------------------------------------- |
| [`src/selection_sort_visualizer/sorting.py`](src/selection_sort_visualizer/sorting.py) | Sorting function and step iterator      |
| [`src/selection_sort_visualizer/parser.py`](src/selection_sort_visualizer/parser.py)   | Input parsing and validation            |
| [`streamlit_app.py`](streamlit_app.py)                                                 | Streamlit UI and Plotly chart rendering |
| [`main.py`](main.py)                                                                   | CLI wrapper                             |
| [`tests/`](tests/)                                                                     | Sorting, parser, and app-helper tests   |
| [`.github/workflows/python-ci.yml`](.github/workflows/python-ci.yml)                   | Ruff, formatting, and pytest CI checks  |
| [`.github/workflows/codeql.yml`](.github/workflows/codeql.yml)                         | GitHub CodeQL analysis                  |

## License

[MIT](LICENSE)
