# app.py
import random
import re
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os

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


@app.route('/')
def home():
    gradient = random.choices(gradients, weights=weights, k=1)[0]
    flipped_gradient = gradient.replace('to right', 'to left')
    button_gradient = gradient_to_rgba(flipped_gradient, 1)  # Change opacity to desired value
    return render_template('upload.html', gradient=gradient, button_gradient=button_gradient)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part', 400
    file = request.files['file']
    filename = secure_filename(file.filename)
    file.save(os.path.join('uploads', filename))
    return 'File uploaded successfully'

if __name__ == '__main__':
    app.run(debug=True)