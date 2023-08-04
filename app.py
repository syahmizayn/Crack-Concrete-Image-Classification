
import streamlit as st
import numpy as np
import cv2
import tensorflow as tf
from tensorflow.keras.models import load_model

# Load your trained model
model = load_model('crack_model.hdf5')

# Function to preprocess the image
def preprocess_image(image):
    resized_image = tf.image.resize(image, (256, 256))
    return resized_image.numpy().astype(int) / 255.0

# Function to make predictions
def make_prediction(image):
    preprocessed_image = preprocess_image(image)
    prediction = model.predict(np.expand_dims(preprocessed_image, 0))
    return prediction[0][0]

# Streamlit app
def main():
    st.title('Crack Concrete Image Classifier')
    st.write('Upload an image and the classifier will predict if it contains a crack or not.')

    # Upload image through Streamlit widget
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Read the image
        image = cv2.imdecode(np.fromstring(uploaded_file.read(), np.uint8), 1)
        
        # Display the uploaded image
        st.image(image, channels='BGR', caption='Uploaded Image', use_column_width=True)

        # Make prediction
        prediction = make_prediction(image)
        if prediction > 0.5:
            st.write('Predicted class is Crack')
        else:
            st.write('Predicted class is Not Crack')

if __name__ == '__main__':
    main()
