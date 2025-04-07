from slack_sdk import WebClient
from config import SLACK_BOT_TOKEN

client = WebClient(token=SLACK_BOT_TOKEN)

def send_slack_message(message, channel="#general"):
    client.chat_postMessage(channel=channel, text=message)

if __name__ == "__main__":
    send_slack_message("Test message from AI Email Assistant!")
