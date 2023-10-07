import smtplib # Simple Mail Transfer Protocol -> SMTP
from email.message import EmailMessage # EmailMessage class
from string import Template # Template class
from pathlib import Path # Path class - similar to os.path

html = Template(Path("index.html").read_text()) # Read the html file and save it as a Template object
email = EmailMessage() # Create an instance of EmailMessage class
email["from"] = "" # Sender Format -> Name <email>
email["to"] = "" # Receiver Format -> email
email["subject"] = "You won a holiday!" # Subject of the email

email.set_content(html.substitute({"name": ""}), "html") # Content of the email

#use the smtp server for login for outlook
with smtplib.SMTP(host="smtp-mail.outlook.com", port=587) as smtp:
    smtp.ehlo() # Identify yourself with the mail server
    smtp.starttls() # Encrypt the traffic -> Transport Layer Security
    smtp.login("","") # Login Format -> email, password
    smtp.send_message(email) # Send the email
    print("All good boss!") # Success message
