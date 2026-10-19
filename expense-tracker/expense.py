
from category import Category


class Expense:
    def __init__(self, amount, category, date):
        self.amount = amount

        if isinstance(category, Category):
            self.category = category
        else:
            self.category = Category(category)

        self.date = date

    def display(self):
        print(
            f"{self.category.name} - "
            f"₹{self.amount:.2f} - {self.date}"
        )

    def is_large_expense(self):
        return self.amount >= 500

    @classmethod
    def from_record(cls, record):
        amount = record[0]
        category = record[1]
        date = record[2] if len(record) >= 3 else ""
        return cls(amount, category, date)
