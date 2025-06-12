import os
import sys
from helpers import add_text_to_image, convert_jpg_to_pdf, send_email
from excel import fetch_data_from_xlsx
from filename import certificateName, xlsxName, user_email , sender_passkey

def sanitize_filename(name, email):
    # Handle None (null) values
    sanitized_name = "".join([c if c.isalnum() or c in (' ', '-', '_') else '_' for c in (name or '')])
    sanitized_email = "".join([c if c.isalnum() or c in ('-', '_', '@') else '_' for c in (email or '')])
    
    return f"./temp/{sanitized_name}_{sanitized_email}"


def main():
    if not os.path.exists('./temp'):
        os.makedirs('./temp')
file_path = xlsxName()  
data = fetch_data_from_xlsx(file_path)  

for i in data:  
    certificate_path = certificateName()  
    input_image_path = os.path.join('certificates', certificate_path)  
    temp_image_path = './temp/certificate.jpg'  
    temp_pdf_path = sanitize_filename(i[0],i[1])+'.pdf' 
    # temp_pdf_path = f"./temp/certificate.pdf"

    add_text_to_image(input_image_path, [i[0], i[1]], temp_image_path)  

    if not os.path.exists(temp_image_path):  
        print(f"File not found: {temp_image_path}")  
        continue  

    convert_jpg_to_pdf(temp_image_path, temp_pdf_path)  

    name = i[0]  
    email = i[1]  
    print(f"Sending to: {email}")  

    subject = "🎉 Congratulations! Your Participation Certificate is Ready 🎓"  

    body = f"""  
    <!DOCTYPE html>  
    <html lang="en">  
    <head>  
      <meta charset="UTF-8" />  
      <meta name="viewport" content="width=device-width, initial-scale=1.0"/>  
      <title>Participation Certificate - Envision25</title>  
      <style>  
        body {{  
          margin: 0;  
          padding: 0;  
          font-family: Arial, sans-serif;  
          background-color: white;  
          color: #161616;  
        }}  
        .container {{  
          width: 100%;  
          max-width: 600px;  
          margin: 0 auto;  
          padding: 20px;  
        }}  
        .card {{  
          background-color: #1e1e1e;  
          border-radius: 8px;  
          padding: 20px;  
          margin-bottom: 20px;  
        }}  
        .image-card img {{  
          width: 100%;  
          border-radius: 12px;  
        }}  
        .text-content h1 {{  
          text-align: center;  
          color: #ffffff;  
        }}  
        .text-content p {{  
          color: #ffffff;  
          font-size: 1.1em;  
          line-height: 1.6;  
        }}  
        .btn {{  
          display: inline-block;  
          margin-top: 10px;  
          padding: 10px 15px;  
          background-color: #00bcd4;  
          color: #fff;  
          text-decoration: none;  
          border-radius: 5px;  
        }}  
      </style>  
    </head>  
    <body>  
      <div class="container">  
        <div class="card">  
          <div class="image-card">  
            <img src="https://alumniweb.blob.core.windows.net/envision/_ENVISION%20EVENTS%20WEBSITE%20CARDS.png" alt="Event Image" />  
          </div>  
        </div>  
        <div class="card" style="background-color:rgb(0, 0, 0); padding: 20px; border-radius: 8px; color: white; font-family: Arial, sans-serif;">  
          <div class="text-content">  
            <h1 style="color: #00ffff; text-align: center;">  
              🎉 Participation Certificate  
            </h1>  
            <p style="font-size: 16px;">Thank you for participating in our event!</p>  
            <p style="font-size: 16px;">  
              🧾 Certificate awarded to: <strong style="color: #00ffff;">{name}</strong>  
            </p>  
            <p style="font-size: 16px;">  
        
               We are delighted to inform you that your certificate for participating in Envision25 is now available! 🌟 Please find the attached PDF certificate for your records.<br><br>
          Thank you for your participation and valuable contributions. We hope you had a wonderful experience and look forward to seeing you at future events! 
            </p>  
          
            <p style="font-size: 16px;">🤝 Best regards,<br />Envision25 Team</p>  
          </div>  
        </div>  
      </div>  
    </body>  
    </html>  
    """  

    sender = user_email()  
    passkey = sender_passkey()  

    try:  
        # send_email(sender, passkey, email, subject, body, temp_pdf_path)  
        print(f"✅ Certificate sent to {email}")  
    except Exception as e:  
        print(f"❌ Failed to send email to {email} : {str(e)}")  
        sys.exit(1)  
