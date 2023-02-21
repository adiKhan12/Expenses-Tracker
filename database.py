from sqlalchemy import create_engine, Column, Integer, String, Float, Date
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

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

# Create the tables in the database
Base.metadata.create_all(engine)
