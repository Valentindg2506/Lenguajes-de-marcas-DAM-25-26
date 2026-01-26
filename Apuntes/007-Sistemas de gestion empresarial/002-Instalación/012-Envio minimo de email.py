import smtplib
from email.message import EmailMessage
import os

SMTP_SERVER = os.environ.get("EMAIL_SERVIDOR")
SMTP_PORT = 587          # 587 = STARTTLS, 465 = SSL
SMTP_USER = os.environ.get("EMAIL_USUARIO")
SMTP_PASS = os.environ.get("EMAIL_CONTRASENA")

msg = EmailMessage()
msg["From"] = "info@jocarsa.com"
msg["To"] = "jocarsa2@gmail.com"
msg["Subject"] = "Esto es un ejercicio de clase"
msg.set_content("Hola esto es una prueba desde Python.\n")

with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as smtp:
    smtp.starttls()
    smtp.login(SMTP_USER, SMTP_PASS)
    smtp.send_message(msg)

print("Email sent")
