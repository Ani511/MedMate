from email.message import EmailMessage
import aiosmtplib
from config import EMAIL_HOST, EMAIL_PORT, EMAIL_USERNAME, EMAIL_PASSWORD

async def send_email(to_email: str, subject: str, content: str):
    msg = EmailMessage()
    msg["From"] = EMAIL_USERNAME
    msg["To"] = to_email
    msg["Subject"] = subject
    msg.set_content(content)

    await aiosmtplib.send(
        msg,
        hostname=EMAIL_HOST,
        port=EMAIL_PORT,
        start_tls=True,
        username=EMAIL_USERNAME,
        password=EMAIL_PASSWORD,
    )
