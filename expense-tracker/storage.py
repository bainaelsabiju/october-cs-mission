
import json
import math
import os

# Build paths relative to this file.
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, "expenses.json")
TEMP_PATH = os.path.join(BASE_DIR, "expenses.tmp")


def validate_expenses(data):
    if not isinstance(data, list):
        raise ValueError("Expense data must be a list.")

    for index, expense in enumerate(data, start=1):
        if not isinstance(expense, list) or len(expense) not in (2, 3):
            raise ValueError(f"Invalid expense record at entry {index}.")

        amount = expense[0]
        category = expense[1]

        if (
            isinstance(amount, bool)
            or not isinstance(amount, (int, float))
            or not math.isfinite(amount)
            or amount <= 0
        ):
            raise ValueError(f"Invalid amount at entry {index}.")

        if not isinstance(category, str) or not category.strip():
            raise ValueError(f"Invalid category at entry {index}.")

        if len(expense) == 3:
            date = expense[2]

            if not isinstance(date, str) or not date.strip():
                raise ValueError(f"Invalid date at entry {index}.")

    return data


def load_expenses():
    if not os.path.exists(FILE_PATH):
        print("No existing expense file found. Starting empty.")
        return []

    try:
        with open(FILE_PATH, "r", encoding="utf-8") as file:
            data = json.load(file)

        return validate_expenses(data)

    except json.JSONDecodeError:
        print("ERROR: The expense file contains invalid JSON.")
        print("Your existing file has not been overwritten.")
        raise

    except ValueError as error:
        print("ERROR: Invalid expense records.")
        print("Details:", error)
        print("Your existing file has not been overwritten.")
        raise

    except OSError as error:
        print("ERROR: Could not read the expense file.")
        print("Details:", error)
        raise


def save_expenses(expenses):
    try:
        validate_expenses(expenses)

        # Write to a temporary file first.
        with open(TEMP_PATH, "w", encoding="utf-8") as file:
            json.dump(expenses, file, indent=4, allow_nan=False)
            file.flush()
            os.fsync(file.fileno())

        # Replace the original only after writing succeeds.
        os.replace(TEMP_PATH, FILE_PATH)

        print("Expenses saved successfully!")
        return True

    except (OSError, TypeError, ValueError) as error:
        print("ERROR: Could not save expenses.")
        print("Details:", error)

        try:
            if os.path.exists(TEMP_PATH):
                os.remove(TEMP_PATH)
        except OSError:
            print("Warning: Could not remove the temporary file.")

        return False
