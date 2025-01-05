import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(from_email, to_email, subject, message, smtp_server, smtp_port, login, password):
    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    # Attach the message body
    msg.attach(MIMEText(message, 'plain'))

    try:
        # Connect to the SMTP server and send the email
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Secure the connection
        server.login(login, password)
        server.send_message(msg)
        server.quit()
        print("Email sent successfully.")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Example usage
from_email = "goob.robot@gmail.com"
to_email = "test@gmail.com"
subject = "Test Email"
message = "Test"
smtp_server = "smtp.gmail.com"
smtp_port = 587
login = "goob.robot@gmail.com"
password = "PASSWORD"

#Call the function
send_email(from_email, to_email, subject, message, smtp_server, smtp_port, login, password)
