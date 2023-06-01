from pydantic import parse_obj_as
from sqlalchemy.orm import Session

from config import SessionLocal
from model import Book as ModelBook
from model import Loan as ModelLoan
from model import User as ModelUser
from schemas import BookBase, UserBase, LoanBase, Loan, BookCreate, UserCreate, LoanOut


# función para obtener una sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# operaciones CRUD para libros
def create_book(db: Session, book: BookCreate):
    new_book = ModelBook(**book.dict())
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book


def get_book(db: Session, book_id: int):
    return db.query(ModelBook).filter(ModelBook.id == book_id).first()


def get_all_books(db: Session, skip: int = 0, limit: int = 100):
    return db.query(ModelBook).offset(skip).limit(limit).all()


def update_book(db: Session, book_id: int, book: BookBase):
    db.query(ModelBook).filter(ModelBook.id == book_id).update(book.dict())
    db.commit()
    return get_book(db, book_id)


def delete_book(db: Session, book_id: int):
    db.query(ModelBook).filter(ModelBook.id == book_id).delete()
    db.commit()
    return {"message": "Book deleted successfully."}


# operaciones CRUD para usuarios
def create_user(db: Session, user: UserCreate):
    new_user = ModelUser(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_user(db: Session, user_id: int):
    return db.query(ModelUser).filter(ModelUser.id == user_id).first()


def get_all_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(ModelUser).offset(skip).limit(limit).all()


def update_user(db: Session, user_id: int, user: UserBase):
    db.query(ModelUser).filter(ModelUser.id == user_id).update(user.dict())
    db.commit()
    return get_user(db, user_id)


def delete_user(db: Session, user_id: int):
    db.query(ModelUser).filter(ModelUser.id == user_id).delete()
    db.commit()
    return {"message": "User deleted successfully."}


# operaciones CRUD para préstamos
def create_loan(db: Session, loan: LoanBase):
    new_loan = ModelLoan(**loan.dict())
    db.add(new_loan)
    db.commit()
    db.refresh(new_loan)
    return new_loan


def get_loan(db: Session, loan_id: int):
    return parse_obj_as(LoanOut, db.query(ModelLoan).filter(ModelLoan.id == loan_id).first())


def get_all_loans(db: Session, skip: int = 0, limit: int = 100):
    return db.query(ModelLoan).offset(skip).limit(limit).all()


def update_loan(db: Session, loan_id: int, loan: LoanBase):
    db.query(ModelLoan).filter(ModelLoan.id == loan_id).update(loan.dict())
    db.commit()
    return get_loan(db, loan_id)


def delete_loan(db: Session, loan_id: int):
    db.query(ModelLoan).filter(ModelLoan.id == loan_id).delete()
    db.commit()
    return {"message": "Loan deleted successfully."}
