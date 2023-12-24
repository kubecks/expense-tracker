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

def delete_item(self, items, item_type):
        """Delete item in specified list of items."""
        try:
            self.display_items(items, item_type)
            item_index = int(input(f"Enter the index of the {item_type.lower()} to delete: ")) - 1
            if item_index in range(len(items)):
                deleted_item = items.pop(item_index)
                self.save_data(items, self.categories_file_path)
                print(f"{item_type} '{deleted_item}' deleted successfully.")
            else:
                print("Invalid index.")
        except Exception as e:
            self.logger.error(f"Error deleting item: {e}")
            
def display_items(self, items, item_type):
        """Display list of items w/ index numbers"""
        print(f"{item_type} List:")
        for index, item in enumerate(items, start=1):
            print(f"{index}. {item}")

def manage_items(self, items, item_type):
        """Manage items in the specified list."""
        while True:
            print(f"{item_type} Management")
            print("1. Display Items")
            print("2. Add Item")
            print("3. Edit Item")
            print("4. Delete Item")
            print("5. Exit")
            choice = input("Select an option: ")

            if choice == "1":
                self.display_items(items, item_type)
            elif choice == "2":
                new_item = input(f"Enter the new {item_type.lower()}: ")
                if new_item not in items:
                    items.append(new_item)
                    self.save_data(self.categories_sheet, items, "Category")
                    print(f"{item_type} '{new_item}' added successfully.")
                else:
                    print(f"{item_type} already exists.")
            elif choice == "3":
                self.edit_item(items, item_type)
            elif choice == "4":
                self.delete_item(items, item_type)
            elif choice == "5":
                break
            else:
                print("Invalid choice. Please try again.")

def get_user_expense(self):
        """Get user input to create a new expense."""
        print(f"🎯 Getting User Expense")
        expense_name = input("Enter expense name: ")
        expense_amount = float(input("Enter expense amount: "))
        expense_date = input("Enter expense date (DD-MM-YYYY): ")

        while True:
            print("Select a category: ")
            for i, category_name in enumerate(self.expense_categories, start=1):
                print(f"  {i}. {category_name}")

            value_range = f"[1 - {len(self.expense_categories)}]"
            selected_index = int(input(f"Enter a category number {value_range}: ")) - 1

            if selected_index in range(len(self.expense_categories)):
                selected_category = self.expense_categories[selected_index]
                new_expense = Expense(
                    name=expense_name, category=selected_category, amount=expense_amount, date=expense_date
                )
                return new_expense
            else:
                print("Invalid category. Please try again!")

def display_expenses(self):
        """Display the list of expenses in a table."""
        if not self.expenses:
            print("No expenses found.")
            return

        table_data = []
        headers = ["Index", "Date", "Expense Name", "Category", "Amount"]

        for i, expense in enumerate(self.expenses, start=1):
            table_data.append([i, expense.date.strftime('%d/%m/%Y'), expense.name, expense.category, f"€{expense.amount:.2f}"])

        print(tabulate(table_data, headers, tablefmt="pretty"))

def display_categories(self):
        """Display the existing expense categories."""
        print("Existing Categories:")
        for i, category_name in enumerate(self.expense_categories, start=1):
            print(f"  {i}. {category_name}")
        
def edit_or_remove_expense(self):
        
        """Edit or remove an expense from the list of expenses."""
        self.display_expenses()
        expense_index = int(input("Enter the index of the expense to edit/remove: ")) - 1

        if expense_index in range(len(self.expenses)):
            selected_expense = self.expenses[expense_index]

            print(f"Selected Expense: {selected_expense}")
            print("1. Edit Expense")
            print("2. Remove Expense")
            edit_or_remove_choice = input("Select an option (1 or 2): ")

            if edit_or_remove_choice == "1":
                # Edit Expense
                updated_name = input("Enter the updated expense name (or press Enter to keep the current name): ")
                updated_amount = input("Enter the updated expense amount (or press Enter to keep the current amount): ")

                self.display_categories()
                selected_category_index = input("Enter the number of the existing category to update (or press Enter to keep the current category): ")
                if selected_category_index:
                    selected_category_index = int(selected_category_index) - 1
                if selected_category_index in range(len(self.expense_categories)):
                    selected_category = self.expense_categories[selected_category_index]
                    selected_expense.category = selected_category

                if updated_name:
                    selected_expense.name = updated_name
                if updated_amount:
                    selected_expense.amount = float(updated_amount)

                self.save_expenses()
                print("Expense updated successfully.")

            elif edit_or_remove_choice == "2":
                # Remove Expense
