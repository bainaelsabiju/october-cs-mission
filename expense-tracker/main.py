
import math

from expense import Expense

from expense_functions import (
    calculate_total,
    calculate_category_totals,
    filter_by_category,
    filter_by_date,
)

from storage import load_expenses, save_expenses


# Add an expense
def add_expense(expenses):
    try:
        amount = float(input("Enter the expense amount: "))

        if not math.isfinite(amount) or amount <= 0:
            print("Amount must be a valid number greater than 0!")
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
def main():
    print("===== EXPENSE TRACKER =====")

    name = input("Enter your name: ").strip()
    print("Welcome,", name)

    # Load existing expenses
    try:
        expenses = load_expenses()
    except (OSError, ValueError):
        print("\nProgram stopped to protect your existing expense data.")
        return

    # Convert saved records into Expense objects
    expense_objects = [
        Expense.from_record(record)
        for record in expenses
    ]

    # Add expenses
    while True:
        add_expense(expenses)

        choice = input(
            "Do you want to add another expense? (yes/no): "
        ).strip().lower()

        if choice != "yes":
            break

    # Convert all records, including newly added expenses, into objects
    expense_objects = [
        Expense.from_record(record)
        for record in expenses
    ]

    # Display all expenses using the Expense class
    print("\n===== YOUR EXPENSES =====")

    for index, expense in enumerate(expense_objects, start=1):
        print(f"{index}. ", end="")
        expense.display()

    # Calculate total spending
    total = calculate_total(expenses)
    print(f"\nTotal spending: ₹{total:.2f}")

    # Calculate spending by category
    category_totals = calculate_category_totals(expenses)

    print("\n===== CATEGORY TOTALS =====")

    for category, amount in category_totals.items():
        print(f"{category}: ₹{amount:.2f}")

    # Filter by category
    category = input("\nEnter a category to filter: ").strip()

    print(f"\n===== {category.upper()} EXPENSES =====")

    matching_expenses = filter_by_category(expenses, category)

    if matching_expenses:
        for record in matching_expenses:
            expense = Expense.from_record(record)
            expense.display()
    else:
        print("No expenses found for this category.")

    # Filter by date
    date_filter = input(
        "\nEnter a date to filter (YYYY-MM-DD): "
    ).strip()

    print(f"\n===== EXPENSES ON {date_filter} =====")

    matching_expenses = filter_by_date(expenses, date_filter)

    if matching_expenses:
        for record in matching_expenses:
            expense = Expense.from_record(record)
            expense.display()
    else:
        print("No expenses found for this date.")

    # Show large expenses using the Expense class
    print("\n===== LARGE EXPENSES (₹500 OR MORE) =====")

    large_expenses_found = False

    for expense in expense_objects:
        if expense.is_large_expense():
            expense.display()
            large_expenses_found = True

    if not large_expenses_found:
        print("No large expenses found.")

    # Save expenses without changing the JSON record format
    save_expenses(expenses)


if __name__ == "__main__":
    main()
