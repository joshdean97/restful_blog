# 📘 RESTful Blog API

A clean, production-style RESTful API for a blogging platform, built with Flask.
This project demonstrates proper API design, CRUD operations, pagination, filtering, validation, and separation of concerns.

This is my first portfolio project focused specifically on REST API fundamentals, rather than frontend output.

## 🚀 Features

- Full CRUD support for blog posts
- REST-correct routing and HTTP methods
- Request validation and serialization with Marshmallow
- Pagination and filtering via query parameters
- Search across multiple fields
- JSON-based tag support
- Clean project structure using Blueprints and extensions
- SQLite database with SQLAlchemy ORM

## 🧠 What This Project Demonstrates

This project intentionally focuses on backend fundamentals:

- Designing resource-based REST endpoints
- Proper use of HTTP verbs (GET, POST, PUT, DELETE)
- Schema-based validation and serialization
- Query building with SQLAlchemy
- Pagination, filtering, and search
- Clean separation between models, schemas, and routes
- Defensive API design (limits, validation errors, safe updates)

## 🛠️ Tech Stack

- Python
- Flask
- Flask Blueprints
- SQLAlchemy (ORM)
- Marshmallow
- SQLite
- Flask-Migrate

## 📂 Project Structure

```
core/
├── extensions.py   # db, marshmallow, migrations
├── models.py       # SQLAlchemy models
├── schemas.py      # Marshmallow schemas
├── routes/
│   └── blog.py     # Blog API routes
├── __init__.py     # App factory
app.py              # App entry point
```

This structure mirrors how production Flask APIs are typically organised.

## ▶️ Running the Project Locally

### Prerequisites

- Python 3.10+
- pip
- (Recommended) a virtual environment

### 1️⃣ Clone the repository
```bash
git clone <your-repo-url>
cd restful-blog
```

### 2️⃣ Create and activate a virtual environment

**macOS / Linux**
```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows**
```bash
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Run database migrations
```bash
flask db upgrade
```
*(If running for the first time, ensure the database is created.)*

### 5️⃣ Start the application
```bash
python app.py
```

The API will be available at: `http://127.0.0.1:5000`

### 6️⃣ Test the API

You can test endpoints using:
- Postman
- curl
- HTTPie
- a frontend client

Example:
```bash
curl http://127.0.0.1:5000/blog
```

### 🧼 Notes

- This project uses SQLite for simplicity
- Environment isolation via venv is recommended
- Pagination defaults to 10 items per page, capped at 50

## 📡 API Endpoints

### Create a post
```
POST /blog

{
    "title": "My first post",
    "content": "Hello world",
    "category": "tech",
    "tags": ["flask", "api"],
    "author": "Josh"
}
```

### Get all posts (with pagination & filters)
```
GET /blog?page=1&per_page=10&search=flask&category=tech&tag=api
```

### Get a single post
```
GET /blog/<id>
```

### Update a post (partial update)
```
PUT /blog/<id>

{
    "title": "Updated title"
}
```

### Delete a post
```
DELETE /blog/<id>
```

## 🧪 Validation & Error Handling

- Requests are validated using Marshmallow schemas
- Invalid input returns structured 400 responses
- Updates support partial payloads
- Pagination limits prevent excessive queries

## 🧩 Project Origin

This project is based on a backend roadmap challenge, but extended beyond the brief to include:

- Schema-based updates
- Filtering & search
- Pagination
- Clean architecture

**Original challenge:** https://roadmap.sh/projects/blogging-platform-api

## 🔮 Possible Next Improvements

- Authentication & authorization
- Role-based access (admin vs public)
- Full-text search (PostgreSQL)
- OpenAPI / Swagger documentation
- Dockerisation
- Rate limiting

## 👤 Author

**Josh Shepherd**  
Backend Developer  
Focused on Python, REST APIs, and clean backend architecture.
