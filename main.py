#Import libraries to send emails.
import os
from email.message import EmailMessage
import ssl
import smtplib
from datetime import datetime

#Get the email you want to use, password, and receiver you want to send the email to. Masked by env file.
email_sender = os.environ.get("EMAIL")
email_password= os.environ.get("PASSWORD")
email_receiver = os.environ.get("RECEIVER")

#For example, if this is for monthly reporting, get the current month.
current_month = datetime.now().month

#Create a map for the month as python returns the month as a number.
month = {

1: "January",
2: "February",
3: "March",
4: "April",
5: "May",
6: "June",
7: "July",
8: "August",
9: "September",
10: "October",
11: "November",
12: "December"

}

#Define your subject and body for email you would like to send.
subject = f"Report for {month[current_month]}"
body = f"""
Hi Jane Doe,

Please find attached the monthly report for the month of {month[current_month]}.

Thank you,
Charlie Johnson
"""

#Instancing the email to prepare to send.
em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

#Secure the email in a SSL wrapper (Transport Layer Security (often known as “Secure Sockets Layer”) encryption)
context = ssl.create_default_context()

#Using 'Simple mail transfer protocol library. Using it for Gmail. Login and send the mail.
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
