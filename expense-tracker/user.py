
class User:
    def __init__(self, name):
        self.name = name
        self.expenses = []

    def add_expense(self, expense):
        self.expenses.append(expense)

    def display_expenses(self):
        print(f"\nExpenses for {self.name}:")

        for expense in self.expenses:
            expense.display()
