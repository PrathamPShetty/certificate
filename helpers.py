import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from reportlab.pdfgen import canvas
import os
from PIL import Image, ImageDraw, ImageFont



def add_text_to_image(image_path, text, output_path, font_path=None):
  
    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)
    font_size = 85
    if font_path:
        font = ImageFont.truetype(font_path, font_size)
    else:
        font = ImageFont.load_default(font_size)
    text_size = font.getbbox(text[0])
    x,y=1564-((text_size[2]-text_size[0])/2),1259
    draw.text((x, y), text[0], fill="black", font=font)
    
    
    # Event name
    font = ImageFont.load_default(font_size)
    text_size = font.getbbox(text[1])
    x,y=402+(1135-((text_size[2]-text_size[0])/2)),1395
    draw.text((x, y), text[1], fill="black", font=font)
    print((text_size[2]-text_size[0])/2)
    print(len(text[2]))

    # College  name
    font_size = 40 if len(text[2]) > 53 else (50 if len(text[2]) > 35 else 80)
    font = ImageFont.load_default(font_size)
    text_size = font.getbbox(text[2])
    x,y=702+(649-((text_size[2]-text_size[0])/2)),1556
    draw.text((x, y), text[2], fill="black", font=font)
    image.save(output_path)
    
    print('completed')


def convert_jpg_to_pdf(jpg_file, pdf_file):
    img = Image.open(jpg_file)
    c = canvas.Canvas(pdf_file, pagesize=img.size)
    c.drawImage(jpg_file, 0, 0)
    c.save()
    img.close()
    os.remove(jpg_file)
    



def send_email(sender_email, sender_password, receiver_email, subject, body, pdf_file):
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))
    with open(pdf_file, "rb") as attachment:
        part = MIMEApplication(attachment.read(), _subtype="pdf")
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {pdf_file}",
    )
    message.attach(part)
    text = message.as_string()
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, text)