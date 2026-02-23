#!/usr/bin/python3
"""
Consuming and processing data from an API using Python
"""

import csv
import requests


URL = "https://jsonplaceholder.typicode.com/posts"


def fetch_and_print_posts():
    """
    Fetch all posts and print the response status code and each post title.
    """
    response = requests.get(URL, timeout=10)
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post.get("title", ""))
    else:
        # helpful for debugging
        print("Request failed.")


def fetch_and_save_posts():
    """
    Fetch all posts and save id, title, and body to posts.csv.
    """
    response = requests.get(URL, timeout=10)

    if response.status_code == 200:
        posts = response.json()

        data = [
            {
                "id": post.get("id"),
                "title": post.get("title"),
                "body": post.get("body"),
            }
            for post in posts
        ]

        with open("posts.csv", mode="w", newline="", encoding="utf-8") as f:
            fieldnames = ["id", "title", "body"]
            writer = csv.DictWriter(f, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(data)
    else:
        print("Request failed. CSV not created.")
