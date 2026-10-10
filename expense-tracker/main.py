import json
import os
import math


# File paths
FILE_PATH = "expense-tracker/expenses.json"
TEMP_PATH = "expense-tracker/expenses.tmp"


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


# Validate loaded expense records
def validate_expenses(data):
    if not isinstance(data, list):
        raise ValueError("Expense data must be a list.")

    for index, expense in enumerate(data, start=1):
        if (
            not isinstance(expense, list)
            or len(expense) < 2
            or len(expense) > 3
        ):
            raise ValueError(
                f"Invalid expense record at entry {index}."
            )

        amount = expense[0]
        category = expense[1]

        if (
            isinstance(amount, bool)
            or not isinstance(amount, (int, float))
            or not math.isfinite(amount)
            or amount <= 0
 ):
            raise ValueError(f"Invalid amount at expense entry {index}.")

        if not isinstance(category, str) or not category.strip():
            raise ValueError(
                f"Invalid category at expense entry {index}."
            )

        if len(expense) == 3:
            if not isinstance(expense[2], str) or not expense[2].strip():
                raise ValueError(
                    f"Invalid date at expense entry {index}."
                )

    return data


# Save expenses safely
def save_expenses(expenses):
    try:
        # Write to a temporary file first
        with open(TEMP_PATH, "w", encoding="utf-8") as file:
            json.dump(expenses, file, indent=4)
            file.flush()
            os.fsync(file.fileno())

        # Replace the original only after writing succeeds
        os.replace(TEMP_PATH, FILE_PATH)

        print("\nExpenses saved successfully!")

    except (OSError, TypeError, ValueError) as error:
        print("\nERROR: Could not save expenses.")
        print("Details:", error)

        # Attempt to remove the temporary file
        try:
            if os.path.exists(TEMP_PATH):
                os.remove(TEMP_PATH)
        except OSError:
            print("Warning: Could not remove the temporary file.")


# Load existing expenses safely
def load_expenses():
    if not os.path.exists(FILE_PATH):
        print("No existing expense file found. Starting with an empty list.")
        return []

    try:
        with open(FILE_PATH, "r", encoding="utf-8") as file:
            data = json.load(file)

        return validate_expenses(data)

    except json.JSONDecodeError:
        print("\nERROR: The expense file contains invalid JSON.")
        print("Your existing file has not been overwritten.")
        raise

    except ValueError as error:
        print("\nERROR: The expense file contains invalid records.")
        print("Details:", error)
        print("Your existing file has not been overwritten.")
        raise

    except OSError as error:
        print("\nERROR: Could not read the expense file.")
        print("Details:", error)
        raise


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

    # Load existing data before allowing changes
    try:
        expenses = load_expenses()
    except (OSError, ValueError):
        print("\nProgram stopped to protect your existing expense data.")
        return

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

    for category, amount in category_totals.items():
        print(f"{category}: ₹{amount:.2f}")

    # Filter by category
    category = input("\nEnter a category to filter: ").strip()

    print(f"\n===== {category.upper()} EXPENSES =====")

    matching_expenses = filter_by_category(expenses, category)

    if matching_expenses:
        for expense in matching_expenses:
            print(f"{expense[1]} - ₹{expense[0]:.2f}")
    else:
        print("No expenses found for this category.")

    # Filter by date
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


if __name__ == "__main__":
    main()
