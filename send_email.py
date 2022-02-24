import smtplib
import ssl
from email.message import EmailMessage

#Here we're assigning things to the different parts of a standard email. 
subject = "Email From Python"
body = "This is a test email from Python."
sender_email = "gurantob@gmail.com"
recipient_email = "gurantob@gmail.com"
password = input("Enter a password: ")

#This uses EmailMessage to assign our past variables to things it can operate upon. 
message = EmailMessage()
message['From'] = sender_email
message['To'] = recipient_email
message['Subject'] = subject
message.set_content(body)

#This keeps the email secure. 
context = ssl.create_default_context()

print("Sending email.")
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, recipient_email, message.as_string())

print("Success!")