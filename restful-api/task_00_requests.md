# Basics of HTTP/HTTPS

## Introduction

The Hypertext Transfer Protocol (HTTP) is the foundation of communication on the web. It allows clients (such as browsers or API consumers) to communicate with servers. HTTPS is the secure version of HTTP, adding encryption using SSL/TLS to protect data in transit.

---

## 1. Differences Between HTTP and HTTPS

### HTTP

HTTP (Hypertext Transfer Protocol) is an application-layer protocol used for transmitting data over the web.

Characteristics:
- Sends data in plain text
- Stateless protocol
- Default port: 80
- No built-in encryption
- Vulnerable to eavesdropping and data tampering

---

### HTTPS

HTTPS (HTTP Secure) is HTTP with encryption using SSL/TLS.

Characteristics:
- Encrypts data between client and server
- Default port: 443
- Uses digital certificates for authentication
- Protects sensitive information such as passwords and payment data

---

### Main Differences

| Feature | HTTP | HTTPS |
|----------|--------|----------|
| Encryption | No | Yes (SSL/TLS) |
| Security | Vulnerable | Secure |
| Default Port | 80 | 443 |
| Use Case | Non-sensitive data | Sensitive data (login, banking, APIs) |
| SEO Ranking | Lower | Higher |

---

## 2. Structure of an HTTP Request and Response

### HTTP Request Structure

Example:

GET /index.html HTTP/1.1  
Host: example.com  
User-Agent: Mozilla/5.0  
Accept: text/html  

Components:

1. Request Line  
   Format: METHOD PATH VERSION  
   Example:  
   GET /api/users HTTP/1.1  

2. Headers  
   Provide metadata about the request. Examples:
   - Host
   - User-Agent
   - Content-Type
   - Authorization

3. Body (Optional)  
   Used mainly with POST, PUT, and PATCH to send data (often JSON).

---

### HTTP Response Structure

Example:

HTTP/1.1 200 OK  
Content-Type: text/html  
Content-Length: 1234  

<html>...</html>

Components:

1. Status Line  
   Format: VERSION STATUS_CODE STATUS_MESSAGE  

2. Headers  
   Examples:
   - Content-Type
   - Content-Length
   - Set-Cookie

3. Body  
   Contains the returned resource (HTML, JSON, file, etc.).

---

## 3. Common HTTP Methods

| Method | Description | Use Case |
|--------|-------------|-----------|
| GET | Retrieves data | Fetching data from an API |
| POST | Creates a new resource | Registering a new user |
| PUT | Updates an entire resource | Updating a full user profile |
| PATCH | Updates part of a resource | Changing only a password |
| DELETE | Removes a resource | Deleting an account |

---

### CRUD Mapping in REST APIs

| CRUD Operation | HTTP Method |
|---------------|------------|
| Create | POST |
| Read | GET |
| Update | PUT / PATCH |
| Delete | DELETE |

---

## 4. Common HTTP Status Codes

Status codes are grouped by their first digit:

- 1xx — Informational
- 2xx — Success
- 3xx — Redirection
- 4xx — Client Error
- 5xx — Server Error

---

### Five Common Status Codes

| Code | Description | Scenario |
|------|-------------|-----------|
| 200 OK | Request succeeded | API returned data successfully |
| 201 Created | Resource created | New user account created |
| 301 Moved Permanently | Redirected | Website redirected to HTTPS |
| 404 Not Found | Resource not found | Invalid endpoint requested |
| 500 Internal Server Error | Server failure | Backend application crashed |

---

## Final Summary

HTTP is a stateless protocol used for web communication but does not encrypt data. HTTPS is the secure version of HTTP and uses SSL/TLS encryption to protect transmitted data.

An HTTP request consists of a request line, headers, and optionally a body.  
An HTTP response consists of a status line, headers, and a body.

Common HTTP methods include GET, POST, PUT, PATCH, and DELETE.  
Common HTTP status codes include 200, 201, 301, 404, and 500.