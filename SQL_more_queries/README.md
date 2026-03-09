# SQL More Queries

Exercises covering MySQL user privileges, constraints, relational design, joins, and aggregations.

## Requirements
- MySQL 8.0+
- Ability to create users, databases, and tables on the server.

## How to run
From this directory, execute any script with MySQL:
```bash
mysql -u <user> -p < 0-privileges.sql
# or inside the MySQL prompt
mysql> SOURCE 10-genre_id_by_show.sql;
```
Load the accompanying sample databases (e.g., `hbtn_0d_usa`, `hbtn_0d_tvshows`) before running the queries that depend on them.

## Files
- `0-privileges.sql` — show grants for `user_0d_1` and `user_0d_2`.
- `1-create_user.sql` — create `user_0d_1` with full privileges.
- `2-create_read_user.sql` — create DB `hbtn_0d_2`, user `user_0d_2` with SELECT-only access.
- `3-force_name.sql` — table `force_name` with `name` NOT NULL.
- `4-never_empty.sql` — table `id_not_null` defaulting `id` to 1.
- `5-unique_id.sql` — table `unique_id` with unique `id` default 1.
- `6-states.sql` — DB `hbtn_0d_usa`, table `states(id PK, name NOT NULL)`.
- `7-cities.sql` — table `cities(id PK, state_id FK, name NOT NULL)` in `hbtn_0d_usa`.
- `8-cities_of_california_subquery.sql` — cities that belong to state `California` (subquery), ordered by `id`.
- `9-cities_by_state_join.sql` — list `city.id`, `city.name`, and state name via JOIN, ordered by city id.
- `10-genre_id_by_show.sql` — show title with each linked `genre_id` (inner join).
- `11-genre_id_all_shows.sql` — all shows with genre IDs, including shows with none (LEFT JOIN).
- `12-no_genre.sql` — shows that have no genre linked.
- `13-count_shows_by_genre.sql` — count shows per genre, descending by count.
- `14-my_genres.sql` — genres for the show `Dexter`, alphabetized.
- `15-comedy_only.sql` — titles of shows in the `Comedy` genre, sorted.
- `16-shows_by_genre.sql` — show titles with genre names (including NULL where no genre), ordered by title then genre.

## Notes
- Scripts are idempotent where possible (`CREATE ... IF NOT EXISTS`, `FLUSH PRIVILEGES`).
- Ensure you `USE <database>;` or include the DB name before running queries that assume a specific schema.
