
import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent / "expenses.db"


def get_connection():
    return sqlite3.connect(DB_PATH)


def create_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY,
        amount REAL,
        category TEXT,
        date TEXT,
        description TEXT
    )
    """)

    conn.commit()
    conn.close()


def add_expense(id, amount, category, date, description):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO expenses
    (id, amount, category, date, description)
    VALUES (?, ?, ?, ?, ?)
    """, (id, amount, category, date, description))

    conn.commit()
    conn.close()

    print("Expense saved successfully!")


def get_expenses():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM expenses")
    data = cursor.fetchall()

    conn.close()
    return data


create_table()
