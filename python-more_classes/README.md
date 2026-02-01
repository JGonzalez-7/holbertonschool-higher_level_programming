# Python - More Classes and Objects

Exercises that deepen class mechanics with a `Rectangle` class: validation, string representations, class attributes, static/class methods, and alternative constructors.

## Files
- `0-rectangle.py`: empty `Rectangle` class (starter stub).
- `1-rectangle.py`: initializer with private `width`/`height` plus validation (`int`, `>= 0`).
- `2-rectangle.py`: adds `area()` and `perimeter()` methods.
- `3-rectangle.py`: implements `__str__` to print the rectangle with `#` and `__repr__` to recreate it.
- `4-rectangle.py`: improves `__repr__` for eval-style recreation.
- `5-rectangle.py`: prints a farewell message when an instance is deleted.
- `6-rectangle.py`: class attribute `number_of_instances` tracks live rectangles.
- `7-rectangle.py`: class attribute `print_symbol` customizes the drawing character.
- `8-rectangle.py`: static method `bigger_or_equal(rect_1, rect_2)` returns the larger rectangle by area.
- `9-rectangle.py`: class method `square(cls, size=0)` returns a new square-shaped `Rectangle`.

## Usage examples
```bash
# Area and perimeter
python3 -c "from 2-rectangle import Rectangle; r = Rectangle(3, 4); print(r.area(), r.perimeter())"

# Custom print symbol and comparison
python3 - <<'PY'
from 7-rectangle import Rectangle
Rectangle.print_symbol = '*'
r1, r2 = Rectangle(2, 3), Rectangle(4, 1)
print(r1)          # draws with '*'
print(Rectangle.bigger_or_equal(r1, r2) is r1)
PY

# Create a square via classmethod
python3 -c "from 9-rectangle import Rectangle; sq = Rectangle.square(5); print(sq.width, sq.height)"
```

## Requirements
- Python 3.8+ (Holberton baseline: Ubuntu 20.04).
- `pycodestyle` 2.8.* for linting.

## Notes
- Each script starts with `#!/usr/bin/python3`.
- Classes are import-safe; no top-level executable code.
