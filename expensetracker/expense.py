class Expense:
    """Expense entry."""
    def __init__(self, name, amount, category, date):
        self.name = name
        self.amount = amount
        self.category = category
        self.date = datetime.strptime(date, "%d-%m-%Y")

    def __str__(self):
        return f"{self.date.strftime('%Y-%m-%d')} - {self.name} - {self.category} - €{self.amount:.2f}"