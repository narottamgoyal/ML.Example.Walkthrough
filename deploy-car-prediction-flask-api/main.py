from __future__ import division, print_function

import os
import numpy as np
from flask import Flask, request, render_template
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from werkzeug.utils import secure_filename

# Define a flask app
app = Flask(__name__)

# Model saved with Keras model.save()
MODEL_PATH = 'model_resnet50.h5 '

# Load your trained model
model = load_model(MODEL_PATH)


@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        try:
            # Get the file from post request
            f = request.files['file']

            # Save the file to ./uploads
            base_path = os.path.join(os.path.dirname(__file__), 'uploads')
            file_path = os.path.join(base_path, secure_filename(f.filename))

            if not os.path.exists(base_path):
                os.makedirs(base_path)

            f.save(file_path)

            img = image.load_img(file_path, target_size=(224, 224))

            image1 = image.img_to_array(img)

            image1 = image1 / 255.  # Add this line

            image1 = image1.reshape((1, image1.shape[0], image1.shape[1], image1.shape[2]))
            result = model.predict(image1)

            result = np.argmax(result, axis=1)
            if result == 0:
                result = "The Car IS Audi"
            elif result == 1:
                result = "The Car is Lamborghini"
            else:
                result = "The Car Is Mercedes"

            return result
        except Exception as e:
            print(e.__class__)
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)

    return None


if __name__ == '__main__':
    app.run()
