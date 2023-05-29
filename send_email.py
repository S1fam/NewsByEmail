import smtplib
import ssl
# import os


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "YOUR GMAIL"
    password = "YOU GMAIL APP PASSWORD"  # os.getenv("PASSWORD2")

    receiver = "YOUR GMAIL"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
