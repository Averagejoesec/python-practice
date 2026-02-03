# Uses functions to organize different operations

# Stores expenses in a Python list (in-memory for now)
expenses = []

# Allows users to add expenses with amount, category, and description
def add_expenses():
    print("Add New Expense")
    amount = float(input("Amount: "))
    category = str(input("Category: "))
    description = str(input("Description: "))

    expenses.append({"Amount" : amount, "Category": category, "Description": description})
    print(expenses)

# Displays all expenses in a clean, formatted output
def view_expenses():
    # Shows spending breakdown by category
    pass

# Calculates and shows total spending
def view_summary():
    pass

# Uses a simple menu system for user interaction
def main_menu():
    print("""Menu:
1. Add Expense
2. View All Expenses
3. View Summary
4. Exit
""")
    userOption = int(input("Choose option: "))
    
    match userOption:
        case 1:
            add_expenses()
        case 2:
            view_expenses()
        case 3:
            view_summary()


main_menu()

