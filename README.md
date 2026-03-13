# holbertonschool-higher_level_programming

Collection of Holberton higher-level programming projects focused on Python, SQL, HTTP, serialization, and object-relational mapping. Each directory is a standalone project with its own tasks, scripts, and project-specific README.

## Overview

This repository tracks the progression from Python fundamentals to more structured application topics:

- basic Python syntax, flow control, data structures, and imports
- object-oriented programming with classes, inheritance, and abstract base classes
- exceptions, file handling, JSON/pickle/XML/CSV serialization, and test-driven development
- SQL fundamentals, relational queries, and Python database access with MySQLdb and SQLAlchemy
- HTTP concepts, API consumption, and simple REST API exercises

## Project map

| Directory | Focus |
| --- | --- |
| `python-hello_world/` | First Python scripts, printing, strings, and formatting |
| `python-if_else_loops_functions/` | Conditionals, loops, and simple functions |
| `python-data_structures/` | Lists, tuples, indexing, replacement, and small sequence algorithms |
| `python-more_data_structures/` | Sets, dictionaries, comprehensions, and mapping utilities |
| `python-import_modules/` | Imports, module organization, and command-line arguments |
| `python-classes/` | Introductory OOP with `Square` |
| `python-more_classes/` | Class attributes, methods, and a richer `Rectangle` model |
| `python-inheritance/` | Inheritance, introspection, and method reuse |
| `python-abc/` | Abstract base classes, duck typing, and multiple inheritance |
| `python-exceptions/` | `try`/`except` handling and custom exceptions |
| `python-input_output/` | File I/O, JSON conversion, and object serialization helpers |
| `python-serialization/` | JSON, pickle, CSV to JSON, and XML serialization exercises |
| `python-test_driven_development/` | Doctests, unittests, and validation-focused functions |
| `SQL_introduction/` | MySQL basics, CRUD, filtering, grouping, and aggregation |
| `SQL_more_queries/` | Privileges, constraints, joins, and relational querying |
| `python-object_relational_mapping/` | MySQLdb queries and SQLAlchemy ORM models |
| `restful-api/` | HTTP fundamentals, `curl`, `requests`, Flask, and basic API security |

## Requirements

Common tools used across the repository:

- Python 3.8+
- `pycodestyle` 2.8.*
- MySQL 8.0+ for SQL and ORM projects

Additional packages for specific projects:

- `mysqlclient` for `MySQLdb`
- `SQLAlchemy`
- `requests`
- `Flask`
- `PyJWT`

## Quick start

Clone the repository and work inside the project directory you need:

```bash
git clone <your-repo-url>
cd holbertonschool-higher_level_programming
```

Run a Python task:

```bash
cd python-hello_world
python3 2-print.py
```

Run a SQL script:

```bash
cd SQL_introduction
mysql -uroot -p < 0-list_databases.sql
```

Run an ORM script:

```bash
cd python-object_relational_mapping
python3 0-select_states.py <mysql_user> <mysql_password> <database_name>
```

## Useful commands

Check Python style:

```bash
pycodestyle *.py
```

Run doctests or unit tests when a project includes them:

```bash
python3 -m doctest -v ./tests/*
python3 -m unittest discover
```

Make a script executable if needed:

```bash
chmod +x script.py
```

## Working in this repo

- Start at the README inside the project folder you are working on.
- Treat each directory as an independent assignment set.
- Expect some projects to require external services or packages, especially MySQL and API-related tasks.

## Notes

- Most Python tasks follow the Holberton convention of executable scripts with `#!/usr/bin/python3`.
- Some directories contain starter files or partial implementations intended to be completed incrementally.
- Environment expectations can vary slightly by project, so prefer the local README in that directory for exact run instructions.
