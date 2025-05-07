import datetime
from pydantic import BaseModel

class Book(BaseModel):
    bookid: int
    title: str
    author: str
    date_donated: datetime.date
    onshelf: bool = True