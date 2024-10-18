from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy import update

from models import Book, PageCount
from engine import get_engine


engine = get_engine()
session = Session(engine)

while True:
    ans = input("Do you want to update page count (y/n)? ")
    if ans in "yesno":
        break

if ans in "yes":
    new_count = int(input("New page count: "))
    query = select(PageCount).where(PageCount.book_id == 1)
    page = session.scalars(query).one()
    page.page = new_count
    session.commit()
elif ans in "no":
    books = session.scalars(select(Book))
    pages = session.scalars(select(PageCount))
    ids_pages = {}

    for book in books:
        for page in pages:
            if book.id == page.book_id:
                print(book.id, book.title)
                ids_pages[book.id] = page.page
                
    ids = list(ids_pages.keys())
    while True:
        choice = int(input(f"\nChoose book ({min(ids)}-{max(ids)}): "))
        if choice in ids:
            print(ids_pages[choice])
            break
    
                   
