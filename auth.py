from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import os

SCOPES = [#'https://www.googleapis.com/auth/gmail.readonly']

def authenticate_gmail():
    flow = InstalledAppFlow.from_client_config({
    "installed": {
        "client_id": "123abc.apps.googleusercontent.com",
        ...
    }
}, SCOPES)
    

    # 🔥 Save the token to token.json
    with open('', 'w') as token_file:
        token_file.write(creds.to_json())

    return creds

creds = authenticate_gmail()
service = build('gmail', 'v1', credentials=creds)

print("✅ Successfully authenticated with Gmail API!")
