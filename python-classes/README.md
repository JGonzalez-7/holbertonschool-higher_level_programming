# Python - Classes and Objects

Intro project on Python OOP using a `Square` class to practice private attributes, validation, properties, and custom printing.

## Files
- `0-square.py`: defines an empty `Square` class.
- `1-square.py`: `Square` with a private `__size` set on init (no validation).
- `2-square.py`: adds size validation (`int`, `>= 0`) before storing `__size`.
- `3-square.py`: adds `area()` method returning `size ** 2`.
- `4-square.py`: exposes `size` as a property with validation in the setter.
- `5-square.py`: adds `my_print()` to draw the square with `#` (prints a blank line when size is 0).
- `6-square.py`: extends print behavior with a `position` tuple offset (`(x, y)` spaces/newlines) and validates both attributes.

## Usage examples
```bash
# Compute area
python3 -c "from 3-square import Square; s = Square(5); print(s.area())"

# Print with position offset
python3 -c "from 6-square import Square; s = Square(3, (1, 2)); s.my_print()"
```

## Requirements
- Python 3.8+ (Holberton baseline: Ubuntu 20.04).
- `pycodestyle` 2.8.* for linting.

## Notes
- Each script begins with `#!/usr/bin/python3`.
- Classes are import-safe; no top-level execution code.
