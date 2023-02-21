from sqlalchemy import create_engine, Column, Integer, String, Float, Date
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String
from flask_login import UserMixin
# Create the engine for the SQLite database
engine = create_engine("sqlite:///expenses.db", echo=True)

# Create the session factory
Session = sessionmaker(bind=engine)

# Create the base class for declarative models
Base = declarative_base()

# Define the Expense model
class Expense(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    date = Column(Date, nullable=False)

    def __repr__(self):
        return f"<Expense(id={self.id}, name='{self.name}', amount={self.amount}, date='{self.date}')>"

# Define the User model
class User(Base, UserMixin):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True)
    password = Column(String(50))
    role = Column(String(20), default='user')

    def is_active(self):
        return True
# Create the tables in the database
Base.metadata.create_all(engine)

