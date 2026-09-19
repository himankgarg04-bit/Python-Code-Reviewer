import subprocess
from google import genai
import os
import smtplib
from email.message import EmailMessage


def getDiff():
    diff =subprocess.check_output(["git", "show"], text=True)
    return diff


client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))


def send_email(html_content):
    msg = EmailMessage()
    msg['Subject'] = 'Code Review Feedback'
    msg['From'] = "himank.garg04@gmail.com"
    msg['To'] = "himank.garg04@gmail.com"
    msg.set_content("Please find the code review feedback below.")
    msg.set_content(html_content, subtype='html')

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login("himank.garg04@gmail.com", os.getenv("MAIL_APP_PASSWORD"))
        smtp.send_message(msg)

    return "Email sent successfully!"


def main():
    diff = getDiff()
    prompt = f"Please review the following code changes and provide feedback:\n\n Mandatory: provide the output in html that can use to send in mail\n\n{diff}"
    response = client.models.generate_content(
        model = "gemini-3.6-flash",
        contents = prompt
    )
    
    html = response.text
    send_email(html)
    

main()
