import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
import os

load_dotenv()


def send_email_with_attachment(attachment_path):
    sender = os.getenv("SMTP_EMAIL")
    password = os.getenv("SMTP_PASSWORD")
    receiver = "hr@ignitershub.com"

    if not sender or not password:
        print("SMTP credentials not found in environment variables")
        return

    msg = EmailMessage()
    msg["From"] = sender
    msg["To"] = receiver
    msg["Subject"] = "Challenge 3 completed"
 
    msg.set_content(
        "Name: Pushkar Raj\n"
        "Semester: 8th\n"
        "Branch: Computer Science\n"
        "Roll Number: 22CSEC21\n"
    )

   
    with open(attachment_path, "rb") as f:
        msg.add_attachment(
            f.read(),
            maintype="application",
            subtype="octet-stream",
            filename=os.path.basename(attachment_path)
        )

    
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender, password)
        server.send_message(msg)

    print(" Email sent successfully with attachment")




if __name__ == "__main__":
   
    send_email_with_attachment("abc.png")  