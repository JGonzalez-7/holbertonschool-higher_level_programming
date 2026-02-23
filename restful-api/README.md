# RESTful API Exercises

Small progression from HTTP basics to building and securing simple APIs in Python.

## Contents
- `task_00_requests.md`: HTTP vs HTTPS, request/response structure, methods, common status codes.
- `task_01_requests.md`: Using `curl` to call APIs (GET, POST, headers, JSON formatting with `jq`).
- `task_02_requests.py`: Consume JSONPlaceholder posts with `requests`; print titles or save to `posts.csv`.
- `task_03_http_server.py`: Minimal API using Python's `http.server` on port 8000.
- `task_04_flask.py`: Basic Flask API with in-memory users.
- `task_05_basic_security.py`: Flask API showing Basic Auth and JWT protection.

## Requirements
- Python 3.8+
- Install deps (consider a venv):
  ```bash
  python3 -m venv .venv && source .venv/bin/activate
  pip install requests Flask Flask-HTTPAuth Flask-JWT-Extended
  ```

## Task notes & how to run
### 0) HTTP primer (`task_00_requests.md`)
Read for protocol overview: HTTPS vs HTTP, request/response anatomy, CRUD-to-verb mapping, frequent status codes.

### 1) Calling APIs with curl (`task_01_requests.md`)
Examples include:
- Fetch posts: `curl https://jsonplaceholder.typicode.com/posts`
- Headers only: `curl -I https://jsonplaceholder.typicode.com/posts`
- POST form or JSON bodies with `-d` / `-H`.

### 2) Python requests (`task_02_requests.py`)
- Print status + titles:
  ```bash
  python3 -c "from task_02_requests import fetch_and_print_posts; fetch_and_print_posts()"
  ```
- Save `id/title/body` to `posts.csv`:
  ```bash
  python3 -c "from task_02_requests import fetch_and_save_posts; fetch_and_save_posts()"
  ```
  Output file appears in this folder.

### 3) Built-in HTTP server (`task_03_http_server.py`)
Start the server:
```bash
python3 task_03_http_server.py
```
Endpoints (port 8000):
- `/` → greeting text
- `/status` → `OK`
- `/data` → sample JSON user
- `/info` → version/description metadata

### 4) Flask API (`task_04_flask.py`)
Run with Flask CLI (recommended):
```bash
flask --app task_04_flask.py run
```
Key routes (in-memory `users` dict):
- `/` greeting, `/status` health
- `/data` list of usernames
- `/users/<username>` get a user or 404
- `/add_user` POST JSON `{username, name, age, city}` to create (409 on duplicate)

### 5) Basic Auth + JWT (`task_05_basic_security.py`)
Run (note the filename differs from the comment inside the file):
```bash
flask --app task_05_basic_security.py run
```
Default users: `user1:password` (role user), `admin1:password` (role admin).
- Basic Auth example: `curl -u user1:password http://127.0.0.1:5000/basic-protected`
- Get JWT: `curl -X POST -H "Content-Type: application/json" -d '{"username":"admin1","password":"password"}' http://127.0.0.1:5000/login`
- Use JWT: `curl -H "Authorization: Bearer <token>" http://127.0.0.1:5000/jwt-protected`
- Admin-only: same JWT header to `/admin-only` (403 for non-admins)

## Tips
- Scripts are for local practice only (in-memory data, hard-coded secrets). Do not deploy as-is.
- Lint with `pycodestyle *.py` to match Holberton style guidelines.
