from fastapi import FastAPI, HTTPException
import asyncio
from pydantic import BaseModel, Field, field_validator
from typing import List, Optional, Union
from datetime import datetime

app = FastAPI()

books_db = [
    {"id": 1, "title": "1984", "author": "George Orwell", "year": 1949},
    {"id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960},
    {"id": 3, "title": "Brave New World", "author": "Aldous Huxley", "year": 1932},
]

class Books(BaseModel):
    id: int
    title: str = Field(..., max_length=100, description="책 제목")
    author: str = Field(..., max_length=100, description="책 저자")
    year: int = Field(..., gt=0, lt=10000, description="책 출판년도")

#모든 책 조회
@app.get("/books/")
def get_books():
    return {"Books":books_db}

#특정 책 조회
@app.get("/books/{book_id}")
def get_book(book_id: int):
    for book in books_db:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")

#특정작가의 책 조회
@app.get("/books/search")
def get_books_by_author(author: str):
    books_by_author = []
    for book in books_db:
        if book["author"] == author:
            books_by_author.append(book)
            
    if books_by_author:
        return books_by_author
    raise HTTPException(status_code=404, detail="No books found for this author")

