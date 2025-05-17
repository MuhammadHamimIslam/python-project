import os
from dotenv import load_dotenv
from email.message import EmailMessage 
import ssl
import smtplib
import re

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

email_subject = take_inp("Subject: ") # get the email's subject 
email_body = take_inp("Body: ") # take the email's body content 

# preparing email 
em = EmailMessage()
em["From"] = email_sender
em["To"] = email_receiver
em["Subject"] = email_subject
em.set_content(email_body)

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