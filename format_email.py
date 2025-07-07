import os
from dotenv import load_dotenv
from email.message import EmailMessage 
import ssl
import smtplib
import re
import secrets
from jinja2 import Environment, FileSystemLoader

load_dotenv() # load env to secure the email and app password 

# take valid input 
def take_inp(prompt):
    """
    Prompt until the user enters a valid input. Returns a string with leading/trailing whitespace removed.
    """
    while True:
            data = input(prompt).strip()
            if data: 
                return data
            else:
                print("Enter a valid input")

# securely load from .env file
email_sender = os.getenv("EMAIL_SENDER") # sender email address 
email_password = os.getenv("APP_PASSWORD") # email password 
while True: 
        email_receiver = take_inp("Enter reciver's email address: ") # receiver email address
        if re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email_receiver): break
        else: 
            print("Email isn't valid!")

verification_code = "".join(str(secrets.randbelow(10)) for _ in range(6))

env = Environment(loader=FileSystemLoader("data"))
template = env.get_template("template.html")
rendered_html = template.render(verification_code=verification_code)

# preparing email 
em = EmailMessage()
em["From"] = email_sender
em["To"] = email_receiver
em["Subject"] = "Otp verification for pyTest"
em.set_content(f"Your verification code for pyTest is {verification_code}")
em.add_alternative(rendered_html, subtype="html")

# setting email context 
context = ssl.create_default_context()

try:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context, timeout=15) as smtp: 
        # login to the sender Gmail account 
        smtp.login(email_sender, email_password)
        
        #smtp.sendmail(email_sender, email_receiver, em.as_string())
        
        # now send the email to the receiver as string 
        smtp.send_message(em)
except Exception as e:
    print("Can't send email!")
    print(e)
else:
    print("Email sent successfully!")