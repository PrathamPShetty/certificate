import os
from helpers import add_text_to_image

if __name__ == "__main__":
    add_text_to_image(os.path.join('certificates','certificate.jpg'),[ "Envision",'Paper Presentation IT','Sahyadri College of Engineering and Management, Adyar'], "certificate.jpg")
    