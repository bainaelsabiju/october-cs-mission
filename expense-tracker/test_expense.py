
from expense import Expense

expense1 = Expense(200, "Food", "2026-10-11")
expense2 = Expense(500, "Travel", "2026-10-11")

expense1.display()
expense2.display()

print(expense1.is_large_expense())
print(expense2.is_large_expense())

record = [350, "Stationery", "2026-10-11"]

expense3 = Expense(record[0], record[1], record[2])

expense3.display()
print("Large expense:", expense3.is_large_expense())

record = [350, "Stationery", "2026-10-11"]

expense3 = Expense.from_record(record)

expense3.display()
print("Large expense:", expense3.is_large_expense())

record = [350, "Stationery", "2026-10-11"]

expense = Expense.from_record(record)
expense.display()
print("Large expense:", expense.is_large_expense())
