from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from config import SCOPES, CREDENTIALS_FILE

def get_calendar_service():
    flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, SCOPES)
    creds = flow.run_local_server(port=0)
    return build("calendar", "v3", credentials=creds)

def create_event(summary, start_time, end_time):
    service = get_calendar_service()
    event = {
        "summary": summary,
        "start": {"dateTime": start_time, "timeZone": "UTC"},
        "end": {"dateTime": end_time, "timeZone": "UTC"},
    }
    service.events().insert(calendarId="primary", body=event).execute()

if __name__ == "__main__":
    create_event("AI Meeting", "2025-04-01T10:00:00", "2025-04-01T11:00:00")
