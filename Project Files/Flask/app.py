from flask import Flask, render_template, request, jsonify
import cv2
import numpy as np
from keras.models import load_model
from werkzeug.utils import secure_filename
import os

app = Flask(__name__, template_folder="templates")

# Loading the model
model = load_model('disaster.h5')
print("Loaded model from disk")

@app.route('/', methods=['GET'])
def index():
    return render_template('home.html')

@app.route('/home', methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/intro', methods=['GET'])
def about():
    return render_template('intro.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    return render_template('upload.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return jsonify({'prediction': 'Error: No image provided'})

    image = request.files['image']
    if image.filename == '':
        return jsonify({'prediction': 'Error: Invalid image'})

    # Save the uploaded image to a temporary file
    temp_filename = secure_filename(image.filename)
    image.save(temp_filename)

    # Read the image using OpenCV
    image = cv2.imread(temp_filename)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = cv2.resize(image, (64, 64))
    x = np.expand_dims(image, axis=0)
    result = np.argmax(model.predict(x), axis=-1)
    index = ['Cyclone', 'Earthquake', 'Flood', 'Wildfire']
    prediction = index[result[0]]

    # Delete the temporary file
    os.remove(temp_filename)

    return jsonify({'prediction': prediction})

if __name__ == '__main__':
    app.run(debug=False, threaded=True)