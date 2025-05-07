from fastapi import FastAPI
from models import Book

app = FastAPI()

catalog: list[Book] = []

# GET / : Returns a greeting message
@app.get("/")
def read_root():
    return {"Hello": "World"}

# GET /books : Returns the list of all books in the catalog
@app.get("/books")
def get_books():
    return catalog

# GET /books/onshelf : Returns the list of books that are currently on the shelf
@app.get("/books/onshelf")
def get_onshelf_books():
    return [book for book in catalog if book.onshelf == True]

# GET /books/{bookid} : Returns the details of a specific book by its ID
@app.get("/books/{bookid}")
def get_book(bookid: int):
    for book in catalog:
        if book.bookid == bookid:
            return book
    return {"error": "Book not found"}

# POST /books : Adds a new book to the catalog
@app.post("/books/{bookid}")
def add_book(book: Book):
    catalog.append(book)
    return book

# PUT /books/{bookid} : Updates the details of a specific book by its ID
@app.put("/books/{bookid}")
def update_book(bookid: int, book: Book):
    for i, b in enumerate(catalog):
        if b.bookid == bookid:
            catalog[i] = book
            return book
    return {"error": "Book not found"}

# DELETE /books/{bookid} : Deletes a specific book by its ID. Note that this operation is highly discouraged since it deletes historical records of books that have been in the catalog. Instead, consider using the put operation to update the onshelf field to False.
@app.delete("/books/{bookid}")
def delete_book(bookid: int):
    for i, b in enumerate(catalog):
        if b.bookid == bookid:
            del catalog[i]
            return {"message": "Book deleted"}
    return {"error": "Book not found"}