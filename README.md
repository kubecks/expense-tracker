# Expense Tracker
 
Link to [Expense Tracker](https://easy-budgeting-bbe77dad071c.herokuapp.com/)


 **Why Expense Tracker?**:
- **Accessibility**: Track your finances on the go with our cloud-based storage
- **Customization**: Tailor the app to your specific needs with customizable expense categories.
- **Insights**: Get insights into your spending habits, helping you stay within budget and save money.

![AmIResponsive](/images/Budgettracker1.png)

## Table of Contents
 1. About
 2. Features
 3. Technologies Used
 4. Setup and Installation
 5. Usage
 6. Project Structure
 7. Testing
 8. Deployment
 9. Credits
 10. Acknowledgments

## About

The Expense Tracker is a command-line application made to simplify personal finance management with precision. Managing finances plays a big role in our overall acievements as it's a cornerstone of personal success when managed properly. `This tool provides a straightforward solution for monitoring and organising one's expenses to ensure they achieve their goals.

**Motivation**: The creation of this Expense Tracker was driven by the urge to help users make informed decisions with their finances. The app does exactly this due to its easy to use and user-friendliness that caters to the budgeting needs of anyone, regardless of how  tech savy they are. 

**Core Functionality**:
- **Budget Setting**: Users can set a monthly budget to track their spending against.
- **Expense Logging**: The application allows for quick and easy logging of expenses, categorizing them for better organization.
- **Financial Overview**: At a glance, users can see a summary of their expenses and how they align with their budget.

**Unique Selling Points**:
- **Google Sheets Integration**: Secure and real-time synchronization with Google Sheets ensuring data is up to date and accessible from anywhere.
- **Interactive Reports**: Visual summaries and categorization provide insights into your financial health.

### How To Use:

**Getting Started**

1. Open your terminal.
2. Navigate to the project's directory.
3. Run the application using the command: `python run.py`

**Usage**

Upon launching the application, you'll be presented with a menu of options and prompts to guide you through managing your expenses.

**Set Your Monthly Budget**

- You'll be prompted to enter your desired monthly budget. This helps in tracking your spending against your budget.

![SetBudget](/images/Start.png)

**Main Menu Options**

From the main menu, you can select from the following actions:

- **1. Add Expense**: Input the name, amount, date, and category for any new expense.
- **2. Display Expenses**: View a list and summary of all recorded expenses.
- **3. Edit/Remove Expense**: Modify or delete expenses using their index number.
- **4. Adjust Monthly Budget**: Update your monthly budget as needed.
- **5. Manage Categories**: Customize your expense categories by adding, editing, or deleting them.
- **6. Summarize Expenses**: Get a detailed summary of your expenses and how they compare to your budget.
- **7. Exit**: Safely exit the application.

![Menu](/images/Main-Menu.png)

### Navigating the Main Menu

### Adding an Expense
- Select option `1` from the main menu.
- Follow the prompts to enter the expense name, amount, date (in DD-MM-YYYY format), and category.
- Once submitted, the expense will be recorded and categorized accordingly.

### Viewing Expenses
- Choose option `2` to display a list of all expenses. You’ll see each expense’s name, amount, category, and date.

### Editing or Removing an Expense
- To edit or remove an expense, select option `3`.
- Use the expense’s index number to select it for editing or removal.
- Follow the prompts to update the expense details or confirm its deletion.

### Adjusting Your Budget
- If you need to update your monthly budget, choose option `4` and enter the new amount when prompted.

### Managing Categories
- By selecting option `5`, you can add, edit, or delete expense categories to better organize your expenses.

### Summarizing Expenses
- Option `6` provides a summary of your expenses, comparing them to your monthly budget. This feature helps in identifying areas where adjustments may be needed.

### Exiting the Application
- To exit the Expense Tracker, select option `7`. If prompted, ensure you save any changes before exiting.

By following these steps, you can effectively manage your expenses and keep track of your financial health with the Expense Tracker.

**Interacting with the Application**

- Follow the on-screen prompts to provide the required information for each action.
- Select expenses for editing or removal by their listed index number.

**Review and Adjust**
- Regularly review the expense summary to monitor your financial health.
- Adjust your budget or spending based on insights gained.

![Summarize](/images/Summarize.png)

**Exiting the Application**

- To close the application, select option **`7`**. Be sure to save any changes if prompted before exiting.

### User Stories

#### End Users

**First-Time Users**
- **As a first-time user**, I want to easily understand the main purpose of the app, so I can decide how it could help me manage my expenses.
- **As a first-time user**, I want to easily navigate through the app, so I can find and use its features without confusion.
- **As a first-time user**, I want to quickly set up my monthly budget, so I can start tracking my expenses right away.

**Returning Users**
- **As a returning user**, I want to view a summary of my current month's spending compared to my budget, so I can adjust my spending habits if necessary.
- **As a returning user**, I want to add, edit, or remove expenses easily, so I can keep my expense tracking up to date.
- **As a returning user**, I want to create and manage custom categories

## Features

The Expense Tracker offers a wide range of features created to simplify personal finance management. Here's what makes this Expense Tracker stand out:

### Simple Budget Setting
- **Monthly Budget Configuration**: Users set and adjust their monthly budget, making it easy for them to have a clear financial goal monthly.

### Comprehensive Expense Management
- **Add Expenses Quickly**: Users can quickly log expenses, including details such as name, amount, date, and category.
- **View Expenses**: Shows a detailed list of all expenses.
- **Edit and Remove Expenses**: Gives users ability to modify or delete expenses as needed, ensuring the accuracy of financial records.

### Customizable Categories
- **Manage Expense Categories**: Users can customize their expense tracking by adding, editing, or deleting categories to suit their personal or organizational needs.

### Financial Overview and Insights
- **Summarize Expenses**: Provides a summary of expenses versus the budget, offering insights into spending habits and financial health.
- **Visual and Interactive Reports**: With Google Sheets integration, users can access visual summaries and categorization of expenses for better financial analysis.

### Google Sheets Integration
- **Real-Time Data Sync**: Changes made in the application are immediately updated in Google Sheets, ensuring data is always current.
- **Accessible Anywhere**: Expenses are stored in Google Sheets, making them accessible from any device, anywhere.

### User-Friendly Interface
- **Intuitive Command-Line Interface**: Designed with simplicity in mind, the application guides users through each step with clear prompts and instructions.
- **Quick Navigation**: Users can easily navigate through the menu options and perform actions efficiently.

### Secure and Reliable
- **Data Integrity**: With Google Sheets as the backend, users can trust in the security and reliability of their financial data.
- **Safe Exit**: Users can exit safely, with a prompt to save any unsaved changes.

## Technologies Used

The Expense Tracker is built with a combination of programming languages, libraries, and tools that ensure its functionality, efficiency, and user-friendly interface. Below is a detailed list of the technologies used in the development of this application:

### Programming Languages
- **Python**: The core backend logic of the Expense Tracker is developed in Python, making use of its simplicity and extensive library support for data manipulation and interaction with Google Sheets.

### Libraries and Frameworks
- **gspread**: A Python API for Google Sheets, gspread is used to read from and write to Google Sheets, acting as the database for storing expense data.
- **Google OAuth2**: Used for authenticating access to Google Sheets, ensuring secure data handling.
- **tabulate**: This is employed to format the display of expenses in a table-like structure, enhancing readability.
- **datetime**: Part of the Python Standard Library, datetime is used for handling dates and times, crucial for logging and organizing expenses by date.

### Tools and Platforms
- **Google Sheets**: Storing all expense data in a structured manner.
- **Git**: Used for version control, allowing for efficient tracking of changes.
- **GitHub**: Hosts the project repository, providing a platform for code storage & management.
- **Visual Studio Code (VS Code)**: A Integrated Development Environment (IDE) that supports Python development and version control through Git.

### Other Technologies
- **Command-Line Interface (CLI)**: The application is designed to be run in a terminal or command prompt, offering a straightforward, text-based interface for user interaction.

By leveraging these technologies, the Expense Tracker provides a robust and user-friendly tool for managing personal finances with the  accessibility of Google Sheets.

## Setup and Installation

Getting the Expense Tracker operational involves several straightforward steps. Before anything else [download Python](https://www.python.org/downloads/) and follow the installation instructions for your operating system.

### Step 1: Clone the Repository
Start by cloning the project repository from GitHub to your local machine. Open your terminal, navigate to the directory where you want to store the project, and run:
git clone https://github.com/kubecks/expense-tracker

### Step 2: Set Up a Virtual Environment (Optional but Recommended)
To avoid conflicts between project dependencies, it's a good practice to create a virtual environment. 

1. Navigate to the project directory:

     - cd expense-tracker

2. Create the virtual environment:
     - python -m venv venv

3. Activate the virtual environment:

On Windows:
 - venv\Scripts\activate

On macOS and Linux:
 - source venv/bin/activate

### Step 3: Install Dependencies
With your virtual environment active, install the project dependencies using pip:
pip install -r requirements.txt

### Step 4: Set Up Google Sheets API Credentials
To interact with Google Sheets, you'll need to set up Google API credentials:

1. Visit the [Google Cloud Platform](https://console.cloud.google.com/welcome?pli=1&project=sampleproject-397012).
2. Create a new project.
3. Enable the Google Sheets API for your project.
4. Create credentials (service account key) for your project and download them as a JSON file.
5. Rename the downloaded file to `creds.json` and place it in the root directory of the project.

### Step 5: Share Your Google Sheet
The application uses a specific Google Sheet as its database. Create a new Google Sheet and share it with the email address provided in your `creds.json` file (found under `client_email`).

### Step 6: Update the SHEET_URL in the Application
Open the `run.py` file (or where the SHEET_URL is defined) and replace the existing SHEET_URL with the URL of your newly created Google Sheet.

### Step 7: Running the Application
With everything set up, you're now ready to launch the Expense Tracker. In your terminal, ensure you are still in the project directory and activate your virtual environment if it's not already active. 

Follow the on-screen instructions to begin tracking your expenses.

## Project Structure

The Expense Tracker project is organized into a clean and manageable structure. Below is an outline of the main components and their purpose within the project:

### Key Files

- `run.py`: The entry point script that runs the Expense Tracker application.
- `expense.py`: Defines the Expense class and related expense management functionality.
- `README.md`: Provides detailed information about the project, how to set it up, and how to use it.

### Configuration and Data Files

- `creds.json`: Contains the credentials required for Google Sheets API integration.
- `.gitignore`: Lists files and directories ignored by git, ensuring sensitive information is not committed to version control.
- `requirements.txt`: Lists all Python dependencies necessary for the project, which can be installed using `pip`.

### Directories

- `__pycache__`: Contains Python 3 bytecode compiled and cached files, which are automatically generated by Python to speed up module loading.
- `.devcontainer`: Configuration files for developing inside a container using Visual Studio Code Remote - Containers extension.

## Testing

Thorough testing has been done to ensure the Expense Tracker operates reliably and handles various types of input gracefully. The testing process encompasses several aspects to maintain the quality and integrity of the application.

### Manual Testing

Manual testing was performed extensively to cover the following:

- **Functionality Testing**: Every feature, including adding, displaying, editing, and removing expenses, as well as adjusting the budget and managing categories, was tested to verify that it functions as expected.
- **User Input Validation**: Tests were performed to ensure that the system handles invalid inputs correctly, prompting the user for re-entry of data when necessary.
- **Data Persistence**: Interactions with Google Sheets were tested to ensure that all data manipulations were persisted correctly and that the data remains consistent and accurate.
- **Boundary Conditions**: Edge cases, such as entering extreme values or testing the application's response to unexpected operational scenarios, were also tested.

### Test Cases

- **Test Case 1**: Add Expense
  - **Objective**: To test if the application correctly adds an expense to the list.
  - **Procedure**: Choose 'Add Expense' from the main menu and enter the expense details as prompted.
  - **Expected Result**: The expense is added to the Google Sheet and can be viewed in the 'Display Expenses' list.

- **Test Case 2**: Invalid Date Entry
  - **Objective**: To test the application's response to an incorrectly formatted date.
  - **Procedure**: Attempt to add an expense with an invalid date format.
  - **Expected Result**: The application prompts the user to re-enter the date in the correct DD-MM-YYYY format.

- **Test Case 3**: Edit Expense
  - **Objective**: To verify that the expense editing function works correctly.
  - **Procedure**: Select an existing expense to edit, change the amount and category, and save the changes.
  - **Expected Result**: The changes are reflected immediately in the expenses list and the Google Sheet.

- **Test Case 4**: Remove Expense
  - **Objective**: To ensure that the remove expense feature correctly deletes an expense from the system.
  - **Procedure**: Choose an expense to remove and confirm the deletion.
  - **Expected Result**: The expense is permanently removed from the Google Sheet and no longer appears in the expenses list.

- **Test Case 5**: Adjust Monthly Budget
  - **Objective**: To test the functionality of updating the monthly budget.
  - **Procedure**: Access the 'Adjust Monthly Budget' feature and enter a new budget amount.
  - **Expected Result**: The new budget amount is stored and used for subsequent expense summary calculations.

# Deployment to Heroku

Deploying your Python application to Heroku is a smooth process with the following steps:

## Prerequisites

- A [Heroku account](https://signup.heroku.com/)
- [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli) installed
- Your application in a Git repository

## Step-by-Step Guide

### Prepare Your Application

 Include a `requirements.txt` file that lists all Python packages needed.

### Deploy Your Application

1. Open your terminal and log into Heroku:
    ```sh
    heroku login
    ```
2. Navigate to your app's directory and set up a Git remote for Heroku:
    ```sh
    heroku git:remote -a your-app-name
    ```
3. Commit your application to Git, if you haven't already:
    ```sh
    git add .
    git commit -am "Initial commit or a description of your commit"
    ```
4. Push your application to Heroku:
    ```sh
    git push heroku master
    ```

### Set Configuration Variables

- Set environment variables using the Heroku CLI:
    ```sh
    heroku config:set VARIABLE_NAME=value
    ```

### Run the Application

- Open your application in the browser:
    ```sh
    heroku open
    ```
    Or visit `https://your-app-name.herokuapp.com`.


## Credits

### Code
- **Google Sheets API**: Utilized for integrating Google Sheets for data storage and retrieval, enabling seamless management of expense data.
- **GSpread Python Library**: Employed for its powerful functionality in interacting with Google Sheets, facilitating easy data manipulation.
- **Python's `datetime` module**: Used for managing dates, essential for organizing expenses chronologically.
- **Tabulate Python Library**: Used to format the display of expenses in a table-like structure, improving readability for the user.

### Resources
- **Stack Overflow**: A crucial resource for solving both common and uncommon coding challenges encountered during development.
- **Official Python Documentation**: Served as a critical reference for understanding and applying Python's built-in features.
- **Google Sheets API Documentation**: Provided detailed guidance on integrating and manipulating Google Sheets data through API calls.
- **Code Institute - Love Sandwiches Walkthrough**: This walkthrough project served as an invaluable reference for understanding the integration of Google Sheets with a Python application. It provided foundational knowledge which significantly influenced the development of the Expense Tracker.
- [Python Google Sheets API Tutorial on YouTube](https://www.youtube.com/watch?v=IbdgcUqWSeo): Helped in understanding how to integrate Google Sheets with Python.
- [Automating with Python and Google Sheets on YouTube](https://www.youtube.com/watch?v=HTD86h69PtE&t=11s): Offered insights into automating data management tasks with Python and Google Sheets.

### Tools
- **Visual Studio Code**: The primary development environment, chosen for its extensive Python support and Git integration.
- **Git and GitHub**: Used for version control, facilitating effective tracking of changes and collaboration.

## Acknowledgments

- **Code Institute Student Support**: Deep gratitude to the Student Support team for their exceptional understanding and assistance throughout the duration of this project. Facing unforeseen challenges are part of any educational journey, and it was during these times that the support and extensions provided by the team proved invaluable. I am profoundly thankful.
- **Friends**: Thankful for the constant support, patience, and encouragement from my friends .
