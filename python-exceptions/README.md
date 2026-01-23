# Python - Exceptions

Exercises focused on Python's exception handling: using `try`/`except`/`finally`, catching specific errors, and raising your own exceptions to signal problems.

## Files
- `0-safe_print_list.py`: safely print `x` elements of a list and return the number printed.
- `1-safe_print_integer.py`: attempt to print an integer with formatting; return `True` on success, `False` otherwise.
- `2-safe_print_list_integers.py`: print the first `x` integers in a list, skipping non-integers without crashing.
- `3-safe_print_division.py`: divide two numbers while handling errors and always displaying the result.
- `4-list_division.py`: perform element-wise division between two lists with robust error handling.
- `5-raise_exception.py`: intentionally raise a `TypeError` to signal invalid usage.
- `6-raise_exception_msg.py`: raise a `NameError` with a custom message.

## Usage
Run scripts with Python 3:
```bash
python3 <script>.py
```
Many files expose functions; import them into your own code or tests to exercise their behaviors.

## Requirements
- Python 3.8+ (Holberton baseline: Ubuntu 20.04 with Python 3.8).
- `pycodestyle` 2.8.* for style checks.
- Executable scripts should start with `#!/usr/bin/python3` and have the executable bit set (`chmod +x <script>.py`).
