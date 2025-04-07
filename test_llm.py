from llm_processor import summarize_email

email_content = """Dear Chaithanya, 

I hope you're doing well. Just a reminder about our meeting scheduled for Monday at 10 AM. 
Please confirm your availability. 

Best regards,  
John"""

summary = summarize_email(email_content)
print("Summary:", summary)
