# Python Foundations — Minimal Starter Project

This tiny project demonstrates core Python foundations: modules, functions, classes, exceptions, file I/O, typing, tests, and a small CLI.

Layout
- `foundations/` — package containing examples
- `tests/` — pytest tests
- `cli.py` — small command-line demo
- `requirements.txt` — dev dependencies

Quick start

1. Create and activate a virtual environment:

```powershell
python -m venv .venv; .\.venv\Scripts\Activate
```

2. Install dev dependencies:

```powershell
pip install -r requirements.txt
```

3. Run tests:

```powershell
pytest -q
```

4. Run CLI:

```powershell
python cli.py greet Alice
```

What's inside
- Examples of functions, classes, dataclasses, exceptions, context managers, and typing.
- Tests that act as usage examples.

Next steps
- Add type checking with mypy, formatting with black, and linting with flake8.
