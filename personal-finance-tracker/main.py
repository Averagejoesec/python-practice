import streamlit as st
import csv
import os
import pandas as pd
import plotly.express as px

class Expense:
    def __init__(self, amount, category, description):
        self.amount = amount
        self.category = category
        self.description = description

class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        self.budgets = {}
        self.load_expenses()
    
    def load_expenses(self):
        if not os.path.exists('personal-finance-tracker/expenses.csv'):
            return
        with open('personal-finance-tracker/expenses.csv', 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                expense = Expense(
                    float(row['amount']),
                    row['category'],
                    row['description']
                )
                self.expenses.append(expense)
    
    def save_expenses(self):
        with open('expenses.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['amount', 'category', 'description'])
            for expense in self.expenses:
                writer.writerow([expense.amount, expense.category, expense.description])
    
    def add_expense(self, amount, category, description):
        expense = Expense(amount, category, description)
        self.expenses.append(expense)
        self.save_expenses()
    
    def get_category_totals(self):
        by_category = {}
        for expense in self.expenses:
            by_category[expense.category] = by_category.get(expense.category, 0) + expense.amount
        return by_category

st.set_page_config(page_title="Personal Finance Dashboard", page_icon="💰")

st.title("💰 Personal Finance Dashboard")
st.markdown("---")

if 'tracker' not in st.session_state:
    st.session_state.tracker = ExpenseTracker()

tracker = st.session_state.tracker

st.subheader("Add New Expense")
col1, col2 = st.columns(2)

with col1:
    amount = st.number_input("Amount ($)", min_value=0.01, step=0.01)
    category = st.text_input("Category", placeholder="e.g., Groceries")

with col2:
    description = st.text_input("Description", placeholder="What did you buy?")

if st.button("Add Expense", type="primary"):
    if category and description:
        tracker.add_expense(amount, category, description)
        st.success(f"Added ${amount:.2f} expense!")
        st.rerun()
    else:
        st.warning("Please fill in all fields")

st.markdown("---")
st.subheader("All Expenses")

if tracker.expenses:
    data = {
        'Amount': [f"${e.amount:.2f}" for e in tracker.expenses],
        'Category': [e.category for e in tracker.expenses],
        'Description': [e.description for e in tracker.expenses]
    }
    df = pd.DataFrame(data)
    st.dataframe(df, use_container_width=True)
    
    st.markdown("### Summary Statistics")
    total = sum(e.amount for e in tracker.expenses)
    st.metric("Total Spending", f"${total:.2f}")
    
    st.markdown("---")
    chart_col1, chart_col2 = st.columns(2)
    
    category_totals = tracker.get_category_totals()
    
    with chart_col1:
        st.markdown("### Spending by Category")
        fig_pie = px.pie(
            values=list(category_totals.values()),
            names=list(category_totals.keys()),
            title="Category Distribution"
        )
        st.plotly_chart(fig_pie, use_container_width=True)
    
    with chart_col2:
        st.markdown("### Category Breakdown")
        fig_bar = px.bar(
            x=list(category_totals.keys()),
            y=list(category_totals.values()),
            labels={'x': 'Category', 'y': 'Amount ($)'},
            title="Total by Category"
        )
        st.plotly_chart(fig_bar, use_container_width=True)

else:
    st.info("No expenses yet. Add your first expense above!")
