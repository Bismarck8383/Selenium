from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DATETIME, Date, DECIMAL
from datetime import datetime
Base = declarative_base()

class User(Base):
    #creanos nuestra tables
    __tablename__ = 'users'
    id = Column(Integer(), primary_key=True)
    username = Column(String(50), nullable=False)
    email = Column(String(200), nullable=True, unique=True)
    created_at = Column(DATETIME(), default=datetime.now())

    def __str__(self):
        return self.username




if __name__ == '__main__':
    pass