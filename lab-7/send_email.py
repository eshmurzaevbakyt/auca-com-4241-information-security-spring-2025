import smtplib
from email.mime.text import MIMEText
sender_email = "test_user@gmail.com"
sender_password = "12345678"
receiver_email = "reciever_test@gmail.com"
subject = "Server Status"
body = "Hello, this is an automated email fromthe server's cron job."
msg = MIMEText(body)
msg["From"] = sender_email
msg["To"] = receiver_email
msg["Subject"] = subject
try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, receiver_email, msg.as_string())
    server.quit()
    print("Email sent successfully!")
except Exception as e:
    print(f"Error sending email: {e}")

