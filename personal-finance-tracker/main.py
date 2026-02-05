# Uses functions to organize different operations

# Stores expenses in a Python list (in-memory for now)
from unicodedata import category

from numpy import sort


expenses = [{"Amount" : 85.99, "Category" : "Groceries", "Description" : "Cheese"},
            {"Amount" : 90.56, "Category" : "Transportation", "Description" : "Gas"},
            {"Amount" : 65.45, "Category" : "Food", "Description" : "Wendys"}]

# Allows users to add expenses with amount, category, and description
def add_expenses():
    print("Add New Expense")
    amount = float(input("Amount: "))
    category = str(input("Category: "))
    description = str(input("Description: "))

    expenses.append({"Amount" : amount, "Category": category, "Description": description})
    print("Expense added successfully!")
    main_menu()

# Displays all expenses in a clean, formatted output
def view_expenses():
    print("All Expenses")
    expenseNumber = 1
    for expense in expenses:
        amount = expense["Amount"]
        category = expense["Category"]
        description = expense["Description"]
        print(f"#{expenseNumber} | ${amount} | {category} | {description}")
        expenseNumber += 1
    main_menu()

# Calculates and shows total spending
def view_summary():
    print("Expense Summary")
    totalSpend = 0.00
    sortByCategory = {}
    for expense in expenses:
        totalSpend += expense["Amount"]
        expenseCategory = expense["Category"]
        expenseAmount = expense["Amount"]
        sortByCategory.update({expenseCategory: expenseAmount})

    print(f"Total Spending: ${round(totalSpend, 2)}\n")
        
    print("By Category:")
    for category, amount in sortByCategory.items():
        print(f"{category}: ${round(amount, 2)}")

    main_menu()


# Uses a simple menu system for user interaction
def main_menu():

    userOption = int(input("\nChoose option: "))
    
    match userOption:
        case 1:
            add_expenses()
        case 2:
            view_expenses()
        case 3:
            view_summary()
        case 4:
            print("Goodbye!")
            exit

if __name__ == "__main__":
    print("""Menu:
    1. Add Expense
    2. View All Expenses
    3. View Summary
    4. Exit""")
    main_menu()