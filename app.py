from flask import Flask, render_template, request
from PIL import Image
from collections import Counter
import numpy as np
import io
import base64

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    # Get the uploaded image file
    image_file = request.files['image']

    # Load the image using Pillow
    image = Image.open(image_file)

    # Convert the image to RGB mode if it's in a different mode
    if image.mode != 'RGB':
        image = image.convert('RGB')

    # Resize the image for faster processing (optional)
    image.thumbnail((200, 200))

    # Convert the image to a NumPy array
    image_array = np.array(image)

    # Flatten the array to a 2D list of pixels
    pixels = image_array.reshape(-1, 3).tolist()

    # Count the occurrence of each color
    color_counts = Counter(tuple(pixel) for pixel in pixels)

    # Find the most common colors
    most_common_colors = color_counts.most_common(5)  # Change the number to get more or fewer colors

    return render_template('result.html', image_data=image_file.read(), most_common_colors=most_common_colors)
