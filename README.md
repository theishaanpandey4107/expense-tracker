# Personal Expense Tracker

A beginner-level Python project that records daily expenses, stores them permanently in a database, and shows summaries and charts in a web dashboard.

**Live demo:** [PASTE-YOUR-STREAMLIT-LINK-HERE](PASTE-YOUR-STREAMLIT-LINK-HERE)

> The demo is shared by everyone who opens it, and data may reset when the app restarts. Please use dummy data only.

## Features

- Add an expense with amount, category, date and description
- Categories are picked from a fixed list (food, travel, shopping, education, other), so invalid categories cannot be saved
- Expenses are stored permanently in a SQLite database
- Summary: total, average, minimum and maximum spending
- Category-wise totals with percentage share
- Bar chart of spending by category
- Table of all saved records

## Tech stack

| Tool | Used for |
|---|---|
| Python | Core logic |
| SQLite | Permanent storage of expenses |
| Pandas | Organising records and calculating totals |
| Matplotlib | Charts |
| Streamlit | Web dashboard |

## How the data flows

```text
User input (Streamlit form)
        ↓
dashboard.py
        ↓
database.py
        ↓
SQLite database (expenses.db)
        ↓
Pandas calculations
        ↓
Tables and Matplotlib charts
```

## Project structure

```text
expense_tracker/
├── dashboard.py      # Streamlit web interface
├── database.py       # SQLite functions: create table, add expense, get expenses
├── app.py            # Original command-line version (first version of the project)
├── analysis.py       # Standalone Matplotlib script for category-wise chart
├── requirements.txt  # Libraries needed to run the project
└── expenses.db       # Created automatically when the app runs
```

## Run it on your computer

1. Clone or download this repository.
2. Open a terminal in the project folder and install the libraries:

   ```bash
   pip install -r requirements.txt
   ```

3. Start the dashboard:

   ```bash
   streamlit run dashboard.py
   ```

4. Open `http://localhost:8501` in your browser if it does not open automatically.

The database file `expenses.db` is created automatically the first time the app runs.

## What I learned

- Connecting Python to a SQLite database and reading and writing records
- Why a function with the same name as an imported one overrides it (name shadowing), and how to fix it
- Passing arguments in the correct order between files
- Validating input before saving it
- Grouping data by category with Pandas and drawing charts with Matplotlib
- Turning a command-line program into a web dashboard with Streamlit
- Deploying an app with GitHub and Streamlit Community Cloud

## Future improvements

- Date-wise and monthly expense analysis
- Pie chart for category share
- Delete and edit expenses
- Better database design and error handling
- Login so each user sees only their own expenses
- A hosted database for permanent storage online

## Author

Ishaan, first-year B.Tech student. This is a learning project built step by step.
