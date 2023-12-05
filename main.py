import json
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import json
import random
with open('keys.json') as file:
   KEYS = json.load(file)

# Sender's email address
sender_email = KEYS.get('SENDER_EMAIL')
password = KEYS.get('APP_PASSWORD')

# Recipient's email address
recipient_email = KEYS.get('RECEIVER_EMAIL')

# Email content
code = random.randint(1000, 9999)
subject = 'Book store web app'


body = f"""
Dear {KEYS.get('RECEIVER_NAME')},

We hope this message finds you well. As part of our security measures, we require you to verify your identity by entering the following verification code on our platform:

Verification Code: {code}

Please use the provided code to complete the verification process. If you did not initiate this request or have any concerns, please contact our support team immediately.

Thank you for choosing our service.

Best regards,
Book store web app

"""


# Create the MIME object
message = MIMEMultipart()
message['From'] = sender_email
message['To'] = recipient_email
message['Subject'] = subject

# Attach the body to the email
message.attach(MIMEText(body, 'plain'))

# Connect to Gmail's SMTP server
with smtplib.SMTP('smtp.gmail.com', 587) as server:
    server.starttls()
    # Log in to the Gmail account
    server.login(sender_email, password)
    # Send the email
    server.sendmail(sender_email, recipient_email, message.as_string())

print("Email sent successfully")

