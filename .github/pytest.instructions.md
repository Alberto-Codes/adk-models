---
applyTo: '**/*_test.py, **/test_*.py'
---

# Pytest Best Practices

This document outlines the best practices for using pytest in this project, focusing on folder structure, organization, and testing patterns.

## Folder Structure

### Recommended Layout

The most recommended approach is to keep tests separate from application code in a dedicated `tests` directory:

```
project_root/
├── pyproject.toml
├── src/
│   └── package_name/
│       ├── __init__.py
│       ├── module1.py
│       └── module2.py
└── tests/
    ├── __init__.py  # Makes tests a package
    ├── conftest.py  # Shared test fixtures
    ├── test_module1.py
    └── test_module2.py
```

This structure has several benefits:
- Keeps tests separate from implementation code
- Makes it clear which files are tests
- Prevents test files from being included in distributions

### Alternative: Tests Inside Package

For some projects, you may want to include tests with the package:

```
project_root/
├── pyproject.toml
└── src/
    └── package_name/
        ├── __init__.py
        ├── module1.py
        ├── module2.py
        └── tests/
            ├── __init__.py
            ├── test_module1.py
            └── test_module2.py
```

This approach is useful when you want to distribute tests with your package.

## Naming Conventions

- Test files should be named `test_*.py` or `*_test.py`
- Test functions should be named `test_*`
- Test classes should be named `Test*`
- Use descriptive names that explain what is being tested

## Test Organization

### Mirror Your Application Structure

Your test structure should mirror your application structure. For example:

```
src/
  package_name/
    core/
      feature.py
    utils/
      helper.py

tests/
  package_name/
    core/
      test_feature.py
    utils/
      test_helper.py
```

### Group Tests by Testing Level

Consider organizing tests by testing level:

```
tests/
  unit/           # Fast tests that test a single component
  integration/    # Tests that check multiple components working together
  functional/     # Tests that check entire features
  performance/    # Tests that verify performance requirements
```

## Using Fixtures

- Place fixtures in `conftest.py` files to make them available to multiple test files
- Use a hierarchy of `conftest.py` files to scope fixtures appropriately:
  - `tests/conftest.py` for project-wide fixtures
  - `tests/unit/conftest.py` for unit-test specific fixtures

Example `conftest.py`:

```python
import pytest

@pytest.fixture
def sample_data():
    return {"key": "value"}

@pytest.fixture(scope="session")
def database_connection():
    # Set up a connection
    connection = create_connection()
    yield connection
    # Tear down after all tests
    connection.close()
```

## Running Tests

To run all tests from the project root:

```bash
pytest
```

To run a specific test file:

```bash
pytest tests/test_module.py
```

To run a specific test function:

```bash
pytest tests/test_module.py::test_function
```

To run tests with verbose output:

```bash
pytest -v
```

## Test Discovery

Pytest automatically finds tests based on these conventions:
- Files named `test_*.py` or `*_test.py`
- Functions prefixed with `test_`
- Classes prefixed with `Test`
- Methods prefixed with `test_` inside `Test` classes

## Assertion Best Practices

- Use plain `assert` statements instead of unittest-style assertions
- Provide helpful messages in assertions:
  ```python
  assert result == expected, f"Expected {expected} but got {result}"
  ```
- Use pytest's built-in assertion introspection to get detailed error messages

## Parametrized Tests

Use `@pytest.mark.parametrize` to run the same test with different inputs:

```python
import pytest

@pytest.mark.parametrize("input,expected", [
    (1, 1),
    (2, 4),
    (3, 9),
    (4, 16),
])
def test_square(input, expected):
    assert input * input == expected
```

## Markers

Use markers to categorize tests:

```python
import pytest

@pytest.mark.slow
def test_slow_operation():
    # Test code here
    pass
```

Run tests with specific markers:

```bash
pytest -m slow
```

## Testing Coverage

Use pytest-cov to measure test coverage:

```bash
pytest --cov=src tests/
```

Generate an HTML coverage report:

```bash
pytest --cov=src --cov-report=html tests/
```

## Temporary Files and Directories

Use `tmp_path` fixture for tests that need to create temporary files:

```python
def test_file_operations(tmp_path):
    test_file = tmp_path / "test.txt"
    test_file.write_text("content")
    assert test_file.read_text() == "content"
```

## Additional Resources

- [Pytest Documentation](https://docs.pytest.org/)
- [Pytest Good Practices](https://docs.pytest.org/en/stable/explanation/goodpractices.html)
- [Python Testing with pytest by Brian Okken](https://pragprog.com/titles/bopytest2/python-testing-with-pytest-second-edition/)
