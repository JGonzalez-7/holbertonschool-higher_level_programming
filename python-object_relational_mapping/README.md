# Python - Object-relational mapping

This project moves from raw MySQL queries with `MySQLdb` to SQLAlchemy ORM models and sessions.

## Requirements
- Python 3.8+
- MySQL server (tested with MySQL 8.0)
- Packages: `mysqlclient` (for `MySQLdb`) and `SQLAlchemy`

Install deps in a virtualenv:
```bash
python3 -m venv .venv && source .venv/bin/activate
pip install mysqlclient SQLAlchemy
```

## Running the scripts
All scripts take credentials and database name as command-line arguments:
```bash
python3 0-select_states.py <user> <password> <database>
```

## Files
Raw SQL with `MySQLdb`:
- `0-select_states.py` — list all rows from `states`, ordered by `id`.
- `1-filter_states.py` — states starting with `N`.
- `2-my_filter_states.py` — states matching a name (uses string formatting; susceptible to SQL injection, for contrast only).
- `3-my_safe_filter_states.py` — same filter using parameter binding.
- `4-cities_by_state.py` — list cities with their state name via JOIN.
- `5-filter_cities.py` — list cities of a given state (safe parameterized query), printed comma-separated.

SQLAlchemy ORM (uses models in `model_state.py` and `model_city.py`):
- `7-model_state_fetch_all.py` — list all `State` objects.
- `8-model_state_fetch_first.py` — print the first `State` or `Nothing`.
- `9-model_state_filter_a.py` — states containing the letter `a`.
- `10-model_state_my_get.py` — print the `id` of a state by name or `Not found`.
- `11-model_state_insert.py` — add `Louisiana`, print its new `id`.
- `12-model_state_update_id_2.py` — rename state with `id = 2` to `New Mexico`.
- `13-model_state_delete_a.py` — delete states whose name contains `a`.
- `14-model_city_fetch_by_state.py` — list all `City` objects with their state name.

Models:
- `model_state.py` — `State` model and `Base` declarative instance.
- `model_city.py` — `City` model referencing `states.id`.

## Notes
- The database must already contain the `states` and `cities` tables (Holberton-provided schema/dumps). The scripts do not create schema.
- For ORM scripts, keep the model files in the same directory so imports resolve correctly.
