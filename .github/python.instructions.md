---
applyTo: '**/*.py'
---

# Python Code Style and Quality Guidelines

All Python code in this repository must adhere to the following standards and practices.

## Style Guide

All Python code must follow the **Google Python Style Guide**: https://google.github.io/styleguide/pyguide.html

### Key Requirements

#### Formatting
- Use 4 spaces for indentation (no tabs)
- Maximum line length: 80 characters
- Use hanging indents for long function calls and definitions
- Separate top-level function and class definitions with two blank lines
- Separate method definitions inside a class with one blank line

#### Naming Conventions
- **Functions and variables**: `snake_case`
- **Classes**: `PascalCase` 
- **Constants**: `UPPER_CASE_WITH_UNDERSCORES`
- **Private attributes/methods**: prefix with single underscore `_private_method`
- **Modules**: short, lowercase names, underscores if needed

#### Imports
- Import entire modules, not individual functions (prefer `import os` over `from os import path`)
- Group imports in this order:
  1. Standard library imports
  2. Related third-party imports  
  3. Local application/library imports
- Separate each group with a blank line
- Use absolute imports whenever possible

#### Documentation
- All public modules, functions, classes, and methods must have docstrings
- Use Google-style docstrings with Args, Returns, and Raises sections
- Example:
```python
def function_name(param1: str, param2: int) -> bool:
    """Brief description of the function.
    
    Longer description if needed.
    
    Args:
        param1: Description of param1.
        param2: Description of param2.
        
    Returns:
        Description of return value.
        
    Raises:
        ValueError: Description of when this exception is raised.
    """
```

## Linting with Ruff

This project uses **ruff** for fast Python linting and code formatting.

### Configuration
Ruff is configured to enforce Google Python Style Guide rules. The following rule sets are enabled:
- `E` and `W` (pycodestyle errors and warnings)
- `F` (Pyflakes)
- `I` (isort for import sorting)
- `N` (pep8-naming)
- `D` (pydocstyle for docstring conventions)
- `UP` (pyupgrade for modern Python idioms)
- `B` (flake8-bugbear for likely bugs)
- `S` (flake8-bandit for security issues)
- `C4` (flake8-comprehensions)
- `PTH` (flake8-use-pathlib)

### Running Ruff
```bash
# Check for issues
ruff check .

# Auto-fix issues where possible
ruff check --fix .

# Format code
ruff format .
```

### Pre-commit Integration
Consider setting up ruff as a pre-commit hook to automatically check code before commits.

## Type Checking

This project uses **type checking** to ensure code correctness and maintainability.

### Type Annotation Requirements
- All function parameters and return values must have type annotations
- Use modern Python typing features (Python 3.9+ style when possible)
- Import types from `typing` module when needed
- Use `Optional[T]` or `T | None` for nullable types
- Use `list[T]`, `dict[K, V]`, `set[T]` instead of `List[T]`, `Dict[K, V]`, `Set[T]`

### Examples
```python
from typing import Optional, Union
from pathlib import Path

def process_data(
    data: list[str], 
    config: dict[str, int],
    output_path: Optional[Path] = None
) -> tuple[bool, str]:
    """Process data and return success status and message."""
    # Implementation here
    return True, "Success"

class DataProcessor:
    """Processes various data formats."""
    
    def __init__(self, config: dict[str, Union[str, int]]) -> None:
        self.config = config
    
    def process(self, items: list[str]) -> list[dict[str, str]]:
        """Process items and return results."""
        # Implementation here
        return []
```

### Running Type Checker
```bash
# Run type checking
ty check .

# Or if using mypy
mypy .
```

## Code Quality Standards

### Error Handling
- Use specific exception types rather than bare `except:`
- Provide meaningful error messages
- Follow the principle: "Easier to Ask for Forgiveness than Permission" (EAFP)

### Testing
- Write unit tests for all public functions and methods
- Use descriptive test method names that explain what is being tested
- Follow the Arrange-Act-Assert pattern

### Comments
- Write comments sparingly - prefer self-documenting code
- When comments are needed, explain **why**, not **what**
- Keep comments up to date with code changes

## Tools Integration

### Recommended IDE Setup
Configure your IDE/editor to:
- Run ruff on save
- Show type checking errors inline
- Format with ruff on save
- Highlight docstring issues

### Automation
Consider adding these tools to your CI/CD pipeline:
```bash
# In your CI script
ruff check .
ruff format --check .
ty check .  # or mypy .
```

## Resources

- [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)
- [Ruff Documentation](https://docs.astral.sh/ruff/)
- [Python Type Hints Documentation](https://docs.python.org/3/library/typing.html)
- [PEP 8 – Style Guide for Python Code](https://peps.python.org/pep-0008/)

---

*These guidelines ensure consistent, readable, and maintainable Python code across the project.*
