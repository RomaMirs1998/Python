# Python Email Sender

This project provides a simple implementation to send emails using Python's `smtplib` and `email.message.EmailMessage` classes.

## Features:
1. Send a plain text email.
2. Send an HTML email using a template.

## Requirements:
- Python 3.x
- An active email account to send the email from.

## Usage:

### Sending a Plain Text Email:
```python
import smtplib
from email.message import EmailMessage

email = EmailMessage()
email["from"] = "Your Name <your_email@example.com>"
email["to"] = "receiver_email@example.com"
email["subject"] = "You won 1,000,000 dollars!"

email.set_content("I am a Python Master!")

with smtplib.SMTP(host="smtp-mail.outlook.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("your_email@example.com","your_password")
    smtp.send_message(email)
    print("All good boss!")

```

Sending an HTML Email using a Template:

First, create an HTML template. Here's an example index.html:

```html

<!DOCTYPE html>
<html lang="en">
<head>
    <!-- Metadata and other head elements -->
</head>
<body>
    You just won a free trip $name
</body>
</html>
```

Now, use the following code to send the email using the template:

```python

import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path("index.html").read_text())
email = EmailMessage()
email["from"] = "Your Name <your_email@example.com>"
email["to"] = "receiver_email@example.com"
email["subject"] = "You won a holiday!"

email.set_content(html.substitute({"name": "Receiver's Name"}), "html")

with smtplib.SMTP(host="smtp-mail.outlook.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("your_email@example.com","your_password")
    smtp.send_message(email)
    print("All good boss!")
```


Notes:

    Make sure to replace placeholders like your_email@example.com, receiver_email@example.com, your_password, and Receiver's Name with appropriate values.
    Always ensure your email credentials are stored securely and never hard-coded or committed to version control.
    Use appropriate mail servers depending on your email service provider. The above examples use Outlook's SMTP server. If you're using another service like Gmail, replace smtp-mail.outlook.com with the appropriate SMTP server.