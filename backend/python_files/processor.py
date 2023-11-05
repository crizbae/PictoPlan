import base64
from io import BytesIO
import json
import cv2
import numpy as np
from imaging import imaging
from gpt_caller import gpt_caller

import os
import glob
def get_images_from_path(path):
    # Get all .png, .jpg, .jpeg files
    image_files = glob.glob(os.path.join(path, "*.[pjJ][npP][gG]*"))
    return image_files

def processor(base64Input):
    # Convert Base64 to image
    images = {}
    for name, data in base64Input.items():
        img_data = base64.b64decode(data)
        img_arr = np.frombuffer(img_data, np.uint8)
        images[name] = cv2.imdecode(img_arr, cv2.IMREAD_COLOR)
    # Run OCR on image
    ocr_out = imaging(images)
    lessons = gpt_caller(ocr_out)
    
    return lessons
