import json
import os


# Calculate total spending
def calculate_total(expenses):
    total = 0

    for expense in expenses:
        total += expense[0]

    return total


# Calculate spending by category
def calculate_category_totals(expenses):
    category_totals = {}

    for expense in expenses:
        category = expense[1]
        amount = expense[0]

        if category in category_totals:
            category_totals[category] += amount
        else:
            category_totals[category] = amount

    return category_totals


# Filter expenses by category
def filter_by_category(expenses, category):
    matching_expenses = []

    for expense in expenses:
        if expense[1].lower() == category.lower():
            matching_expenses.append(expense)

    return matching_expenses


# Filter expenses by date
def filter_by_date(expenses, date):
    matching_expenses = []

    for expense in expenses:
        if len(expense) >= 3 and expense[2] == date:
            matching_expenses.append(expense)

    return matching_expenses


# Save expenses
def save_expenses(expenses):
    with open("expense-tracker/expenses.json", "w") as file:
        json.dump(expenses, file, indent=4)


# Load expenses
def load_expenses():
    if os.path.exists("expense-tracker/expenses.json"):
        with open("expense-tracker/expenses.json", "r") as file:
            return json.load(file)
    else:
        return []


print("===== EXPENSE TRACKER =====")

name = input("Enter your name: ")

print("Welcome,", name)


# Load existing expenses
expenses = load_expenses()

def add_expense(expenses):
    amount = float(input("Enter the expense amount: "))

    if amount <= 0:
        print("Invalid amount!")
        return

    print("Valid amount!")

    category = input("Enter the category: ")
    date = input("Enter the expense date (YYYY-MM-DD): ")

    expenses.append([amount, category, date])

    print("Expense Added!")


# Add expenses
while True:
    add_expense(expenses)

    choice = input("Do you want to add another expense? (yes/no): ")

    if choice.lower() == "no":
        break

    category = input("Enter the category: ")

    date = input("Enter the expense date (YYYY-MM-DD): ")

    

    print("Expense Added!")

    choice = input("Do you want to add another expense? (yes/no): ")

    if choice.lower() == "no":
        break


# Display all expenses
print("\n===== YOUR EXPENSES =====")

for index, expense in enumerate(expenses, start=1):

    amount = expense[0]
    category = expense[1]

    if len(expense) >= 3:
        date = expense[2]
        print(f"{index}. {category} - ₹{amount:.2f} - {date}")
    else:
        print(f"{index}. {category} - ₹{amount:.2f}")


# Calculate total spending
total = calculate_total(expenses)

print(f"\nTotal spending: ₹{total:.2f}")


# Calculate spending by category
category_totals = calculate_category_totals(expenses)

print("\n===== CATEGORY TOTALS =====")

for category, total in category_totals.items():
    print(f"{category}: ₹{total:.2f}")


# Filter expenses by category
category = input("\nEnter a category to filter: ")

print(f"\n===== {category.upper()} EXPENSES =====")

matching_expenses = filter_by_category(expenses, category)

for expense in matching_expenses:
    print(f"{expense[1]} - ₹{expense[0]:.2f}")


# Filter expenses by date
date_filter = input("\nEnter a date to filter (YYYY-MM-DD): ")

print(f"\n===== EXPENSES ON {date_filter} =====")

matching_expenses = filter_by_date(expenses, date_filter)

for expense in matching_expenses:
    print(f"{expense[1]} - ₹{expense[0]:.2f}")


# Save expenses
save_expenses(expenses)