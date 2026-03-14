# utils/mailgun.py
import os
import requests

def send_mailgun_email(subject: str, text: str, to_email: str):
    """
    Sends an email via Mailgun API.
    Returns the requests.Response object.
    """
    MAILGUN_DOMAIN = os.getenv("MAILGUN_DOMAIN")
    MAILGUN_API_KEY = os.getenv("MAILGUN_API_KEY")
    FROM_EMAIL = os.getenv("DEFAULT_FROM_EMAIL")

    if not (MAILGUN_DOMAIN and MAILGUN_API_KEY and FROM_EMAIL):
        raise ValueError("Mailgun environment variables not set!")

    url = f"https://api.mailgun.net/v3/{MAILGUN_DOMAIN}/messages"
    data = {
        "from": f"Guides Website <{FROM_EMAIL}>",
        "to": to_email,
        "subject": subject,
        "text": text
    }

    response = requests.post(url, auth=("api", MAILGUN_API_KEY), data=data)
    return response
