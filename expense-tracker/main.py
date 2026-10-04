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

        expenses.append([amount, category])

        print("Expense Added!")

        choice = input("Do you want to add another expense? (yes/no): ")

        if choice.lower() == "no":
            break

print("\n===== YOUR EXPENSES =====")

for index, expense in enumerate(expenses, start=1):
    amount = expense[0]
    category = expense[1]

    print(f"{index}. {category} - ₹{amount:.2f}")

total = 0

for expense in expenses:
    total = total + expense[0]

print(f"\nTotal spending: ₹{total:.2f}")
with open("expense-tracker/expenses.json", "w") as file:
    json.dump(expenses, file, indent=4)