import logging
import gspread
from google.oauth2.service_account import Credentials
import warnings
from tabulate import tabulate
from datetime import datetime

# Suppress the gspread warning
warnings.filterwarnings("ignore", category=UserWarning, module="gspread")

# Google Sheets scope
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
] 

# Load Google Sheets credentials from the JSON file
CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET_URL = 'https://docs.google.com/spreadsheets/d/1TR5G47Vod-z4LYL8L5ptrYjAFKCOhmeneQodZjO19qE'
SHEET = GSPREAD_CLIENT.open_by_url(SHEET_URL)

class Expense:
    """Expense entry."""
    def __init__(self, name, amount, category, date):
        self.name = name
        self.amount = amount
        self.category = category
        self.date = datetime.strptime(date, "%d-%m-%Y")

    def __str__(self):
        return f"{self.date.strftime('%Y-%m-%d')} - {self.name} - {self.category} - €{self.amount:.2f}"

class ExpenseTracker:
    """Manages the expense tracking application."""
    def __init__(self, spreadsheet):
        self.expense_sheet = spreadsheet.worksheet('expenses')
        self.categories_sheet = spreadsheet.worksheet('categories')
        self.expenses = []
        self.expense_categories = self.load_categories()
        self.user_budget = self.get_user_budget()
        self.setup_logger()

def setup_logger(self):
        """Set up a logger for the application."""
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler = logging.FileHandler('expense_tracker.log')
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

def set_user_budget(self, budget):
        """Set the user's monthly budget."""
        self.user_budget = budget

def get_user_budget(self):
        """Prompt  user for their monthly budget."""
        return float(input("Enter your monthly budget: "))

def colorize(self, text, color):
        """Add color formatting to text."""
        colors = {
            "red": "\033[91m",
            "green": "\033[92m",
            "white": "\033[0m",
        }
        return f"{colors[color]}{text}{colors['white']}"

def load_data(self, sheet, column):
        """Load data from specific column in Google Sheets worksheet."""
        try:
            column_obj = sheet.find(column)
            if column_obj:
                data = sheet.col_values(column_obj.col)
                data.pop(0)  # Remove the header
                return data
            else:
                return []  # Column not found
        except Exception as e:
            self.logger.error(f"Error loading data from Google Sheets: {e}")
            return []

def save_data(self, sheet, data, range_name):
        """Save data to a specific range in a Google Sheets worksheet."""
        try:            
            # Clear the existing data in the range
            sheet.values().clear(spreadsheetId=self.spreadsheet.id, range=range_name).execute()

            # Prepare the data for writing
            values = [
                data,
            ]

            # Write the new data to the range
            body = {
                "values": values,
            }
            result = sheet.values().update(spreadsheetId=self.spreadsheet.id, range=range_name, valueInputOption="RAW", body=body).execute()
        except Exception as e:
            self.logger.error(f"Error saving data to Google Sheets: {e}")

def summarize_expenses(self):
        """Summarize user's expenses and display the summary."""
        category_totals = {}
        total_expenses = 0

        for expense in self.expenses:
            total_expenses += expense.amount
            category_totals[expense.category] = category_totals.get(expense.category, 0) + expense.amount

        budget = self.user_budget

        if total_expenses < budget:
            total_expenses_formatted = self.colorize(f'€{total_expenses:.2f}', 'green')
            outstanding_budget = self.colorize(f'€{budget - total_expenses:.2f}', 'green')
        elif total_expenses > budget:
            total_expenses_formatted = self.colorize(f'€{total_expenses:.2f}', 'red')
            outstanding_budget = self.colorize(f'€{budget - total_expenses:.2f}', 'red')
        else:
            total_expenses_formatted = self.colorize(f'€{total_expenses:.2f}', 'white')
            outstanding_budget = self.colorize(f'€{budget - total_expenses:.2f}', 'white')

        print(f"Total Expenses: {total_expenses_formatted}")
        print(f"Outstanding Monthly Budget: {outstanding_budget}")
        print("Category-wise Expenses:")
        for category, amount in category_totals.items():
            formatted_amount = self.colorize(f'€{amount:.2f}', 'green')
            print(f"{category}: {formatted_amount}")

def load_expenses(self):
        """Load expenses data from Google Sheets and convert it to Expense objects.

        Returns:
            list: list of Expense objects.
        """
        try:
            expense_data = self.load_data(self.expense_sheet, "Expense Name")
            amount_data = self.load_data(self.expense_sheet, "Amount")
            category_data = self.load_data(self.expense_sheet, "Category")

            expenses = []

            for name, amount, category in zip(expense_data, amount_data, category_data):
                expenses.append(Expense(name, float(amount), category))

            return expenses
        except Exception as e:
            self.logger.error(f"Error loading expenses from Google Sheets: {e}")
            return []

def save_expenses(self):
        """Save expenses data to Google Sheets."""
        try:
            expense_names = ["Expense Name"] + [expense.name for expense in self.expenses]
            expense_amounts = ["Amount"] + [str(expense.amount) for expense in self.expenses]
            expense_categories = ["Category"] + [expense.category for expense in self.expenses]

            data_to_save = [expense_names, expense_amounts, expense_categories]

            self.expense_sheet.update(data_to_save)
        except Exception as e:
            self.logger.error(f"Error saving expenses to Google Sheets: {e}")

def load_categories(self):
        """Load expense categories from Google Sheets."""
        try:
            categories = self.load_data(self.categories_sheet, "Category")
            print("Loaded categories:", categories)  
            return categories
        except Exception as e:
            self.logger.error(f"Error loading categories from Google Sheets: {e}")
            return []

def edit_item(self, items, item_type):
        """Edit an item in specified list of items."""
        try:
            self.display_items(items, item_type)
            item_index = int(input(f"Enter the index of the {item_type.lower()} to edit: ")) - 1
            if item_index in range(len(items)):
                new_value = input(f"Enter the new value for '{items[item_index]}': ")
                items[item_index] = new_value
                self.save_data(items, self.categories_file_path)
                print(f"{item_type} updated successfully.")
            else:
                print("Invalid index.")
        except Exception as e:
            self.logger.error(f"Error editing item: {e}")
