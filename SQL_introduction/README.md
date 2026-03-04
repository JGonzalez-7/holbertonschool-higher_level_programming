# SQL Introduction

Small MySQL exercises that progress from listing databases to basic CRUD, filtering, grouping, and simple aggregation.

## Requirements
- MySQL 8.0+
- Run commands as a user with privileges to create/drop databases and tables.

## Quick start
From this directory:
```bash
# Example: run a script
mysql -u <user> -p < 0-list_databases.sql

# Or inside the MySQL shell
mysql> SOURCE 1-create_database_if_missing.sql;
```

## Files
- `0-list_databases.sql` — show all databases.
- `1-create_database_if_missing.sql` — create `hbtn_0c_0` if missing.
- `2-remove_database.sql` — drop `hbtn_0c_0` if it exists.
- `3-list_tables.sql` — list tables in the current DB.
- `4-first_table.sql` — create `first_table (id, name)`.
- `5-full_table.sql` — display `CREATE TABLE` for `first_table`.
- `6-list_values.sql` — select all rows from `first_table`.
- `7-insert_value.sql` — insert row `(89, 'Best School')` into `first_table`.
- `8-count_89.sql` — count rows in `first_table` where `id = 89`.
- `9-full_creation.sql` — create `second_table (id, name, score)` and seed four rows.
- `10-top_score.sql` — list `second_table` rows ordered by highest score.
- `11-best_score.sql` — list rows with `score >= 10`, highest first.
- `12-no_cheating.sql` — set Bob's score to 10.
- `13-change_class.sql` — delete rows where `score <= 5`.
- `14-average.sql` — compute average score.
- `15-groups.sql` — group by `score`, show counts, highest count first.
- `16-no_link.sql` — list rows with non-empty `name`, ordered by score desc.

## Notes
- `first_table` and `second_table` are created in the current database; run `USE <db>;` before sourcing scripts.
- Scripts are idempotent where possible (`CREATE ... IF NOT EXISTS`, `DROP ... IF EXISTS`).
