import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from database import add_expense, get_expenses

CATEGORIES = ["food", "travel", "shopping", "education", "other"]


def load_df():
    rows = get_expenses()
    return pd.DataFrame(rows, columns=["id", "amount", "category", "date", "description"])


st.title("Expense Tracker")

# ---------- 1. Add expense form ----------
st.header("Add expense")

with st.form("add_form", clear_on_submit=True):
    amount = st.number_input("Amount (₹)", min_value=0.0, step=1.0)
    category = st.selectbox("Category", CATEGORIES)
    date = st.date_input("Date")
    description = st.text_input("Description")
    submitted = st.form_submit_button("Save")

if submitted:
    if amount <= 0:
        st.error("Amount must be more than 0.")
    else:
        df = load_df()
        new_id = 1 if df.empty else int(df["id"].max()) + 1
        add_expense(new_id, amount, category, date.strftime("%d/%m/%Y"), description)
        st.success("Expense saved!")

# ---------- 2. Read from database ----------
df = load_df()

if df.empty:
    st.info("No expenses yet. Add your first one above.")
else:
    # ---------- 3. Summary numbers ----------
    st.header("Summary")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Total", f"₹{df['amount'].sum():.2f}")
    c2.metric("Average", f"₹{df['amount'].mean():.2f}")
    c3.metric("Minimum", f"₹{df['amount'].min():.2f}")
    c4.metric("Maximum", f"₹{df['amount'].max():.2f}")

    # ---------- 4. Category-wise ----------
    st.header("Category wise")
    totals = df.groupby("category")["amount"].sum()
    percent = (totals / totals.sum() * 100).round(1)
    summary = pd.DataFrame({"total": totals, "percent %": percent})
    st.dataframe(summary)

    fig, ax = plt.subplots()
    ax.bar(totals.index, totals.values)
    ax.set_title("Category Wise Expenses")
    ax.set_xlabel("Categories")
    ax.set_ylabel("Amount (₹)")
    st.pyplot(fig)

    # ---------- 5. All records ----------
    st.header("All records")
    st.dataframe(df)