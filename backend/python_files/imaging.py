import cv2 
import pytesseract
import numpy as np
import os
import re
from tqdm import tqdm

filepath = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
path = "/images/textbook/"
filepath += path

# print(filepath)


def imaging(images):
    custom_config = r'--oem 3 --psm 6'

    data = {}

    for filename, image in images.items():
        imageText = pytesseract.image_to_string(image, config=custom_config)
        
        
        splitName = filename.split("-")
        sectionNumber = splitName[1]
        fileNumber = splitName[2]
        fileNumber = fileNumber.split(".")[0]
            
        sectionHeader = "SECTION" + sectionNumber
        fileHeader = "PAGE" + fileNumber
        
        
        if sectionHeader not in data:
            data[sectionHeader] = {}
        if fileHeader not in data[sectionHeader]:
            data[sectionHeader][fileHeader] = {}
        data[sectionHeader][fileHeader] = imageText
        
    sorted_data = {
        section: {
            f"PAGE{num}": data[section][f"PAGE{num}"]
            for num in sorted(
                (int(re.search(r'\d+', page).group()) for page in data[section]),
                key=int
            )
        }
        for section in data
    }
    
    return sorted_data