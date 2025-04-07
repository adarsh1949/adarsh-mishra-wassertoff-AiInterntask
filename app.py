import sys
sys.stdout = sys.stderr = open(os.devnull, 'w')python import os
print("DEBUG: Current directory:", os.getcwd())
print("DEBUG: Files in directory:", os.listdir())from flask import Flask, jsonify
import json  # Add this import

app = Flask(__name__)

# Sample email data storage
email_logs = [
    {"sender": "john@example.com", "receiver": "you@gmail.com", "subject": "Meeting"},
    {"sender": "alice@company.com", "receiver": "you@gmail.com", "subject": "Project Update"}
]

@app.route('/')
def show_emails():
    return jsonify({"status": "AI Email Assistant Running", "emails": email_logs})

@app.route('/emails')
def get_emails():
    return jsonify(email_logs)

if __name__ == '__main__':
    # Disable verbose logging
    import logging
    log = logging.getLogger('werkzeug')
    log.setLevel(logging.ERROR)
    
    print("AI Email Assistant is Running!")
    print("Email logs available at http://localhost:5000/emails")
    app.run(debug=False)