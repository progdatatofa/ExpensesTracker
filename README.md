# Expense Tracker

A command-line expense tracker built with Python, Object-Oriented Programming (OOP), and JSON file storage.

## Features

* Add new expenses
* View all expenses
* Search for an expense
* Update existing expenses
* Delete expenses
* Calculate total expenses
* Find the highest expense
* View expenses by category
* Save expenses to a JSON file
* Load saved expenses when the application starts
* Input validation and error handling

## Technologies Used

* Python
* Object-Oriented Programming (OOP)
* JSON
* File Handling
* Exception Handling

## Project Structure

```text
ExpenseTracker/
│
├── main.py
├── manager.py
├── expense.py
├── storage.py
├── expense.json
├── README.md
└── .gitignore
```

## How It Works

The application is divided into different components to keep the code organized and separate responsibilities.

### `expense.py`

Contains the `Expense` class, which represents an individual expense.

Each expense contains information such as:

* ID
* Description
* Amount
* Category

### `manager.py`

Contains the `ExpenseManager` class.

It handles the main expense operations, including:

* Adding expenses
* Retrieving expenses
* Searching expenses
* Updating expenses
* Deleting expenses
* Calculating total expenses
* Finding the highest expense
* Filtering expenses by category

### `storage.py`

Handles JSON file persistence.

The application saves expense data to `expense.json` and loads the saved data when the application starts.

### `main.py`

Contains the command-line interface.

It handles:

* Displaying the menu
* Collecting user input
* Input validation
* Calling the appropriate manager methods
* Displaying results to the user

## Installation

Clone the repository:

```bash
git clone https://github.com/progdatatofa/ExpensesTracker.git
```

Navigate into the project directory:

```bash
cd ExpenseTracker
```

Run the application:

```bash
python3 main.py
```

## Example

```text
1. Add Expense
2. View Expenses
3. Search Expense
4. Update Expense
5. Delete Expense
6. Calculate Total Expenses
7. Show Highest Expense
8. Show Expenses by Category
9. Exit
```

## What I Learned

Through this project, I practiced building a complete Python application using Object-Oriented Programming.

The project helped strengthen my understanding of:

* Classes and objects
* CRUD operations
* JSON data persistence
* File handling
* Exception handling
* Input validation
* Functions and modules
* Separation of responsibilities
* Working with lists and dictionaries

## Future Improvements

Possible future improvements include:

* Add expense dates
* Add monthly and yearly expense summaries
* Add budget tracking
* Add expense sorting
* Add graphical reports
* Replace JSON storage with a database
* Build a web-based version using Django
