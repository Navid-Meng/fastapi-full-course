from fastapi import FastAPI, HTTPException, Query, Body
from typing import Optional as Opt

app = FastAPI()

books = [
    { 'id': 1, 'title': 'Title One',   'author': 'Author One', "price": 10, "year": 2015 },
    { 'id': 2, 'title': 'Title Two',   'author': 'Author One', "price": 20, "year": 2015  },
    { 'id': 3, 'title': 'Title Three', 'author': 'Author Three', "price": 30, "year": 2025  },
    { 'id': 4, 'title': 'Title Four',  'author': 'Author Four', "price": 40, "year": 2018  },
    { 'id': 5, 'title': 'Title Five',  'author': 'Author Five', "price": 50, "year": 2018  }
]

@app.get('/')
async def index():
    return { 'message': 'go to /docs for documentations' }

@app.get("/books")
async def get_books(
    author: Opt[str] = Query(None, description='Filter by author'),
    title: Opt[str] = Query(None, description='Filter by title'),
    min_price: Opt[float] = Query(None, description='Filter by max price'),
    max_price: Opt[float] = Query(None, description='Filter by min price'),
    year: Opt[int] = Query(None, description='Filter by year')
):
    result = books
    
    if author: 
        result = [book for book in result if author.lower() in book['author'].lower()]
    if title:
        result = [book for book in result if title.lower() in book['title'].lower()]
    if min_price:
        result = [book for book in result if book['price'] >= min_price]
    if max_price:
        result = [book for book in result if book['price'] <= max_price]
    if year:
        result = [book for book in result if book['year'] == year]
    
    return result

@app.get("/books/{book_id}")
async def get_book(book_id: str):
    for book in books:
        if book['id'] == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found!")

@app.post("/books")
async def create_book(new_book = Body()):
    books.append(new_book)
    return new_book