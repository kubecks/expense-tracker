import logging
import gspread
from google.oauth2.service_account import Credentials
from tabulate import tabulate
from datetime import datetime
import warnings

# Suppress UserWarning from gspread
warnings.filterwarnings("ignore", category=UserWarning, module="gspread")
warnings.filterwarnings("ignore", category=DeprecationWarning, module="gspread")

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
    def __init__(self, name, amount, category, date_str):
        self.name = name
        self.amount = amount
        self.category = category
        self.date = self.validate_date(date_str)
    
    @staticmethod
    def validate_date(date_str):
        """Validates and converts the date string to a datetime object."""
        try:
            return datetime.strptime(date_str, "%d-%m-%Y")
        except ValueError:
            raise ValueError("Date must be in DD-MM-YYYY format")
    
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
        """Prompt user for their monthly budget."""
        while True:
            try:
                budget = float(input("Enter your monthly budget: "))
                if budget < 0:
                    raise ValueError("Budget cannot be negative.")
                return budget
            except ValueError as e:
                print(f"Invalid input: {e}")

    def colorize(self, text, color):
            """Add color formatting to text."""
            colors = {
                "red": "\033[91m",
                "green": "\033[92m",
                "white": "\033[0m",
            }
            return f"{colors[color]}{text}{colors['white']}"

    def load_data(self, sheet, column_name):
            """Load data from specific column in Google Sheets worksheet."""
            try:
                # Find the cell with the specified header name
                header_cell = sheet.find(column_name)
                if header_cell:
                    # Make sure the found cell is in the first row
                    if header_cell.row == 1:
                        # Get all values in the column
                        column_data = sheet.col_values(header_cell.col)
                        # Remove the header
                        column_data.pop(0)
                        return column_data
                    else:
                        self.logger.error(f"Header '{column_name}' found but not in the first row.")
                        return []
                else:
                    self.logger.error(f"Header '{column_name}' not found in the sheet.")
                    return []
            except Exception as e:
                self.logger.error(f"Error loading data from Google Sheets: {e}")
                return []

    def save_data(self, sheet, data, range_name):                
            try:
                sheet = self.categories_sheet
                column = 'A'  # Assuming 'Category' data is in the first column
                # Directly using 1 for the column index as 'A' corresponds to the first column
                col_index = 1

                # Clear existing content in the column after the header.
                sheet.batch_clear([f"{column}2:{column}{len(data)+100}"])  # Adjust as needed

                # Update the sheet with new data.
                for i, value in enumerate(data, start=2):  # Starting from row 2 to keep the header
                    sheet.update_cell(i, col_index, value)

                self.logger.info("Categories updated successfully.")
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
                    placeholder_date = "01-01-2000"  # Placeholder date
                    if amount.replace('.', '', 1).isdigit(): # Check if amount is a digit before conversion
                        expenses.append(Expense(name, float(amount), category, placeholder_date))

                return expenses
            except Exception as e:
                self.logger.error(f"Error loading expenses from Google Sheets: {e}")
                return []

    def prepare_expense_data_for_sheet(self):
            """Prepare the expense data for Google Sheets."""
            expense_data = [["Expense Name", "Amount", "Category"]]  
            for expense in self.expenses:
                # Append each expense's details as a list
                expense_data.append([expense.name, expense.amount, expense.category])
            return expense_data

    def update_sheet_data(self, data, start_cell='A1'):
            """Update the Google Sheet with given data starting from the start_cell."""
            try:
                # Use batch update for efficiency
                self.expense_sheet.update(range_name=start_cell, values=data, value_input_option='USER_ENTERED')
                self.logger.info("Google Sheet updated successfully.")
            except Exception as e:
                self.logger.error(f"Error updating Google Sheet: {e}")

    def save_expenses(self):
            """Save expenses data to Google Sheets."""
            try:
                expense_data = self.prepare_expense_data_for_sheet()
                self.update_sheet_data(expense_data)
            except Exception as e:
                self.logger.error(f"Error saving expenses to Google Sheets: {e}")
                print("Failed to save expenses to Google Sheets.")

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
                self.display_items(self.expense_categories, item_type)
                item_index = int(input(f"Enter the index of the {item_type.lower()} to edit: ")) - 1
                if item_index in range(len(self.expense_categories)):
                    new_value = input(f"Enter the new value for '{self.expense_categories[item_index]}': ")
                    self.expense_categories[item_index] = new_value
                    # Update the category in Google Sheets
                    self.update_categories_sheet()
                    print(f"{item_type} updated successfully.")
                else:
                    print("Invalid index.")
            except Exception as e:
                self.logger.error(f"Error editing item: {e}")

    def delete_item(self, items, item_type):
            """Delete item in specified list of items.""" 
            try:
                self.display_items(self.expense_categories, item_type)
                item_index = int(input(f"Enter the index of the {item_type.lower()} to delete: ")) - 1
                if item_index in range(len(self.expense_categories)):
                    deleted_item = self.expense_categories.pop(item_index)
                    # Update the category in Google Sheets
                    self.update_categories_sheet()
                    print(f"{item_type} '{deleted_item}' deleted successfully.")
                else:
                    print("Invalid index.")
            except Exception as e:
                self.logger.error(f"Error deleting item: {e}")                
                
    def update_categories_sheet(self):
        """Update the categories sheet in Google Sheets."""
        try:
            # Prepare the category data for Google Sheets
            category_data = [["Category"]] + [[cat] for cat in self.expense_categories]
            # Update the categories sheet with the new data
            self.categories_sheet.update('A1', category_data, value_input_option='USER_ENTERED')
        except Exception as e:
            self.logger.error(f"Error updating categories in Google Sheets: {e}")
                
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
                        self.save_data(self.categories_sheet, self.expense_categories, "Category")
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
            print("🎯 Getting User Expense")
            name = input("Enter expense name: ")
            amount = self.get_valid_amount()
            date_str = self.get_valid_date()
            category = self.choose_category()
            return Expense(name, amount, category, date_str)

    def get_valid_amount(self):
            """Get and validate expense amount from user."""
            while True:
                try:
                    amount = float(input("Enter expense amount: "))
                    if amount < 0:
                        raise ValueError("Amount cannot be negative.")
                    return amount
                except ValueError as e:
                    print(f"Invalid input: {e}. Please enter a valid number.")

    def get_valid_date(self):
            """Get and validate expense date from user."""
            while True:
                date_str = input("Enter expense date (DD-MM-YYYY): ")
                try:
                    datetime.strptime(date_str, "%d-%m-%Y")
                    return date_str
                except ValueError:
                    print("Invalid date format. Please use DD-MM-YYYY.")
            
    def choose_category(self):
            """Allow user to choose an expense category."""
            while True:
                print("Select a category: ")
                for i, category_name in enumerate(self.expense_categories, start=1):
                    print(f"{i}. {category_name}")
                try:
                    selected_index = int(input("Enter a category number: ")) - 1
                    if 0 <= selected_index < len(self.expense_categories):
                        return self.expense_categories[selected_index]
                    else:
                        print("Invalid category number.")
                except ValueError:
                    print("Please enter a valid number.")                 

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

                    # Display categories for selection
                    self.display_items(self.expense_categories, "Category")
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
                    removed_expense = self.expenses.pop(expense_index)
                    self.save_expenses()
                    print(f"Expense '{removed_expense}' removed successfully.")
                else:
                    print("Invalid option.")
            else:
                print("Invalid expense index.")
                
    def run_menu_option(self, option):
            """Run the selected menu option."""
            if option == "1":
                expense = self.get_user_expense()
                self.expenses.append(expense)
                self.save_expenses()
                print("Expense added successfully.")
            elif option == "2":
                self.display_expenses()
            elif option == "3":
                self.edit_or_remove_expense()
            elif option == "4":
                new_budget = self.get_user_budget()
                self.set_user_budget(new_budget)
                print(f"Monthly budget adjusted to €{new_budget:.2f}")
            elif option == "5":
                self.manage_items(self.expense_categories, "Category")
            elif option == "6":
                self.summarize_expenses()
            elif option == "7":
                return "exit"  # Signal to exit the loop
            else:
                print("Invalid choice. Please try again.")
            
    def run(self):
        """Run the main application loop."""
        try:
            self.load_expenses()  # Load expenses once at the start
            while True:
                print("Expense Tracker Menu")
                print("1. Add Expense")
                print("2. Display Expenses")
                print("3. Edit/Remove Expense")
                print("4. Adjust Monthly Budget")
                print("5. Manage Categories")
                print("6. Summarize Expenses")
                print("7. Exit")

                option = input("Select an option: ")
                if option == "7":
                    break  # Exit the loop if option 7 is selected
                self.run_menu_option(option)
        
        except KeyboardInterrupt:
            print("\nExiting the application. Goodbye!")
        except ValueError as e:
            self.logger.error(f"Value error: {e}")
            print(f"An error occurred: {e}")
        except Exception as e:
            self.logger.error(f"Unexpected error in the main loop: {e}")
            print("An unexpected error occurred. Exiting the application.")
                    

    def main(self):
            """Main function that initializes logging and runs the application."""
            print(f"🎯 Running Expense Tracker!")
            logging.basicConfig(level=logging.INFO)
            self.run()

if __name__ == "__main__":
        expense_tracker = ExpenseTracker(SHEET)
        expense_tracker.main()
