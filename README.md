To build a website that finds the most common colors in an uploaded image using Python, you can utilize a web framework like Flask and the Python Imaging Library (PIL) to process the uploaded image. Here's a step-by-step guide:

1. Set up the project:
   - Install Flask and PIL by running `pip install flask pillow` in your command prompt or terminal.
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
   import numpy as np
   from collections import Counter
   ```

3. Initialize the Flask application:
   - Add the following code to `app.py`:

   ```python
   app = Flask(__name__)
   ```

4. Create a route for uploading the image and finding the most common colors:
   - Add the following code to `app.py`:

   ```python
   @app.route('/', methods=['GET', 'POST'])
   def upload_image():
       if request.method == 'POST':
           # Get the uploaded image file
           image = request.files['image']
           
           # Read the image using PIL
           img = Image.open(image)
           
           # Convert the image to RGB mode
           img = img.convert('RGB')
           
           # Resize the image if needed
           img = img.resize((200, 200))  # Adjust the size as per your requirement
           
           # Convert the image to a NumPy array
           img_array = np.array(img)
           
           # Flatten the image array
           pixels = img_array.reshape(-1, 3)
           
           # Get the most common colors
           color_counts = Counter(map(tuple, pixels))
           most_common_colors = color_counts.most_common(5)  # Get the top 5 most common colors
           
           return render_template('result.html', image=image, colors=most_common_colors)
       
       return render_template('index.html')
   ```

5. Create HTML templates:
   - Create a new directory called `templates` inside your project directory.
   - Inside the `templates` directory, create two new files: `index.html` and `result.html`.
   - Add the following code to `index.html`:

   ```html
   <!DOCTYPE html>
   <html>
     <head>
       <title>Color Analyzer</title>
     </head>
     <body>
       <h1>Color Analyzer</h1>
       <form action="/" method="post" enctype="multipart/form-data">
         <input type="file" name="image" accept="image/*" required>
         <button type="submit">Analyze</button>
       </form>
     </body>
   </html>
   ```

   - Add the following code to `result.html`:

   ```html
   <!DOCTYPE html>
   <html>
     <head>
       <title>Color Analysis Result</title>
     </head>
     <body>
       <h1>Color Analysis Result</h1>
       <h2>Uploaded Image:</h2>
       <img src="{{ url_for('static', filename=image.filename) }}" alt="Uploaded Image">
       <h2>Most Common Colors:</h2>
       <ul>
         {%

 for color, count in colors %}
           <li style="background-color: rgb{{ color }};">RGB {{ color }} - Count: {{ count }}</li>
         {% endfor %}
       </ul>
     </body>
   </html>
   ```

6. Create a static directory:
   - Create a new directory called `static` inside your project directory.
   - Place a sample image named `sample.jpg` in the `static` directory (or upload your own image).

7. Run the application:
   - In your command prompt or terminal, navigate to your project directory.
   - Run `flask run` to start the Flask development server.
   - Open your web browser and visit `http://localhost:5000` to access the color analyzer website.

When you upload an image using the form, the script will read and process the image using PIL. It will resize the image, convert it to a NumPy array, and flatten the array. Then, it will count the occurrences of each color and return the top 5 most common colors. The result will be displayed on the `result.html` page.

Note: Make sure the uploaded image is in a format supported by PIL (e.g., JPEG, PNG, etc.).