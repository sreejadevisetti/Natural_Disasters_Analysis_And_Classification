# Natural Disasters Intensity Analysis And Classification

## Introduction

This project provides a system for analyzing and classifying the intensity of natural disasters. It uses a Convolutional Neural Network (CNN) for image classification. The system is able to classify images into four categories of natural disasters: Cyclone, Earthquake, Flood, and Wildfire.

## Getting Started

To use the system, you need to follow these steps:

1. Clone or download the project repository from GitHub.

2. Install the required dependencies by running `pip install flask opencv-python keras numpy`.

3. Ensure you have Python 3.x installed on your machine.

4. Place your dataset in the appropriate directories for training and testing. The dataset should be organized in separate folders for each class (Cyclone, Earthquake, Flood, and Wildfire). The folder structure should be as follows:

   ```
   project_folder/
   ├── app.py
   ├── disaster.h5
   ├── model-bw.json
   ├── templates/
   │   ├── home.html
   │   ├── intro.html
   │   ├── upload.html
   └── dataset/
       ├── train_set/
       │   ├── Cyclone/
       │   ├── Earthquake/
       │   ├── Flood/
       │   ├── Wildfire/
       ├── test_set/
       │   ├── Cyclone/
       │   ├── Earthquake/
       │   ├── Flood/
       │   ├── Wildfire/
   ```

5. Run the `app.py` file using the command `python app.py`. The Flask application will start running on your local server.

6. Open your web browser and navigate to `http://localhost:5000/` to access the web interface.

## Technical Architecture
<img width="462" alt="Screenshot 2023-08-01 182144" src="https://github.com/Sreeja799/Natural_Disasters_Intensity_Analysis_And_Classification/assets/73770166/29ff5d44-ee6f-469d-b551-3857cca507a8">

## Model Training

The model was trained using the `model.ipynb` Jupyter notebook, which utilizes the Keras library for building and training the CNN model. The dataset was augmented using ImageDataGenerator to enhance the training process and improve the model's accuracy.

## Web Interface

The web interface provides the following pages:

1. **Home**: The landing page for the web application.

2. **Intro**: An introduction to the system and its purpose.

3. **Upload**: This page allows users to upload an image for classification.

## Image Classification

To classify an image, go to the "Upload" page, click on the "Choose File" button, select an image of a natural disaster, and click on the "Predict" button. The system will then classify the image and display the predicted class (Cyclone, Earthquake, Flood, or Wildfire).

Please note that the model has been trained on specific types of natural disaster images. For accurate classification, use images that belong to one of these four classes.

## Note

The system utilizes a pre-trained model (`disaster.h5`) for classification. If you wish to retrain the model or use a different dataset, you can modify the `model.ipynb` notebook and follow the instructions mentioned there.

## Troubleshooting

In case of any issues or errors, make sure to check the following:

1. The file paths for the dataset in both the `model.ipynb` and `app.py` files are correct and point to the right directories.

2. The required libraries (Flask, OpenCV, Keras, and NumPy) are installed in your Python environment.

3. Images uploaded for classification are of the correct format (JPEG or PNG) and belong to one of the four natural disaster classes.

## Conclusion

The Natural Disasters Intensity Analysis And Classification system is a valuable tool for predicting the intensity of various natural disasters based on input images. It can be used for disaster management and emergency response purposes. Feel free to explore the system and provide feedback for improvements.

## Output Screenshots

