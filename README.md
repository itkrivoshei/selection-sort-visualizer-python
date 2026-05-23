# Selection Sort Visualizer

Interactive Python app for exploring how the selection sort algorithm works step by step.

The project includes a small algorithm core, a Streamlit visual demo, a CLI entry point, and automated checks with GitHub Actions.

## Demo

The Streamlit app entry point is:

```text
streamlit_app.py
```

Deploy it with Streamlit Community Cloud by selecting this repository, the `main` branch, and `streamlit_app.py` as the main file.

## Features

- Step-by-step selection sort visualization
- Custom number input from the sidebar
- Interactive slider for moving through algorithm states
- Plotly chart with color-coded sorting states
- Pure Python algorithm implementation
- Pytest test coverage for the sorting logic
- Ruff linting and formatting checks in CI

## Project Structure

```text
.
├── .github/workflows/python-ci.yml
├── main.py
├── selection_sort.py
├── streamlit_app.py
├── test_selection_sort.py
├── visual_selection_sort.py
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

Run the Streamlit demo:

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
pytest -q
```

Run linting and formatting checks:

```bash
ruff check .
ruff format --check .
```

## Algorithm Notes

Selection sort repeatedly scans the unsorted section of a list, selects the smallest value, and swaps it into the next sorted position.

Complexity:

- Time: `O(n²)`
- Space: `O(1)` for the in-place algorithm idea

This makes it useful for learning algorithm mechanics, but not suitable as a production sorting strategy for large datasets.

## License

This project is licensed under the MIT License.
