"""This module writes a piece of text and the date to a file.
"""

__version__ = '1.0'
__author__ = 'Gijs Entius'

import os
from datetime import date
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 


def write_to_image(image_path, text, date_format="%d-%m-%Y"):
    """Function to write text to a file.
    """
    image_text = text + " " + str(date.today().strftime(date_format))
    img = Image.open(file_path)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("Roboto-Bold.ttf", 16)
    draw.text((0, 0), image_text, (0,0,0), font=font)

    path, filename = os.path.split(file_path)
    new_filename = str(filename.split(".")[0]) + \
        "_copy" + "." + str(filename.split(".")[1])
    output_path = os.path.join(path, new_filename)
    img.save(output_path)

if __name__ == "__main__":
    file_path = input("What is the file path: ")
    image_text = input("What text needs to be printed on the image: ")
    write_to_image(file_path, image_text)