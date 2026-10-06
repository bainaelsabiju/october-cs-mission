import json
import os

print("===== EXPENSE TRACKER =====")

name = input("Enter your name: ")

print("Welcome,", name)

# Load existing expenses
if os.path.exists("expense-tracker/expenses.json"):
    with open("expense-tracker/expenses.json", "r") as file:
        expenses = json.load(file)
else:
    expenses = []


# Add expenses
while True:
    amount = float(input("Enter the expense amount: "))

    if amount <= 0:
        print("Invalid amount!")
        continue

    print("Valid amount!")

    category = input("Enter the category: ")
    date = input("Enter the expense date (YYYY-MM-DD): ")

    # Save amount, category and date
    expenses.append([amount, category, date])

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
total = 0

for expense in expenses:
    total = total + expense[0]

print(f"\nTotal spending: ₹{total:.2f}")


# Calculate spending by category
category_totals = {}

for expense in expenses:
    category = expense[1]
    amount = expense[0]

    if category in category_totals:
        category_totals[category] += amount
    else:
        category_totals[category] = amount


print("\n===== CATEGORY TOTALS =====")

for category, total in category_totals.items():
    print(f"{category}: ₹{total:.2f}")


# Filter expenses by category
category = input("\nEnter a category to filter: ")

print(f"\n===== {category.upper()} EXPENSES =====")

for expense in expenses:
    if expense[1].lower() == category.lower():
        print(f"{expense[1]} - ₹{expense[0]:.2f}")


# Filter expenses by date
date_filter = input("\nEnter a date to filter (YYYY-MM-DD): ")

print(f"\n===== EXPENSES ON {date_filter} =====")

for expense in expenses:
    if len(expense) >= 3 and expense[2] == date_filter:
        print(f"{expense[1]} - ₹{expense[0]:.2f}")


# Save expenses
with open("expense-tracker/expenses.json", "w") as file:
    json.dump(expenses, file, indent=4)