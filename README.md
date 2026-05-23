# Selection Sort Visualizer

[![Python CI](https://img.shields.io/github/actions/workflow/status/itkrivoshei/selection-sort-visualizer-python/python-ci.yml?branch=main&style=flat-square)](https://github.com/itkrivoshei/selection-sort-visualizer-python/actions/workflows/python-ci.yml)
[![License: MIT](https://img.shields.io/github/license/itkrivoshei/selection-sort-visualizer-python?style=flat-square)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.10%2B-blue?style=flat-square&logo=python&logoColor=white)](pyproject.toml)
[![Streamlit demo](https://img.shields.io/badge/demo-Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)](https://selection-sort-visualizer-python.streamlit.app/)

Interactive Python visualizer for the selection sort algorithm.

## Stack

- Python 3.10+
- Streamlit
- Plotly
- Pytest
- Ruff
- GitHub Actions

## Scope

- Step-by-step selection sort visualization
- Custom integer input
- Interactive step slider
- Color-coded algorithm states
- Reusable sorting module
- Small CLI example

## Live Demo

The Streamlit app is deployed here:

https://selection-sort-visualizer-python.streamlit.app/

## Install

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[app,dev]"
```

On Windows, activate the virtual environment with:

```powershell
.venv\Scripts\activate
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

```bash
python -m ruff check .
python -m ruff format --check .
python -m pytest -q
```

## Project Structure

```text
.
├── .github/workflows/python-ci.yml
├── src/selection_sort_visualizer/
│   ├── __init__.py
│   ├── parser.py
│   └── sorting.py
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

## Deployment

Streamlit Community Cloud uses:

```text
Main file path: streamlit_app.py
Python version: runtime.txt
Dependencies: requirements.txt
```

## License

This project is licensed under the [MIT License](LICENSE).
