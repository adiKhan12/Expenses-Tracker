# Expense Tracker

Expense Tracker is a web application that allows you to track your expenses easily and efficiently. You can add, view, and delete your expenses, and see a summary of your spending over time.

## Features

- Add a new expense with a name, amount, and date.
- View a list of all expenses, sorted by date.
- Delete an expense.
- See a summary of your spending over time, with a line chart and a pie chart.

## Technologies

Expense Tracker is built with the following technologies:

- Python
- Flask
- SQLAlchemy
- Bootstrap
- Chart.js
- Docker

## Installation

To install and run the application locally, follow these steps:

1. Clone this repository to your local machine:
```
https://github.com/adiKhan12/Expenses-Tracker.git
```

2. Install the required Python packages:

````
pip install -r requirements.txt
````
3. Configure the database:
- If you're using SQLite, no further configuration is necessary. The database file will be created in the project directory automatically when you run the application.

4. Create the database tables:
```
python database.py
```
5. Start the development server:
```
python run.py
```
You can then open your web browser and go to http://localhost:5000/ to view the home page, and http://localhost:5000/add to add a new expense.


6. Build the Docker image:
```
docker build -t expense-tracker .
```
7. Run the Docker container:
```
docker run --rm -p 5000:5000 expense-tracker
```

You can then open your web browser and go to http://localhost:5000/ to view the home page, and http://localhost:5000/add to add a new expense.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

This project is based on the [Flask Expense Tracker](https://github.com/mattmakai/flask-expense-tracker) tutorial by Matt Makai. Thanks to Matt and the Flask community for their great work!



