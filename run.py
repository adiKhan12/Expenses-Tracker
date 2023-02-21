from flask import Flask, render_template, request, redirect, url_for
from expense_tracker import ExpenseTracker
from flask_login import login_user, logout_user, login_required
from flask_login import LoginManager, UserMixin
from database import Session, User
from flask import flash
from uuid import uuid4
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = str(uuid4())

login_manager = LoginManager()
login_manager.init_app(app)

tracker = ExpenseTracker()

@login_manager.user_loader
def load_user(user_id):
    session = Session()
    user = session.query(User).filter(User.id == int(user_id)).first()
    session.close()
    return user

@login_manager.unauthorized_handler
def unauthorized():
    return redirect('/login')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        register = request.form.get('register')
        session = Session()

        # Check if the user is registering
        if register:
            # Check if the username is already taken
            if session.query(User).filter_by(username=username).first() is not None:
                flash('The username is already taken. Please choose a different one.')
                session.close()
                return redirect('/login')

            # Create a new user with the provided username and password
            password_hash = generate_password_hash(password)
            user = User(username=username, password=password_hash)
            session.add(user)
            session.commit()

            flash('You have successfully registered. Please log in to continue.')
            session.close()
            return redirect('/login')

        # Check if the username and password are correct
        user = session.query(User).filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            session.close()
            return redirect('/')
        else:
            flash('Invalid username or password')
            session.close()
            return render_template('login.html')

    else:
        return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/login')

@app.route("/")
@login_required
def index():
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    if start_date and end_date:
        expenses = tracker.get_expenses_by_date_range(start_date, end_date)
    else:
        expenses = tracker.get_expenses()

    return render_template('index.html', expenses=expenses)

@app.route("/add", methods=["GET", "POST"])
@login_required
def add():
    if request.method == "POST":
        name = request.form["name"]
        amount = float(request.form["amount"])
        date_str = request.form["date"]
        tracker.add_expense(name, amount, date_str)
        return redirect(url_for("index"))

    return render_template("add.html")

@app.route("/delete/<int:id>", methods=["POST"])
@login_required
def delete(id):
    tracker.delete_expense(id)
    return redirect(url_for("index"))

@app.route("/edit/<int:id>", methods=["GET", "POST"])
@login_required
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
