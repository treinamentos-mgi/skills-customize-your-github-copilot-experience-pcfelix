from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI(title="Books API")


class BookCreate(BaseModel):
    # TODO: Add title, author, and year fields.
    pass


class Book(BookCreate):
    # TODO: Add the book ID field.
    pass


books: dict[int, Book] = {}


@app.get("/books", response_model=list[Book])
def list_books():
    # TODO: Return all books.
    pass


@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int):
    # TODO: Return the book or raise HTTPException with status code 404.
    pass


@app.post("/books", response_model=Book, status_code=status.HTTP_201_CREATED)
def create_book(book_data: BookCreate):
    # TODO: Assign an ID, store the book, and return it.
    pass


@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, book_data: BookCreate):
    # TODO: Replace the book or raise HTTPException with status code 404.
    pass


@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int):
    # TODO: Delete the book or raise HTTPException with status code 404.
    pass


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)