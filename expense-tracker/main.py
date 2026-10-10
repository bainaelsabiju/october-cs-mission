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
        if expense[1].strip().lower() == category.strip().lower():
            matching_expenses.append(expense)

    return matching_expenses


# Filter expenses by date
def filter_by_date(expenses, date):
    matching_expenses = []

    for expense in expenses:
        if len(expense) >= 3 and expense[2].strip() == date.strip():
            matching_expenses.append(expense)

    return matching_expenses


# Save expenses
def save_expenses(expenses):
    try:
        with open("expense-tracker/expenses.json", "w") as file:
            json.dump(expenses, file, indent=4)

        print("\nExpenses saved successfully!")

    except OSError:
        print("\nError: Could not save expenses.")


# Load expenses
def load_expenses():
    file_path = "expense-tracker/expenses.json"

    if not os.path.exists(file_path):
        return []

    try:
        with open(file_path, "r") as file:
            data = json.load(file)

        if not isinstance(data, list):
            raise ValueError("Expense data must be a list.")

        return data

    except json.JSONDecodeError:
        print("ERROR: The expense file contains invalid JSON.")
        print("Please check or restore the file before continuing.")
        raise

    except OSError:
        print("ERROR: Could not read the expense file.")
        raise


# Add an expense
def add_expense(expenses):
    try:
        amount = float(input("Enter the expense amount: "))

        if amount <= 0:
            print("Amount must be greater than 0!")
            return

        category = input("Enter the category: ").strip()
        date = input("Enter the expense date (YYYY-MM-DD): ").strip()

        if not category or not date:
            print("Category and date cannot be empty!")
            return

        expenses.append([amount, category, date])

        print("Expense Added!")

    except ValueError:
        print("Please enter a valid number!")

    finally:
        print("Input process finished.")


# Main program
print("===== EXPENSE TRACKER =====")

name = input("Enter your name: ").strip()

print("Welcome,", name)


# Load existing expenses
expenses = load_expenses()


# Add expenses
while True:
    add_expense(expenses)

    choice = input(
        "Do you want to add another expense? (yes/no): "
    ).strip().lower()

    if choice != "yes":
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
category = input("\nEnter a category to filter: ").strip()

print(f"\n===== {category.upper()} EXPENSES =====")

matching_expenses = filter_by_category(expenses, category)

if matching_expenses:
    for expense in matching_expenses:
        print(f"{expense[1]} - ₹{expense[0]:.2f}")
else:
    print("No expenses found for this category.")


# Filter expenses by date
date_filter = input(
    "\nEnter a date to filter (YYYY-MM-DD): "
).strip()

print(f"\n===== EXPENSES ON {date_filter} =====")

matching_expenses = filter_by_date(expenses, date_filter)

if matching_expenses:
    for expense in matching_expenses:
        print(f"{expense[1]} - ₹{expense[0]:.2f}")
else:
    print("No expenses found for this date.")


# Save expenses
save_expenses(expenses)
