
def calculate_total(expenses):
    total = 0

    for expense in expenses:
        total += expense[0]

    return total


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


def filter_by_category(expenses, category):
    matching_expenses = []

    for expense in expenses:
        if expense[1].strip().lower() == category.strip().lower():
            matching_expenses.append(expense)

    return matching_expenses


def filter_by_date(expenses, date):
    matching_expenses = []

    for expense in expenses:
        if len(expense) >= 3 and expense[2].strip() == date.strip():
            matching_expenses.append(expense)

    return matching_expenses

def calculate_monthly_totals(expenses):
    monthly_totals = {}

    for record in expenses:
        amount = float(record[0])
        date = record[2] if len(record) >= 3 else ""

        if len(date) < 7 or date[4] != "-":
            continue

        month = date[:7]

        if month not in monthly_totals:
            monthly_totals[month] = 0

        monthly_totals[month] += amount

    return monthly_totals
