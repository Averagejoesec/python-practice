# {"Amount" : 85.99, "Category" : "Groceries", "Description" : "Cheese"},
#             {"Amount" : 90.56, "Category" : "Transportation", "Description" : "Gas"},
#             {"Amount" : 65.45, "Category" : "Food", "Description" : "Wendys"}
# Uses an Expense class to represent individual expenses
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

    def add_expenses(self):
        print("\nAdd New Expense")
        print("---------------")
        amount = float(input("Amount: "))
        category = str(input("Category: "))
        description = str(input("Description: "))
        expense = Expense(amount, category, description)

        self.expenses.append(expense)
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
            print("\nGoodbye!")
            break
        case _:
            print("\nInvalid option. Please try again.\n")
