from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy import update

from models import Book, PageCount
from engine import get_engine


engine = get_engine()
session = Session(engine)
books = session.scalars(select(Book))
ids_titles = {book.id: book.title for book in books}

print("Books in database:")
for i, t in ids_titles.items():
    print(f"{i}: {t}")

print("\n")
while True:
    try:
        ans1 = int(input(f"Choose id ({min(ids_titles.keys())}-{max(list(ids_titles.keys()))}): "))
    except ValueError:
        continue
    else:
        if ans1 not in list(ids_titles.keys()):
            print("that book doesn`t exist")
        else:
            break

query = select(PageCount).where(PageCount.book_id == ans1)
page = session.scalars(query).one()

while True:
    ans2 = input("Do you want to change page count (y/n)? ")
    if ans2 in "yes":
        try:
            new_count = int(input("New page count: "))
        except ValueError:
            continue
        else:
            page.page = new_count
            session.commit()
            break
    elif ans2 in "no":
        print(f"Current page count: {page.page}")
        break
