from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Dict, Any

from crud import create_book, get_book, get_all_books, update_book, delete_book, create_user, get_user, get_all_users, \
    update_user, delete_user, create_loan, get_loan, get_all_loans, update_loan, delete_loan, get_db
from schemas import BookBase, Book, UserBase, User, LoanBase, Loan, BookCreate
from sqlalchemy import text
from assertpy import assert_that
from fastapi.logger import logger

router = APIRouter()

BOOK_NOT_FOUND_ERROR = "Book not found."


# operaciones CRUD para libros
@router.post("/books", response_model=Book)
def create_new_book(book: BookCreate, db: Session = Depends(get_db)):
    new_book = create_book(db, book)
    return new_book


@router.get("/books/{book_id}", response_model=Book)
def get_one_book(book_id: int, db: Session = Depends(get_db)):
    book = get_book(db, book_id)
    if book is None:
        raise HTTPException(status_code=404, detail=BOOK_NOT_FOUND_ERROR)
    return book


@router.get("/books", response_model=List[Book])
def get_all_books_list(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    try:
        books = get_all_books(db, skip, limit)
        assert_that(books).is_not_none()
        assert_that(books).is_not_empty()
        # assert_that(len(books)).is_greater_than_or_equal_to(10), "La cantidad de Libros es muy baja"
        return books
    except Exception:
        logger.exception("500 Internal Server Error")
        raise HTTPException(status_code=500, detail="Error Interno del servido")


@router.put("/books/{book_id}", response_model=Book)
def update_book_by_id(book_id: int, book: BookBase, db: Session = Depends(get_db)):
    updated_book = update_book(db, book_id, book)
    if updated_book is None:
        raise HTTPException(status_code=404, detail=BOOK_NOT_FOUND_ERROR)
    return updated_book


@router.delete("/books/{book_id}")
def delete_book_by_id(book_id: int, db: Session = Depends(get_db)):
    deleted_book = delete_book(db, book_id)
    if deleted_book is None:
        raise HTTPException(status_code=404, detail=BOOK_NOT_FOUND_ERROR)
    return deleted_book


# operaciones CRUD para usuarios
@router.post("/users", response_model=User)
def create_new_user(user: UserBase, db: Session = Depends(get_db)):
    new_user = create_user(db, user)
    return new_user


@router.get("/users/{user_id}", response_model=User)
def get_one_user(user_id: int, db: Session = Depends(get_db)):
    user = get_user(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found.")
    return user


@router.get("/users", response_model=List[User])
def get_all_users_list(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = get_all_users(db, skip, limit)
    return users


@router.put("/users/{user_id}", response_model=User)
def update_user_by_id(user_id: int, user: UserBase, db: Session = Depends(get_db)):
    updated_user = update_user(db, user_id, user)
    if updated_user is None:
        raise HTTPException(status_code=404, detail="User not found.")
    return updated_user


@router.delete("/users/{user_id}")
def delete_user_by_id(user_id: int, db: Session = Depends(get_db)):
    deleted_user = delete_user(db, user_id)
    if deleted_user is None:
        raise HTTPException(status_code=404, detail="User not found.")
    return deleted_user


@router.post("/loans", response_model=Loan)
def create_new_loan(loan: LoanBase, db: Session = Depends(get_db)):
    new_loan = create_loan(db, loan)
    return new_loan


@router.get("/loans/{loan_id}", response_model=Loan)
def get_one_loan(loan_id: int, db: Session = Depends(get_db)):
    loan = get_loan(db, loan_id)
    if loan is None:
        raise HTTPException(status_code=404, detail="Loan not found.")
    return loan


@router.get("/loans", response_model=List[Loan])
def get_all_loans_list(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    loans = get_all_loans(db, skip, limit)
    return loans


@router.put("/loans/{loan_id}", response_model=Loan)
def update_loan_by_id(loan_id: int, loan: LoanBase, db: Session = Depends(get_db)):
    updated_loan = update_loan(db, loan_id, loan)
    if updated_loan is None:
        raise HTTPException(status_code=404, detail="Loan not found.")
    return updated_loan


@router.delete("/loans/{loan_id}")
def delete_loan_by_id(loan_id: int, db: Session = Depends(get_db)):
    deleted_loan = delete_loan(db, loan_id)
    if deleted_loan is None:
        raise HTTPException(status_code=404, detail="Loan not found.")
    return deleted_loan


@router.get("/vista_prestamos", response_model=List[Dict[str, Any]])
def get_vista_prestamos(db: Session = Depends(get_db)):
    query = text('SELECT * FROM vista_prestamos')
    result = db.execute(query)
    columns = result.keys()
    return [dict(zip(columns, row)) for row in result]
