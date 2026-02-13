# Python Serialization

Small set of scripts showing different serialization formats in Python (JSON, pickle, CSV→JSON, XML). All tasks rely on the standard library only.

## Files
- `task_00_basic_serialization.py` – `serialize_and_save_to_file` writes a dictionary to JSON; `load_and_deserialize` reads it back.
- `task_01_pickle.py` – `CustomObject` with `serialize`/`deserialize` helpers for pickling an instance; `display` prints its attributes.
- `task_02_csv.py` – `convert_csv_to_json` loads a CSV with `csv.DictReader` and saves rows to `data.json`; returns `True`/`False` on success.
- `task_03_xml.py` – `serialize_to_xml` turns a dictionary into an XML file (root tag `data`); `deserialize_from_xml` rebuilds the dictionary.

## How to run
From this `python-serialization` directory:

```bash
python3 - <<'PY'
from task_00_basic_serialization import serialize_and_save_to_file, load_and_deserialize
from task_01_pickle import CustomObject
from task_02_csv import convert_csv_to_json
from task_03_xml import serialize_to_xml, deserialize_from_xml

serialize_and_save_to_file({"lang": "Python", "year": 1991}, "info.json")
print(load_and_deserialize("info.json"))

obj = CustomObject("Ada", 36, False)
obj.serialize("person.pkl")
CustomObject.deserialize("person.pkl").display()

# assumes sample.csv is present in this folder
convert_csv_to_json("sample.csv")

serialize_to_xml({"course": "Holberton", "topic": "Serialization"}, "data.xml")
print(deserialize_from_xml("data.xml"))
PY
```

Adjust filenames to point to your own test data. Scripts can also be imported into separate unit tests or notebooks.
