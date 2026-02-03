# Python - Inheritance

Exercises on class inheritance, introspection, and method overriding using a BaseGeometry → Rectangle → Square progression.

## Files
- `0-lookup.py`: function `lookup(obj)` returns the list of available attributes/methods.
- `1-my_list.py`: `MyList` subclass of `list` with `print_sorted()` helper.
- `2-is_same_class.py`: `is_same_class(obj, a_class)` checks exact type match.
- `3-is_kind_of_class.py`: `is_kind_of_class(obj, a_class)` checks instance of class or inherited.
- `4-inherits_from.py`: `inherits_from(obj, a_class)` true only when obj is a strict subclass instance.
- `5-base_geometry.py`: base class placeholder `BaseGeometry`.
- `6-base_geometry.py`: `BaseGeometry.area()` raises an exception (to be overridden).
- `7-base_geometry.py`: adds `integer_validator(name, value)` for validating dimensions.
- `8-rectangle.py`: `Rectangle` inherits `BaseGeometry`, validates `width`/`height` in `__init__`.
- `9-rectangle.py`: implements `area()` and `__str__` → `[Rectangle] <width>/<height>`.
- `10-square.py`: `Square` inherits `Rectangle`, validates `size`, reuses Rectangle init.
- `11-square.py`: overrides `__str__` → `[Square] <size>/<size>` while using inherited area.

## Usage examples
```bash
# Look up available attributes
python3 -c "from 0-lookup import lookup; print(lookup(5))"

# Validate and print shapes
python3 - <<'PY'
from 9-rectangle import Rectangle
from 11-square import Square
r = Rectangle(3, 4)
s = Square(5)
print(r, 'area:', r.area())
print(s, 'area:', s.area())
PY
```

## Requirements
- Python 3.8+ (Holberton baseline: Ubuntu 20.04).
- `pycodestyle` 2.8.* for linting.

## Notes
- Each script starts with `#!/usr/bin/python3`.
- Classes are import-safe; no top-level executable code.
