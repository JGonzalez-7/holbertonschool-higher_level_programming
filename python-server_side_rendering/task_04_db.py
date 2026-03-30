#!/usr/bin/python3
"""Flask app that displays products from JSON, CSV, or SQLite."""

from flask import Flask, render_template, request
import csv
import json
import sqlite3

app = Flask(__name__)


def read_products_from_json():
    """Read product data from a JSON file."""
    with open('products.json', 'r', encoding='utf-8') as file:
        return json.load(file)


def read_products_from_csv():
    """Read product data from a CSV file."""
    products = []

    with open('products.csv', 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            products.append({
                'id': int(row['id']),
                'name': row['name'],
                'category': row['category'],
                'price': float(row['price'])
            })

    return products


def read_products_from_sql():
    """Read product data from the SQLite database."""
    conn = sqlite3.connect('products.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute('SELECT id, name, category, price FROM Products')
    rows = cursor.fetchall()
    conn.close()

    products = []
    for row in rows:
        products.append({
            'id': row['id'],
            'name': row['name'],
            'category': row['category'],
            'price': row['price']
        })

    return products


@app.route('/products')
def products():
    """Display products from the selected source."""
    source = request.args.get('source')
    product_id = request.args.get('id')
    products_data = []
    error = None

    try:
        if source == 'json':
            products_data = read_products_from_json()
        elif source == 'csv':
            products_data = read_products_from_csv()
        elif source == 'sql':
            products_data = read_products_from_sql()
        else:
            error = 'Wrong source'
            return render_template(
                'product_display.html',
                products=[],
                error=error
            )
    except (OSError, json.JSONDecodeError, sqlite3.Error, ValueError):
        error = 'Database error'
        return render_template(
            'product_display.html',
            products=[],
            error=error
        )

    if product_id is not None:
        try:
            product_id = int(product_id)
            products_data = [
                product for product in products_data
                if product['id'] == product_id
            ]
            if not products_data:
                error = 'Product not found'
        except ValueError:
            error = 'Product not found'
            products_data = []

    return render_template(
        'product_display.html',
        products=products_data,
        error=error
    )


if __name__ == '__main__':
    app.run(debug=True, port=5500)
