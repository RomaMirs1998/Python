from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = ""
# Your Auth Token from twilio.com/console
auth_token =""

client = Client(account_sid, auth_token) # Client is a class from twilio.rest


# Send SMS
message = client.messages.create(
    from_="+12",
    body = "Hello from Python",
    to = "+43"
)

print(message.sid) # sid = session id (unique identifier for this message) -> to check if message was sent successfully
