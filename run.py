from flask import Flask, render_template, request, redirect, url_for
from expense_tracker import ExpenseTracker

app = Flask(__name__)

tracker = ExpenseTracker()

@app.route("/")
def index():
    expenses = tracker.get_expenses()
    return render_template("index.html", expenses=expenses)

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        name = request.form["name"]
        amount = float(request.form["amount"])
        date_str = request.form["date"]
        tracker.add_expense(name, amount, date_str)
        return redirect(url_for("index"))

    return render_template("add.html")

@app.route("/delete/<int:id>", methods=["POST"])
def delete(id):
    tracker.delete_expense(id)
    return redirect(url_for("index"))

@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    expense = tracker.get_expense(id)
    if request.method == "POST":
        name = request.form["name"]
        amount = float(request.form["amount"])
        date_str = request.form["date"]
        tracker.update_expense(id, name, amount, date_str)
        return redirect(url_for("index"))
    else:
        return render_template("edit.html", expense=expense)


if __name__ == "__main__":
    app.run(debug=True)
