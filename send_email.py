import os
import smtplib, ssl
from variables import os


def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    user_name = "jamessharmanpython@gmail.com"
    password = os.getenv("password_2")
    receiver = "jamessharmanpython@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(user_name, password)
        server.sendmail(user_name, receiver, message)