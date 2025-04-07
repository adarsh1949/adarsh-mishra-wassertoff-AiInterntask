import sqlite3
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import os
import pickle

SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]
CREDENTIALS_FILE = "credentials.json"
DB_NAME = "emails.db"

def get_gmail_service():
    """Authenticate and return the Gmail API service using OAuth 2.0."""
    creds = None

    # Load saved credentials if available
    if os.path.exists("token.pickle"):
        with open("token.pickle", "rb") as token:
            creds = pickle.load(token)

    # If no valid credentials, request new authentication
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())  # Refresh expired token
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, SCOPES)
            creds = flow.run_local_server(port=0)

        # Save new credentials for future use
        with open("token.pickle", "wb") as token:
            pickle.dump(creds, token)

    return build("gmail", "v1", credentials=creds)

def fetch_latest_emails():
    """Fetch the latest 5 emails from Gmail inbox and store them in SQLite."""
    service = get_gmail_service()
    results = service.users().messages().list(userId="me", maxResults=5).execute()
    messages = results.get("messages", [])

    if not messages:
        print("No new emails found.")
        return

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    for msg in messages:
        msg_data = service.users().messages().get(userId="me", id=msg["id"]).execute()
        headers = {h["name"]: h["value"] for h in msg_data["payload"]["headers"]}

        sender = headers.get("From", "Unknown Sender")
        subject = headers.get("Subject", "No Subject")
        body = msg_data.get("snippet", "No Content")

        cursor.execute("INSERT OR IGNORE INTO emails VALUES (?, ?, ?, ?)", (msg["id"], sender, subject, body))

        print(f"Email ID: {msg['id']}")
        print(f"From: {sender}")
        print(f"Subject: {subject}")
        print(f"Snippet: {body}\n")

    conn.commit()
    conn.close()

if __name__ == "__main__":
    fetch_latest_emails()
