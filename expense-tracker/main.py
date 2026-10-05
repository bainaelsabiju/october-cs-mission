import json
import os

print("===== EXPENSE TRACKER =====")

name = input("Enter your name: ")

print("Welcome,", name)

if os.path.exists("expense-tracker/expenses.json"):
    with open("expense-tracker/expenses.json", "r") as file:
        expenses = json.load(file)
else:
    expenses = []



while True:
    amount = float(input("Enter the expense amount: "))

    if amount <= 0:
        print("Invalid amount!")
    else:
        print("Valid amount!")

        category = input("Enter the category: ")
        date = input("Enter the expense date (YYYY-MM-DD): ")


        expenses.append([amount, category])

        print("Expense Added!")

        choice = input("Do you want to add another expense? (yes/no): ")

        if choice.lower() == "no":
            break

print("\n===== YOUR EXPENSES =====")

for index, expense in enumerate(expenses, start=1):
    amount = expense[0]
    category = expense[1]

    if len(expense) >= 3:
        date = expense[2]
        print(f"{index}. {category} - ₹{amount:.2f} - {date}")
    else:
        print(f"{index}. {category} - ₹{amount:.2f}")
total = 0

for expense in expenses:
    total = total + expense[0]

print(f"\nTotal spending: ₹{total:.2f}")
category = input("\nEnter a category to filter: ")

print(f"\n===== {category.upper()} EXPENSES =====")

date_filter = input("\nEnter a date to filter (YYYY-MM-DD): ")

print(f"\n===== EXPENSES ON {date_filter} =====")

for expense in expenses:
    if len(expense) >= 3 and expense[2] == date_filter:
        print(f"{expense[1]} - ₹{expense[0]:.2f}")

for expense in expenses:
    if expense[1].lower() == category.lower():
        print(f"{expense[1]} - ₹{expense[0]:.2f}")
with open("expense-tracker/expenses.json", "w") as file:
    json.dump(expenses, file, indent=4)