import requests
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from reportlab.pdfgen import canvas
import os
from PIL import Image, ImageDraw, ImageFont


def add_text_to_image(image_path, text, output_path, font_path='./font/Merriweather/Merriweather-VariableFont_opsz,wdth,wght.ttf'):
    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)

    # Draw first line of text
    font_path1='./font/DMSerifDisplay-Regular.ttf'
    font_size = 30
    font = ImageFont.truetype(font_path1, font_size)
    text_size = font.getbbox(text[0])
    x = 412 - ((text_size[2] - text_size[0]) / 2)
    y = 256
    draw.text((x, y), text[0], fill="brown", font=font)
    print(text[0])

    # text[1]= "SmartAgro: An AI-powered system that guides farmers in crop selection, fertilizer planning "

    print(len(text[1]))
    if len(text[1]) > 125:
        font_size = 10
    elif len(text[1]) > 113:
        font_size = 10
    elif len(text[1]) > 107:
        font_size = 10

    elif len(text[1]) > 100:
        font_size = 12

    elif len(text[1]) > 90:
        font_size = 13
    elif len(text[1]) > 60:
        font_size = 17
    elif len(text[1]) > 50:
        font_size = 20
    else:
        font_size = 23


    font = ImageFont.truetype(font_path, font_size)
    text_size = font.getbbox(text[1])
    x = 412 - ((text_size[2] - text_size[0]) / 2)
    y = 324
    draw.text((x, y), text[1], fill="blue", font=font)

 


   







    if image.mode == 'RGBA':
        image = image.convert('RGB')
    image.save(output_path)

   


def convert_jpg_to_pdf(jpg_file, pdf_file):
    img = Image.open(jpg_file)
    c = canvas.Canvas(pdf_file, pagesize=img.size)
    c.drawImage(jpg_file, 0, 0)
    c.save()
    img.close()
    os.remove(jpg_file)
    

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import os

# def send_email(sender_email, sender_password, receiver_email, subject, body, pdf_file):
#     # Check if the PDF file exists
#     if not os.path.isfile(pdf_file):
#         print(f"Error: The file '{pdf_file}' does not exist.")
#         return
    
#     # Create the email message
#     message = MIMEMultipart()
#     message["From"] = sender_email
#     message["To"] = receiver_email
#     message["Subject"] = subject
    
#     # Attach the body in HTML format
#     message.attach(MIMEText(body, "html"))
    
#     # Attach the PDF file
#     with open(pdf_file, "rb") as attachment:
#         part = MIMEApplication(attachment.read(), _subtype="pdf")
#         part.add_header("Content-Disposition", "attachment", filename="Certificate.pdf")
#         message.attach(part)

#     try:
#         # Send the email via Mailgun's SMTP server
#         with smtplib.SMTP("smtp.mailgun.org", 587) as server:
#             server.starttls()  # Secure the connection
#             server.login("postmaster@prathampshetty.me", 'pRATHAM@99SAI')  # Login using provided credentials
#             server.sendmail('postmaster@prathampshetty.me', receiver_email, message.as_string())
#             print(f"Email successfully sent to {receiver_email}")
#     except Exception as e:
#         print(f"Failed to send email to {receiver_email}: {str(e)}")

def send_email(sender_email, sender_password, receiver_email, subject, body, pdf_file):
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "html"))
    
    with open(pdf_file, "rb") as attachment:
        part = MIMEApplication(attachment.read(), _subtype="pdf")
        part.add_header(
            "Content-Disposition",
            f"attachment; filename=Certificate.pdf",
        )
        message.attach(part)

    text = message.as_string()

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_email, text)
            print(f"Email successfully sent to {receiver_email}")
    except Exception as e:
        print(f"Failed to send email to {receiver_email}: {str(e)}")
        

# def send_email(sender_email, sender_password, receiver_email, subject, body, pdf_file):
#     message = MIMEMultipart()
#     message["From"] = sender_email
#     message["To"] = receiver_email
#     message["Subject"] = subject
#     message.attach(MIMEText(body, " html"))
#     with open(pdf_file, "rb") as attachment:
#         part = MIMEApplication(attachment.read(), _subtype="pdf")
#     part.add_header(
#         "Content-Disposition",
#         f"attachment; filename=Certificate.pdf",
#     )
#     message.attach(part)
#     text = message.as_string()
#     with smtplib.SMTP("smtp.mailgun.org", 587) as server:
#         server.starttls()
#         server.login(sender_email, sender_password)
#         server.sendmail(sender_email, receiver_email, text)


# def send_email(sender_email, api_key, receiver_email, subject, body, pdf_file):
#     # Mailgun API endpoint
#     url = "https://app.mailgun.com/v3"

#     # Mailgun API parameters
#     params = {
#         "from": sender_email,
#         "to": receiver_email,
#         "subject": subject,
#         "text": body,
#     }

#     # Mailgun API files (attachment)
#     files = [
#         ("attachment", ("envision24_certificate.pdf", open(pdf_file, "rb").read()))
#     ]

#     # Mailgun API headers
#     headers = {
#         "Authorization": f"Basic {api_key}"
#     }

#     # Send the email using Mailgun API
#     response = requests.post(url, files=files, data=params, headers=headers)

#     # Check the response
#     if response.status_code == 200:
#         print("Email sent successfully!")
#     else:
#         print("Failed to send email. Status code:", response.status_code)
    