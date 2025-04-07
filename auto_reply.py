import openai
import smtplib
from email.message import EmailMessage
from config import OPENAI_API_KEY, SMTP_EMAIL, SMTP_PASSWORD

openai.api_key = OPENAI_API_KEY

def generate_reply(email_body):
    prompt = f"Draft a professional reply to:\n\n{email_body}"
    response = openai.ChatCompletion.create(model="gpt-4", messages=[{"role": "user", "content": prompt}])
    return response["choices"][0]["message"]["content"]

def send_email(to_email, subject, body):
    msg = EmailMessage()
    msg["From"] = SMTP_EMAIL
    msg["To"] = to_email
    msg["Subject"] = subject
    msg.set_content(body)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(SMTP_EMAIL, SMTP_PASSWORD)
        server.send_message(msg)
