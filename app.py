from flask import Flask, render_template, request
from PIL import Image
import numpy as np

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the uploaded file from the form
        file = request.files['file']
        
        # Process the file and find the most common colors
        # ...
        
        # Return the result as a template variable
        return render_template('result.html', colors=colors)
    
    # Render the file upload form
    return render_template('index.html')

def find_colors(file):
    # Open the uploaded image
    img = Image.open(file)

    # Resize the image to reduce processing time
    img = img.resize((100, 100))

    # Convert the image to a NumPy array
    arr = np.array(img)

    # Flatten the array and find the unique colors
    colors, counts = np.unique(arr.reshape(-1, 3), axis=0, return_counts=True)

    # Sort the colors by frequency in descending order
    sorted_indices = np.argsort(-counts)
    colors = colors[sorted_indices]

    # Convert the colors from NumPy array to hex strings
    hex_colors = ['#%02x%02x%02x' % tuple(color) for color in colors]

    # Return the most common colors
    return hex_colors[:10]