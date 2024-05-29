import smtplib
import ssl

from utils import get_environment_variable


def send_email_report(to_email, subject="GitHub Email Report", body=""):
    port = 465
    smtp_server = "smtp.gmail.com"
    PASSWORD = get_environment_variable('MAIL_PASSWORD')
    USERNAME = get_environment_variable('MAIL_USERNAME')

    if not USERNAME or not PASSWORD:
        raise ValueError("Mail username or password not set in environment variables")

    message = f"""\
Subject: {subject}

{body}
"""
    context = ssl.create_default_context()

    try:
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(USERNAME, PASSWORD)
            server.sendmail(USERNAME, to_email, message)
        print(f"Email sent to {to_email}")
    except Exception as e:
        print(f"Error sending email: {e}")
