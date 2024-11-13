import os
import sys
from helpers import add_text_to_image, convert_jpg_to_pdf, send_email
from excel import fetch_data_from_xlsx

def main():
    # Ensure the temp directory exists
    if not os.path.exists('./temp'):
        os.makedirs('./temp')

    file_path = "quiz.xlsx"  # Replace with the path to your XLSX file
    data = fetch_data_from_xlsx(file_path)
    data1 = [[1, 2, 'Praneeth', 'praneeth574231@gmail.com', 'Recent Innovations in Computer Science']]
    for i in data1:
        if i[3] == 'email':
            continue

        # Paths for the image and PDF files
        input_image_path = 'certificates/certificate11.jpg'  # Your uploaded certificate template
        temp_image_path = './temp/certificate.jpg'
        temp_pdf_path = "./temp/certificate.pdf"

        add_text_to_image(input_image_path, [i[1], i[4]], temp_image_path)
        
        if not os.path.exists(temp_image_path):
            print(f"File not found: {temp_image_path}")
            continue
        
        convert_jpg_to_pdf(temp_image_path, temp_pdf_path)
        
        name = i[1]
        email = i[2]
        print(email)
        subject = "🎉  Congratulations! Your BGMI Event Certificate is Ready 🎓"
        body = f"""
        <html>
        <head>
            <style>
                table[name="blk_permission"], table[name="blk_footer"] {{display:none;}}
            </style>
        </head>
       <body>
    <div class="header">
        <img src="https://beebom.com/wp-content/uploads/2023/05/Untitled-design-4-5.jpg" alt="BGMI Event Image" style="width:100%; max-width:750px; height:auto;">
        <h1>BGMI Event<br>_______</h1>
    </div>
    <div class="content">
        <p>Dear {name},</p>
        <p>We are delighted to inform you that your certificate for participating in the BGMI event is now available! 🌟</p>
        <p>Please find the attached PDF certificate for your records.</p>
        <p>Thank you for your participation and valuable contributions to the BGMI event. We hope you had a wonderful experience and look forward to seeing you at future events!</p>
        <p>Best regards,<br>Team AIML</p>
    </div>
</body>
</html>
        """

        try:
            #  send_email('prathampshetty99sai@gmail.com', "dlwo fqoz vkvw mwyi", email, subject, body, temp_pdf_path)
            send_email('postmaster@sandbox63f8a7a2b2b04dd2a99cb2f15de32799.mailgun.org', "cf6320f7e2597edd9d72f5b974e221bd-91fbbdba-aa8e9bec", email, subject, body, temp_pdf_path)
        except Exception as e:
            print(f"Failed to send email to {email} : {str(e)}")
            sys.exit(1)

if __name__ == "__main__":
    main()
