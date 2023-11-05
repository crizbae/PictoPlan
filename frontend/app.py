# app.py
import random
import re
import uuid
import shutil
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os
import json
import base64
print(os.getcwd())

app = Flask(__name__)

gradients = [
    'linear-gradient(to right, #0f2027, #203a43, #2c5364)',
    'linear-gradient(to right, #283048, #859398)',
    'linear-gradient(to right, #ddd6f3, #faaca8)',
    'linear-gradient(to right, #ff5f6d, #ffc371)',
    'linear-gradient(to right, #d9a7c7, #fffcdc)',
    'linear-gradient(to right, #bdc3c7, #2c3e50)',
    'linear-gradient(to right, #e8cbc0, #636fa4)',
    'linear-gradient(to right, #fbd3e9, #bb377d)',
    'linear-gradient(to right, #b993d6, #8ca6db)',
    'linear-gradient(to right, #ffafbd, #ffc3a0)',
    'linear-gradient(to right, #eecda3, #ef629f)',
    # Add more gradients as desired...
]

ur_gradient = 'linear-gradient(to right, #ffe259, #ffa751)'
gradients.append(ur_gradient)

weights = [1] * len(gradients)  # All gradients have equal weight
weights[-1] = 0.001  # The last gradient (the rare one) has a weight of 0.0001
session_uuid = uuid.uuid4()
section = 1
page = 1

def hex_to_rgba(hex, opacity):
    hex = hex.lstrip('#')
    r, g, b = tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))
    return f'rgba({r}, {g}, {b}, {opacity})'

def gradient_to_rgba(gradient, opacity):
    hex_colors = re.findall(r'#[a-zA-Z0-9]{6}', gradient)
    rgba_colors = [hex_to_rgba(color, opacity) for color in hex_colors]
    for hex_color, rgba_color in zip(hex_colors, rgba_colors):
        gradient = gradient.replace(hex_color, rgba_color)
    return gradient

@app.route('/json/<filename>')
def serve_json(filename):
    # Read the JSON file
    with open('json/' + filename + '.json') as json_file:
        data = json.load(json_file)

    # Pass the data to the template
    return render_template('index.html', data=data)

@app.route('/')
def home():
    gradient = random.choices(gradients, weights=weights, k=1)[0]
    flipped_gradient = gradient.replace('to right', 'to left')
    button_gradient = gradient_to_rgba(flipped_gradient, 1)  # Change opacity to desired value
    return render_template('upload.html',
                           gradient=gradient,
                           button_gradient=button_gradient,
                           page=page,
                           section=section)

@app.route('/upload', methods=['POST'])
def upload_file():
    global page
    if 'file' not in request.files:
        return 'No file part', 400
    file = request.files['file']
    filename = secure_filename(file.filename)
    # save file to 'uploads/image.png'
    temp_dir = 'temp'
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)
    filename = str(session_uuid).replace('-', '') + '-' + str(section) + '-' + str(page) + '.png'
    file.save(os.path.join(temp_dir, filename))
    page += 1
    return home()

@app.route('/next-section', methods=['POST'])
def next_section():
    global section
    global page
    section += 1
    page = 1
    return home()

@app.route('/finished', methods=['POST'])
def finished():
    # Send temp directory to backend
    # Delete temp directory
    global session_uuid
    global section
    global page
    session_uuid = uuid.uuid4()
    section = 1
    page = 1
    
    # Convert files to base64 in a dict with key as name of file
    files = {}
    for file in os.listdir('temp'):
        with open(os.path.join('temp', file), 'rb') as f:
            encoded = base64.b64encode(f.read())
            files[file] = encoded.decode('utf-8')
    # Send files to backend
    # Magic VooDoo
    
    if os.path.exists('temp'):
        shutil.rmtree('temp')
    return render_template('finished.html')

if __name__ == '__main__':
    app.run(debug=True)