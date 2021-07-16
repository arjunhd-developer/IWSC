import gspread as gsp
from google.oauth2 import service_account


SCOPE = [
    "https://spreadsheets.google.com/feeds",
    'https://www.googleapis.com/auth/spreadsheets',
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

SERVICE_ACCOUNT_FILE = "google-credentials.json"

creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPE)


class Gspread:
    def __init__(self):
        self.client = gsp.authorize(credentials=creds)
        self.main_sheet = self.client.open("Webinar Schedule 2021")\
            .worksheet("Main Response")
        self.main_data = self.main_sheet.get_all_records()

    def get_records(self):
        self.main_sheet = self.client.open("Webinar Schedule 2021") \
            .worksheet("Main Response")
        self.main_data = self.main_sheet.get_all_records()
        self.main_data = self.main_sheet.get_all_records()

    def sort_alpha(self):
        self.main_sheet.sort((3, 'asc'))

    def sort_region(self):
        self.main_sheet.sort((7, 'asc'))
