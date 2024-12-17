import gspread
from google.oauth2.service_account import Credentials

scopes = ['https://www.googleapis.com/auth/spreadsheets']

creads = Credentials.from_service_account_file("credentials.json", scopes=scopes)
client = gspread.authorize(creads)

# copy your sheet id from google sheet
sheet_id = ""
workbook = client.open_by_key(sheet_id)
# add your sheet name
worksheet = workbook.worksheet("Sheet1")


# customise your data as of your requirements
def insert_data(worksheet, record):
    """
    Insert a single record as a new row in the Google Sheet.
    :param worksheet: gspread worksheet object
    :param record: Dictionary with keys: 'name', 'age', 'location'
    """
    values = [record['name'], record['age'], record['location']]
    worksheet.append_row(values)  # Append to the next empty row
    print("Row added:", values)


# Example Data Insertion
data = [
    {'name': 'Tarun Kumar', 'age': 20, 'location': 'Gurugram'},
    {'name': 'Desh Kumar', 'age': 21, 'location': 'Delhi'},
]

# Insert Data One by One
for record in data:
    insert_data(worksheet, record)


# for more info pleae refer to this doc
# https://docs.gspread.org/en/v6.1.3/