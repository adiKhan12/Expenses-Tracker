from datetime import date
from database import Session, Expense

class ExpenseTracker:
    def add_expense(self, name, amount, date_str):
        session = Session()

        expense = Expense(name=name, amount=amount, date=date.fromisoformat(date_str))
        session.add(expense)
        session.commit()

        session.close()

    def get_expenses(self):
        session = Session()

        expenses = session.query(Expense).all()

        session.close()

        return expenses
