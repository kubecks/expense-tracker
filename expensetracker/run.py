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
