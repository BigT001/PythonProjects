from email.message import EmailMessage
from appPass import password

email_sender = "sta99175@gmail.com"
email_password = password

import ssl
import smtplib

email_receiver = input("Enter email: ")

subject = "Complete signup"
body = """
One more step. click the link to complete signup.
"""

print("Check your email!")

em = EmailMessage()
em["From"] = email_sender
em["To"] = email_receiver
em["Subject"] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())