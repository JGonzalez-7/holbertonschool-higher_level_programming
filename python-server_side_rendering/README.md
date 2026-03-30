# Python Server Side Rendering

This directory contains a small progression of Python and Flask exercises focused on server-side rendering, template reuse, file-based data loading, and basic database-backed views.

## Contents

- `task_00_intro.py`: Generates invitation text files from a template and attendee data.
- `task_01_jinja.py`: Basic Flask app with reusable Jinja templates.
- `task_02_logic.py`: Adds dynamic rendering of items from `items.json`.
- `task_03_files.py`: Displays products from either `products.json` or `products.csv`.
- `task_04_db.py`: Extends the product view to support SQLite data from `products.db`.
- `products_populate.py`: Creates and populates the SQLite database used by `task_04_db.py`.
- `template.txt`: Source template used for invitation generation.
- `items.json`: Sample JSON data for the `/items` route.
- `products.json`: Sample product data in JSON format.
- `products.csv`: Sample product data in CSV format.
- `templates/`: Shared Jinja templates and page views.

## Templates

The `templates/` directory includes:

- `header.html` and `footer.html` for reusable layout sections
- `index.html`, `about.html`, and `contact.html` for static pages
- `items.html` for rendering a list of items from JSON
- `product_display.html` for rendering product data or error messages

## Requirements

- Python 3
- Flask

Install Flask if needed:

```bash
pip install flask
```

## Running The Files

Run commands from inside this directory so relative paths like `items.json`, `products.json`, and `products.csv` resolve correctly.

```bash
cd python-server_side_rendering
```

### 1. Invitation Generator

`task_00_intro.py` defines `generate_invitations(template, attendees)`. It does not start a web server by itself. Import it into Python or another script and pass:

- a string template with placeholders like `{name}` and `{event_title}`
- a list of attendee dictionaries

Example placeholders supported:

- `name`
- `event_title`
- `event_date`
- `event_location`

Generated files are written as `output_1.txt`, `output_2.txt`, and so on.

### 2. Basic Flask App

```bash
python3 task_01_jinja.py
```

Available routes:

- `/`
- `/about`
- `/contact`

### 3. Flask App With JSON Data

```bash
python3 task_02_logic.py
```

Available routes:

- `/`
- `/about`
- `/contact`
- `/items`

The `/items` route reads from `items.json` and renders the list in `templates/items.html`.

### 4. Product Display From JSON or CSV

```bash
python3 task_03_files.py
```

Use the `/products` route with a `source` query parameter:

- `/products?source=json`
- `/products?source=csv`

Optional filtering by product id:

- `/products?source=json&id=1`
- `/products?source=csv&id=2`

Behavior:

- invalid or missing `source` returns `Wrong source`
- invalid or missing product id match returns `Product not found`

### 5. Product Display With SQLite Support

Create and populate the database first:

```bash
python3 products_populate.py
```

Then start the app:

```bash
python3 task_04_db.py
```

Supported sources:

- `/products?source=json`
- `/products?source=csv`
- `/products?source=sql`

Optional filtering:

- `/products?source=sql&id=1`

Behavior:

- invalid or missing `source` returns `Wrong source`
- missing product match returns `Product not found`
- file/database read problems return `Database error`

## Notes

- All Flask apps run on port `5000` with `debug=True`.
- `task_04_db.py` expects a SQLite database file named `products.db`.
- `products_populate.py` creates the `Products` table and inserts two sample rows: `Laptop` and `Coffee Mug`.
- `product_display.html` renders a table when products are available and an error message otherwise.
