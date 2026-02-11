# Python Input/Output exercises

Practice file handling, JSON serialization, and simple class serialization patterns in Python. Most scripts are currently stubs; fill them in as you work through each task.

## Files
- `0-read_file.py` – Read a UTF-8 text file and print its contents.
- `1-write_file.py` – (stub) Write a string to a file and return the character count.
- `2-append_write.py` – (stub) Append text to a file and return the number of characters added.
- `3-to_json_string.py` – (stub) Convert a Python object to its JSON string representation.
- `4-from_json_string.py` – (stub) Parse a JSON string back into the corresponding Python object.
- `5-save_to_json_file.py` – (stub) Serialize a Python object to JSON and save it to disk.
- `6-load_from_json_file.py` – (stub) Load JSON from a file and recreate the Python object.
- `7-add_item.py` – (stub) Script entry point to load a list from JSON, add CLI args, and save it back.
- `8-class_to_json.py` – (stub) Helper to turn a class instance into a JSON-friendly dict.
- `9-student.py` – (stub) `Student` class with basic serialization to dictionary.
- `10-student.py` – (stub) `Student` class with selective attribute export.
- `11-student.py` – (stub) `Student` class with attribute reload from dictionary.
- `12-pascal_triangle.py` – (stub) Generate Pascal’s triangle as a list of lists.

## How to run
From this `python-input_output` directory:
```bash
python3 0-read_file.py
python3 1-write_file.py      # once implemented
python3 7-add_item.py arg1 arg2 ...
```
Add any needed test files (e.g., `.json` or `.txt`) alongside the scripts while developing.

## What to practice
- Safe text file reading/writing with context managers.
- Appending without overwriting existing content.
- JSON serialization/deserialization with `json` module.
- Making classes serializable by exposing dictionary representations.
- Building small CLI utilities that persist data between runs.
