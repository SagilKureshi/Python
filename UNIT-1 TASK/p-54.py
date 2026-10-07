import smtplib
from email.message import EmailMessage

# Email details
sender_email = "your_email@gmail.com"
receiver_email = "receiver_email@gmail.com"
app_password = "your_app_password"

# Create email
message = EmailMessage()
message["Subject"] = "Python Email"
message["From"] = sender_email
message["To"] = receiver_email

message.set_content("Hello, this email is sent using Python.")

# Connect to Gmail SMTP server
with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.login(sender_email, app_password)
    server.send_message(message)

print("Email sent successfully.")