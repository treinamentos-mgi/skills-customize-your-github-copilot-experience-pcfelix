# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small REST API for managing books with FastAPI. Practice defining request models, creating HTTP endpoints, and returning appropriate status codes.

## 📝 Tasks

### 🛠️ Define the data model and read endpoints

#### Description

Define the book data models and implement endpoints that list the books or retrieve one book by its ID.

#### Requirements

The completed program must:

- Define a `BookCreate` model with `title`, `author`, and `year` fields, and a `Book` model that also includes an `id`.
- Return all stored books from `GET /books`.
- Return a book by ID from `GET /books/{book_id}`.
- Return HTTP 404 when the requested book ID does not exist.

### 🛠️ Add and test CRUD endpoints

#### Description

Complete the API so clients can create, update, and delete books, then try the endpoints using FastAPI's interactive documentation. Install the dependencies with `python -m pip install fastapi uvicorn` and run `python starter-code.py` from the assignment directory.

#### Requirements

The completed program must:

- Create a book with `POST /books` and return the created book with HTTP 201.
- Replace an existing book with `PUT /books/{book_id}` and return HTTP 404 if its ID does not exist.
- Delete an existing book with `DELETE /books/{book_id}` and return HTTP 204; return HTTP 404 if its ID does not exist.
- Run the API locally and verify the endpoints at `http://127.0.0.1:8000/docs`.

For `POST /books` and `PUT /books/{book_id}`, use a JSON request body such as:

```json
{
  "title": "The Hobbit",
  "author": "J.R.R. Tolkien",
  "year": 1937
}
```