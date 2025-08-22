# FastAPI Todo Application

A robust RESTful API for managing todo items built with FastAPI, SQLAlchemy, and Pydantic.

## Features

- CRUD operations for todo items
- Input validation using Pydantic schemas
- SQLAlchemy ORM for database operations
- Docker support for easy deployment
- Comprehensive test suite
- SQLite database for development and testing

## Prerequisites

- Python 3.11+
- Docker and Docker Compose (optional)

## Installation

### Local Development

1. Clone the repository:
```bash
git clone https://github.com/teekayyj-dotcom/Todo_app.git
cd Todo_app
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

### Using Docker

1. Build and run the containers:
```bash
docker-compose up --build
```

## API Endpoints

- `GET /todos`: List all todos
- `POST /todos`: Create a new todo
- `GET /todos/{todo_id}`: Get a specific todo
- `PUT /todos/{todo_id}`: Update a todo
- `DELETE /todos/{todo_id}`: Delete a todo

## Running Tests

To run the test suite:

```bash
TESTING=1 PYTHONPATH=. pytest tests/test_fastapi.py -v
```

## Project Structure

```
├── app/
│   ├── __init__.py
│   ├── crud.py         # Database CRUD operations
│   ├── database.py     # Database configuration
│   ├── models.py       # SQLAlchemy models
│   └── schemas.py      # Pydantic models for validation
├── tests/              # Test suite
├── docker-compose.yml  # Docker Compose configuration
├── Dockerfile          # Docker configuration
└── requirements.txt    # Python dependencies
```

## Development

The application uses:
- FastAPI for the web framework
- SQLAlchemy for ORM
- Pydantic for data validation
- SQLite for the database
- pytest for testing

