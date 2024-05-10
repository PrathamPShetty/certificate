import os
from helpers import add_text_to_image, convert_jpg_to_pdf


if __name__ == "__main__":
    add_text_to_image(os.path.join('certificates', 'certificate.jpg'), ["Envision",  'Sahyadringfjhfg College of Engineering and Management, Adyar','Jo Jeeta Wohi Sikandar: Cube Showdown Circus'], "certificate.jpg")
    convert_jpg_to_pdf('./temp/certificate.jpg', "./temp/Envision_Certificate.pdf")

