# Image_Colour_Palette_Generator
A website that finds the most common colours in an uploaded image.
To build a website that finds the most common colors in an uploaded image using Python, you can use the Flask web framework and the Pillow library for image processing. Here's a step-by-step guide to help you get started:

1. Set up the project:
   - Install Flask by running `pip install flask` in your command prompt or terminal.
   - Install Pillow by running `pip install pillow`.
   - Create a new directory for your project.
   - Inside the project directory, create a virtual environment by running `python -m venv venv`.
   - Activate the virtual environment:
     - On Windows: `venv\Scripts\activate`
     - On macOS/Linux: `source venv/bin/activate`
   - Create a new file called `app.py` in your project directory.

2. Import the required modules:
   - Open `app.py` and add the following import statements:

   ```python
   from flask import Flask, render_template, request
   from PIL import Image
   from collections import Counter
   import numpy as np
   import io
   import base64
   ```

3. Initialize the Flask application:
   - Add the following code to `app.py`:

   ```python
   app = Flask(__name__)
   ```

4. Create a route for the home page:
   - Add the following code to `app.py`:

   ```python
   @app.route('/')
   def index():
       return render_template('index.html')
   ```

5. Create a route to handle the image upload and find the most common colors:
   - Add the following code to `app.py`:

   ```python
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
   ```

6. Create the HTML templates:
   - Create a new directory called `templates` inside your project directory.
   - Inside the `templates` directory, create the following two files:
     - `index.html`:

       ```html
       <!DOCTYPE html>
       <html>
         <head>
           <title>Most Common Colors</title>
         </head>
         <body>
           <h1>Most Common Colors</h1>
           <form action="/upload" method="post" enctype="multipart/form-data">
             <input type="file" name="image">
             <button type="submit">Upload</button>
           </form>
         </body>
       </html>
       ```

     - `result.html`:

       ```html
       <!DOCTYPE html>
       <html>
         <head>
           <title>Most Common Colors - Results</title>
         </head>
         <body>
           <h1>Most Common Colors - Results