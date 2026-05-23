# Selection Sort Visualizer

Interactive Python app for exploring how selection sort works step by step.

The project separates the algorithm logic from the Streamlit interface and includes automated checks for linting, formatting, and tests.

## Demo

Streamlit entry point:

```text
streamlit_app.py
```

For Streamlit Community Cloud, use:

```text
Repository: itkrivoshei/selection-sort-visualizer-python
Branch: main
Main file path: streamlit_app.py
Python version: runtime.txt
```

## Features

- Step-by-step selection sort visualization
- Custom number input
- Interactive algorithm step slider
- Color-coded Plotly chart
- Reusable Python sorting module
- CLI example
- Pytest tests
- Ruff linting and formatting
- GitHub Actions validation

## Project Structure

```text
.
├── .github/
│   └── workflows/
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

## Run Locally

Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
python -m pip install --upgrade pip
python -m pip install -e ".[app,dev]"
```

Run the Streamlit app:

```bash
streamlit run streamlit_app.py
```

Run the CLI example:

```bash
python main.py 64 25 12 22 11
```

## Quality Checks

Run tests:

```bash
python -m pytest -q
```

Run linting and formatting checks:

```bash
python -m ruff check .
python -m ruff format --check .
```

## Algorithm Notes

Selection sort repeatedly scans the unsorted section of a list, selects the smallest value, and swaps it into the next sorted position.

Complexity:

- Time: `O(n²)`
- Space: `O(1)` for the in-place algorithm idea

## License

This project is licensed under the MIT License.
