import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication


def sendEmailService(listEmail):
    # Set up SMTP server and login credentials
    smtp_server = "smtpdm-ap-southeast-1.aliyun.com"
    smtp_port = 80
    username = "profind@mail.confins.co"
    password = "AdIns202012345"

    # Set up email content
    sender_email = "profind@mail.confins.co"

    recipient_email = ", ".join(listEmail)
    subject = "Data OCR bulan ini"
    body = "Berikut data ocr bulan ini"

    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = recipient_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    # Attach a file (optional)
    with open("example1.xlsx", "rb") as f:
        attachment = MIMEApplication(f.read(), _subtype="xlsx")
        attachment.add_header(
            "Content-Disposition", "attachment", filename="example.xlsx"
        )
        msg.attach(attachment)

    # Send email
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(username, password)
        server.sendmail(sender_email, recipient_email, msg.as_string())
