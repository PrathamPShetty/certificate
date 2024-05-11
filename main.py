import os
from helpers import add_text_to_image, convert_jpg_to_pdf, send_email
from excel import fetch_data_from_xlsx

if __name__ == "__main__":
    file_path = "certificate_issue.xlsx"  # Replace with the path to your XLSX file
    data = fetch_data_from_xlsx(file_path)
   
    
    for i in data:
        #  print(i[2])
        #  print(i[3])
        #  print(i[5])
        #  print(i[6])

        if i[3] == 'email':
            continue
        else:
            add_text_to_image(os.path.join('certificates', 'certificate.jpg'), [f"{i[2]}", f'{i[5]}', f'{i[6]}'], "certificate.jpg")
            convert_jpg_to_pdf('./temp/certificate.jpg', "./temp/Envision_Certificate.pdf")
            
            email = i[3]
            print(email)
            subject = f"🎉 Congratulations! Your {i[6]} Event Certificate is Ready 🎓"
            body = f"""Dear {i[2]},
            We are delighted to inform you that your certificate for participating in the {i[6]} event is now available! 🌟

📜 Certificate Details:
Event: {i[6]}
Participant Name: {i[2]}

Please find the attached PDF certificate for your records.

Thank you for your participation and valuable contributions to the {i[6]} event. We hope you had a wonderful experience and look forward to seeing you at future events!

Best regards,
Team Envision24
"""
            try:
                send_email('envision24team@gmail.com', "crinvcrptnghowiz", email, subject, body, './temp/Envision_Certificate.pdf')
                
            except Exception as e:
                print(f"Failed to send email to {email}: {str(e)}")