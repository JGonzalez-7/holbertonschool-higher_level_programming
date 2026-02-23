#!/usr/bin/python3
"""
Simple Flask API

How to run:

1. Install Flask (if not installed):
pip install Flask

2. Run using Flask CLI:
flask --app task_04_flask.py run

3. Open in browser:
http://127.0.0.1:5000

You can also test with curl:
curl http://127.0.0.1:5000/
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

# Do not include testing data when pushing.
users = {}


@app.route("/", methods=["GET"])
def home():
    """Root endpoint."""
    return "Welcome to the Flask API!"


@app.route("/status", methods=["GET"])
def status():
    """Health/status endpoint."""
    return "OK"


@app.route("/data", methods=["GET"])
def data():
    """Return a list of all usernames."""
    return jsonify(list(users.keys()))


@app.route("/users/<username>", methods=["GET"])
def get_user(username):
    """Return a user object by username."""
    user = users.get(username)
    if user is None:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user)


@app.route("/add_user", methods=["POST"])
def add_user():
    """Add a new user from JSON body."""
    payload = request.get_json(silent=True)
    if payload is None:
        return jsonify({"error": "Invalid JSON"}), 400

    username = payload.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    user = {
        "username": username,
        "name": payload.get("name"),
        "age": payload.get("age"),
        "city": payload.get("city"),
    }

    users[username] = user

    return jsonify({"message": "User added", "user": user}), 201


if __name__ == "__main__":
    app.run()
