# Basic API using FastAPI

## Setup Requirements

This project begins with setting up a virtual environment in the main area of this repository. To establish the virtual environment, the following steps were taken:
 1. Check to see which python is currently being used. The output is used as a method of comparison from initial to final state. ``which python``
 2. Use a standard command to establish a virtual environment. ``py -m venv .venv``
 3. Activate the virtual environment. ``source .venv/Scripts/activate``
 4. Verify that the python in the virtual environment is being used. ``which python``

Next, I updated ``pip`` using the command ``py -m pip install --upgrade pip``.

Finally, I installed FastAPI with the command ``pip install "fastapi[standard]"``. This installation method also installed uvicorn and pydantic packages, which is necessary for this solution.

## Class ERD
This diagram was used to validate the pydanic model ``Book`` in the ``models.py`` file.  
![ERD diagram for little library catalog](/section1/erd.png)

## Code
I began by defining the `Book` model in `models.py`.

```python
import datetime
from pydantic import BaseModel

class Book(BaseModel):
    bookid: int
    title: str
    author: str
    date_donated: datetime.date
    onshelf: bool = True
```

Next, I imported the `Book` model into `main.py` and developed prototype CRUD operations.

```python
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
```

## Execution
This API can be executed by using the following command: ``uvicode main:app --reload``