# Python - Test-driven Development

Exercises that introduce test-driven development with Python: writing functions alongside doctests and unittests to validate behavior and edge cases.

## Files
- `0-add_integer.py`: add two integers/floats after strict type validation (defaults `b` to 98).
- `2-matrix_divided.py`: divide all elements of a matrix by a number with input validation and rounded results.
- `3-say_my_name.py`: print a formatted "My name is" message using provided first and last names.
- `4-print_square.py`: print a square of `#` characters of a given size with validation.
- `5-text_indentation.py`: print text with new lines inserted after `.`, `?`, and `:` while trimming extra spaces.
- `tests/6-max_integer_test.py`: unittests for a `max_integer` helper (expected in `6-max_integer.py`).
- `tests/*.txt`: doctest files that specify expected output for the corresponding modules.

## Running tests
Run doctests for all tasks:
```bash
python3 -m doctest -v tests/*.txt
```
Run the unittest suite:
```bash
python3 -m unittest tests/6-max_integer_test.py
```

## Requirements
- Python 3.8+ (Holberton baseline: Ubuntu 20.04 with Python 3.8).
- `pycodestyle` 2.8.* for style checks.
- Scripts intended to run directly should start with `#!/usr/bin/python3` and have the executable bit set (`chmod +x <script>.py`).
