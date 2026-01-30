# Python - Classes and Objects

Intro project on basic object-oriented programming in Python using a `Square` class as the running example.

## Files present
- `0-square.py`: empty `Square` class (starter stub).
- `1-square.py`: skeleton for initializing a square with a private `size`.
- `2-square.py`: placeholder for size validation (`int`, `>= 0`).
- `3-square.py`: placeholder for an `area()` method.
- `4-square.py`: placeholder for a size property with getter/setter validation.
- `5-square.py`: placeholder for `my_print()` to draw the square with `#`.
- `6-square.py`: placeholder for handling a `position` offset when printing.

## Usage examples
```bash
# Example with completed tasks (once implementations are added)
python3 -c "from 3-square import Square; s = Square(5); print(s.area())"

python3 -c "from 6-square import Square; s = Square(3, (1, 2)); s.my_print()"
```

## Requirements
- Python 3.8+ (Holberton baseline: Ubuntu 20.04).
- `pycodestyle` 2.8.* for linting.

## Notes
- Each script should start with `#!/usr/bin/python3`.
- Keep classes self-contained; do not execute test code on import.
