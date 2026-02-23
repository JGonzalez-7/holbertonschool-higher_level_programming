# Consume Data from an API Using Command Line Tools (curl)

## Introduction

curl (Client URL) is a command-line tool used to transfer data from or to a server using protocols such as HTTP and HTTPS. It is commonly used to test APIs, debug endpoints, and interact with RESTful web services directly from the terminal.

---

## 1. Installing and Verifying curl

### Installation

On macOS or Linux:

curl is usually preinstalled. If not:

Ubuntu/Debian:
sudo apt install curl

macOS (Homebrew):
brew install curl

On Windows:
Use Windows Subsystem for Linux (WSL) or download curl from the official website.

---

### Verify Installation

Run:

curl --version

Expected Output:
- curl version number
- Supported protocols (http, https, ftp, etc.)
- SSL/TLS support details

Example:

curl 8.0.1 (x86_64-pc-linux-gnu)
Protocols: dict file ftp ftps http https ...
Features: SSL IPv6 libz ...

---

## 2. Fetching Data from a Webpage

Basic GET request:

curl http://example.com

This retrieves the HTML content of the webpage and prints it to the terminal.

---

## 3. Fetching Data from an API

Public API used: JSONPlaceholder  
https://jsonplaceholder.typicode.com

### Retrieve Posts

Run:

curl https://jsonplaceholder.typicode.com/posts

Expected Output:
A JSON array of posts.

Example:

[
  {
    "userId": 1,
    "id": 1,
    "title": "sunt aut facere repellat",
    "body": "quia et suscipit..."
  },
  ...
]

Each post contains:
- userId
- id
- title
- body

---

## 4. Fetch Only Headers

Use the -I flag:

curl -I https://jsonplaceholder.typicode.com/posts

Expected Output:
- HTTP status line
- Response headers only

Example:

HTTP/2 200
content-type: application/json; charset=utf-8
cache-control: max-age=43200
...

The -I option is useful for:
- Checking status codes
- Viewing content type
- Inspecting caching rules

---

## 5. Making a POST Request

Use the -X flag to specify the method and -d to send data.

Example:

curl -X POST \
-d "title=foo&body=bar&userId=1" \
https://jsonplaceholder.typicode.com/posts

Expected Output:

{
  "title": "foo",
  "body": "bar",
  "userId": "1",
  "id": 101
}

Explanation:
- -X POST specifies the HTTP method.
- -d sends data in the request body.
- JSONPlaceholder simulates creation and returns id 101.

---

## 6. Useful curl Flags

| Flag | Purpose |
|------|----------|
| -I | Fetch headers only |
| -X | Specify HTTP method |
| -d | Send data in request body |
| -H | Add custom headers |
| -v | Verbose output |
| -o | Save output to file |

Example with header:

curl -H "Content-Type: application/json" \
-X POST \
-d '{"title":"foo","body":"bar","userId":1}' \
https://jsonplaceholder.typicode.com/posts

---

## 7. Formatting JSON Output

To format JSON output clearly, pipe it into jq:

curl https://jsonplaceholder.typicode.com/posts | jq

This makes JSON easier to read and debug.

---

## Final Summary

curl is a powerful command-line tool for interacting with APIs.

Using curl, you can:
- Send GET requests to retrieve data
- Inspect response headers
- Send POST requests with data
- Add custom headers
- Debug and test RESTful APIs directly from the terminal
