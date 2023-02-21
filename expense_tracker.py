from datetime import date
from database import Session, Expense
from datetime import datetime

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

    def get_expense(self, id):
        session = Session()

        expense = session.query(Expense).get(id)

        session.close()

        return expense

    def update_expense(self, id, name, amount, date_str):
        session = Session()

        expense = session.query(Expense).get(id)
        expense.name = name
        expense.amount = amount
        expense.date = datetime.strptime(date_str, "%Y-%m-%d").date()
        session.commit()

        session.close()

    def delete_expense(self, id):
        session = Session()

        expense = session.query(Expense).get(id)
        session.delete(expense)
        session.commit()

        session.close()

    def get_expenses_by_date_range(self, start_date_str, end_date_str):
        session = Session()

        start_date = datetime.strptime(start_date_str, "%Y-%m-%d").date()
        end_date = datetime.strptime(end_date_str, "%Y-%m-%d").date()
        expenses = session.query(Expense).filter(Expense.date.between(start_date, end_date)).all()
        
        session.close()
        return expenses
