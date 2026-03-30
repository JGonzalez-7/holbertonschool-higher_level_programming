#!/usr/bin/python3
"""Flask app that displays products from JSON or CSV files."""

from flask import Flask, render_template, request
import csv
import json

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


@app.route('/products')
def products():
    """Display products from the selected source."""
    source = request.args.get('source')
    product_id = request.args.get('id')
    products_data = []
    error = None

    if source == 'json':
        products_data = read_products_from_json()
    elif source == 'csv':
        products_data = read_products_from_csv()
    else:
        error = 'Wrong source'
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
    app.run(debug=True, port=5000)
