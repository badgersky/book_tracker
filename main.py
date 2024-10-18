from sqlalchemy import select
from sqlalchemy.orm import Session

from models import Book, PageCount
from engine import get_engine


engine = get_engine()
session = Session(engine)

books = session.scalars(select(Book))
pages = session.scalars(select(PageCount))

print("Choose book")
ids_pages = {}

for book in books:
    for page in pages:
        if book.id == page.book_id:
            print(book.id, book.title)
            ids_pages[book.id] = page.page
            
ids = list(ids_pages.keys())
while True:
    choice = int(input(f"Choose book ({min(ids)}-{max(ids)}): "))
    if choice in ids:
        print(ids_pages[choice])
    
                   
