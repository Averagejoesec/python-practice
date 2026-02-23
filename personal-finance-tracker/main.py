import csv
import os

print("Personal Finance Tracker with Budgets")
print("=====================================\n")


class Expense:
    def __init__(self, amount, category, description):
        self.amount = amount
        self.category = category
        self.description = description

    def display(self):
        return f"${self.amount:<7.2f} | {self.category:<12} | {self.description}"

# Uses an ExpenseTracker class to manage all expenses
class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        self.budgets = {}
        self.load_expenses

    def load_expenses(self):
        if not os.path.exists('expenses.csv'):
            return
        print("Loading expenses from file...")
        with open('expenses.csv', 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                expense = Expense(
                    float(row['amount']),
                    row['category'],
                    row['description']
                )
                self.expenses.append(expense)
        print(f"Load {len(self.expenses)} existing expenses. \n")

    def save_expenses(self):
        with open('expenses.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['amount', 'category', 'description'])
            for expense in self.expenses:
                writer.writerow([expense.amount, expense.category, expense.description])

    def set_budget(self):
        print("\nSet Category Budget")
        print("-------------------")
        category = input("Category: ")
        budget = float(input("Monthly Budget: $"))
        print("\nBudget set successfully!\n")

    def check_budget(self, category):
        category_total = sum(e.amount for e in self.expenses if e.category == category)
        if category in self.budgets:
            budget = self.budgets[category]
            percentage = (category_total / budget) * 100
            if percentage >= 80 and percentage < 100:
                print(f"\n Warning: You've spent ${category_total:.2f} of your ${budget:.2f} {category} budget ({percentage:.0f}%)")
            elif percentage >= 100:
                print(f"\n Alert: You've exceed your ${budget:.2f} {category} budget! Current spending: ${category_total:.2f}")

    def add_expenses(self):
        print("\nAdd New Expense")
        print("---------------")
        amount = float(input("Amount: "))
        category = str(input("Category: "))
        description = str(input("Description: "))
        expense = Expense(amount, category, description)
        self.expenses.append(expense)
        self.save_expenses()
        self.check_budget(category)
        print("\nExpense added successfully!\n")

    def view_expenses(self):
        print("\nAll Expenses")
        print("-------------")
        if not self.expenses:
            print("No expenses recorded yet.\n")
            return
        for i, expense in enumerate(self.expenses, 1):
            print(f"#{i:<3} | {expense.display()}")
        print()

    # Calculates and shows total spending
    def view_summary(self):
        print("\nExpense Summary")
        print("--------------")
        if not self.expenses:
            print("No expenses recorded yet.\n")
            return
        total = sum(expense.amount for expense in self.expenses)
        print(f"Total Spending: ${total:.2f}")
        byCategory = {}
        for expense in self.expenses:
            # byCategory[expense.category] = byCategory.get(expense.category, 0) + expense.amount
            if expense.category in byCategory:
                byCategory[expense.category] += expense.amount
            else:
                byCategory[expense.category] = expense.amount
        print("By Category:")
        for category, amount in byCategory.items():
            if category in self.budgets:
                budget = self.budgetes[category]
                percentage = (amount / budget) * 100
                status = f"${amount:.2f} / ${budget:.2f} ({percentage:.0f}% used)"
                if percentage >= 80:
                    status += " ⚠️"
            else:
                status = f"${amount:.2f} (No budget set)"
            print(f"{category}: ${amount:.2f}")
        print()


tracker = ExpenseTracker()

# Uses a simple menu system for user interaction
while True:
    print("""Menu:
    1. Add Expense
    2. View All Expenses
    3. View Summary
    4. Exit""")
    userOption = input("\nChoose option: ")
    match userOption:
        case "1":
            tracker.add_expenses()
        case "2":
            tracker.view_expenses()
        case "3":
            tracker.view_summary()
        case "4":
            tracker.set_budget()
        case "5":
            print("\nSaving expenses to file...")
            tracker.save_expenses()
            print("Goodbye!")
            break
        case _:
            print("\nInvalid option. Please try again.\n")
