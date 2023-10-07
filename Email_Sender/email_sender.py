import smtplib # Simple Mail Transfer Protocol -> SMTP
from email.message import EmailMessage # EmailMessage class

email = EmailMessage() # Create an instance of EmailMessage class
email["from"] = "" # Sender Format -> Name <email>
email["to"] = "" # Receiver Format -> email
email["subject"] = "You won 1,000,000 dollars!" # Subject of the email

email.set_content("I am a Python Master!") # Content of the email

#use the smtp server for login for outlook
# if you want to use gmail, use smtp.gmail.com
with smtplib.SMTP(host="smtp-mail.outlook.com", port=587) as smtp:
    smtp.ehlo() # Identify yourself with the mail server
    smtp.starttls() # Encrypt the traffic -> Transport Layer Security
    smtp.login("","") # Login Format -> email, password
    smtp.send_message(email) # Send the email
    print("All good boss!") # Success message
