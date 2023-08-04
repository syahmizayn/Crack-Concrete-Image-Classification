# Crack-Concrete-Image-Classification
This repository contains code for a deep learning project that classifies images of cracked concrete using TensorFlow and Streamlit.

![image](https://github.com/syahmizayn/Crack-Concrete-Image-Classification/assets/127170997/f6dd50fa-e186-42da-94b2-4c0d8913cd56)

**Data Source**

The dataset used for this project is sourced from two research papers:

"Performance Comparison of Pretrained Convolutional Neural Networks on Crack Detection in Buildings" by Ç.F. Özgenel and A. Gönenç Sorguç, presented at ISARC 2018 in Berlin.

"Road Crack Detection Using Deep Convolutional Neural Network" by Lei Zhang, Fan Yang, Yimin Daniel Zhang, and Y.J. Zhang, published in the 2016 IEEE International Conference on Image Processing (ICIP). [DOI: 10.1109/ICIP.2016.7533052]

**Data Preparation**
The dataset is downloaded from a public URL using the requests library and stored in a RAR file.
The downloaded RAR file is extracted, and any images with unsupported extensions are removed from the dataset.

**Model Training**
The data is split into training, validation, and test sets.
A CNN model is defined and trained using the training set. The model's performance is visualized using TensorBoard.
Model Evaluation
The trained model is evaluated on the test set using precision, recall, and accuracy metrics.

**Model Deployment**
The trained model is saved as a crack_model.hdf5 file.
The Streamlit app is set up to make real-time predictions on uploaded images.
The app allows users to upload images and get predictions on whether they contain cracks or not.

**Instructions for Use**
1. Install required dependencies in requirements.txt.
2. Run the data preparation, model training, and model evaluation code.
3. Save the trained model as crack_model.hdf5.
4. Deploy the Streamlit app using streamlit run app.py and npx localtunnel -p 8501.
5. Access the deployed app through the provided external URL.

Enjoy using the Crack Concrete Image Classification app to predict cracked concrete in images!
