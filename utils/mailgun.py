# utils/mailgun.py
import os
import requests

def send_mailgun_email(subject, text, to_email):
    api_key = os.getenv("MAILGUN_API_KEY")
    domain = os.getenv("MAILGUN_DOMAIN")
    from_email = os.getenv("DEFAULT_FROM_EMAIL")

    return requests.post(
        f"https://api.mailgun.net/v3/{domain}/messages",
        auth=("api", api_key),
        data={
            "from": f"Guides Website <{from_email}>",
            "to": to_email,
            "subject": subject,
            "text": text,
        },
    )
