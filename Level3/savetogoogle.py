import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import main
from web_scrap import OLXScraping
import pandas as pd
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

# The ID and range of a sample spreadsheet.
SPREADSHEET_ID = "1qg6A6ySbRXOs3RpkUGOKezYwbRKeQ6fHFLFgt2IgZBk"
RANGE_NAME = "Sheet1!A1"


CSV_FILE_PATH = "Data.csv"

def readcsv():
    df = pd.read_csv(CSV_FILE_PATH)
    values = df.values.tolist()
    header = df.columns.tolist()
    return [header] + values

def main():
    creds = None

    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    try:
        service = build("sheets", "v4", credentials=creds)

        # Call the Sheets API
        valueData = readcsv()

        sheet = service.spreadsheets()
        result = (
            sheet.values()
            .update(
                spreadsheetId=SPREADSHEET_ID,
                range=RANGE_NAME,
                valueInputOption="USER_ENTERED",
                body={"values": valueData},
            )
            .execute()
        )

    except HttpError as err:
        print(err)


if __name__ == "__main__":
    main()
