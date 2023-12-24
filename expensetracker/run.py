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
