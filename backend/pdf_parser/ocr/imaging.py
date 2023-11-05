import cv2 
import pytesseract
import numpy as np
import os
import json
import re
from tqdm import tqdm







filepath = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
path = "/images/textbook/"
filepath += path

print(filepath)


# custom_config = r'--oem 3 --psm 6'


# data = {}

# for filename in tqdm(os.listdir(filepath)):

#     image = cv2.imread(filepath + filename)
#     imageText = pytesseract.image_to_string(image, config=custom_config)
    
#     #remove all special characters and newlines from imagetext
    
#     splitName = filename.split("-")
#     sectionNumber = splitName[1]
#     fileNumber = splitName[2]
#     fileNumber = fileNumber.split(".")[0]
        
#     sectionHeader = "SECTION" + sectionNumber
#     fileHeader = "PAGE" + fileNumber
    
    
#     if sectionHeader not in data:
#         data[sectionHeader] = {}
#     if fileHeader not in data[sectionHeader]:
#         data[sectionHeader][fileHeader] = {}
#     data[sectionHeader][fileHeader] = imageText
    

#     #turn the data into a json file and sort and format it nicely
    
    
# sorted_data = {
#     section: {
#         f"PAGE{num}": data[section][f"PAGE{num}"]
#         for num in sorted(
#             (int(re.search(r'\d+', page).group()) for page in data[section]),
#             key=int
#         )
#     }
#     for section in data
# }

# jsondata = json.dumps(sorted_data, indent=4)


# with open('sorted_data.json', 'w') as f:
#     f.write(jsondata)
    

