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
