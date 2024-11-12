import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model
from PIL import Image
import cv2

# Load the trained generator model
model_path = '../saved_models/generator_AB.h5'
try:
    generator = load_model(model_path)
    st.success("Model loaded successfully!")
except Exception as e:
    st.error(f"Error loading model: {e}")
    st.stop()

# Function to preprocess the image
def preprocess_image(image):
    img = image.resize((128, 128))
    img_array = np.array(img) / 127.5 - 1.0  # Normalize to [-1, 1]
    return np.expand_dims(img_array, axis=0)

# Function to postprocess the generated image
def postprocess_image(image_array):
    image_array = (image_array + 1.0) * 127.5  # Denormalize to [0, 255]
    image_array = np.clip(image_array, 0, 255).astype(np.uint8)
    return Image.fromarray(image_array)

# Streamlit interface
st.title("Style Transfer Using GANs for Multiple Images")

# Allow multiple file uploads
uploaded_files = st.file_uploader("Upload content images", type=["jpg", "jpeg", "png"], accept_multiple_files=True)

if uploaded_files:
    for uploaded_file in uploaded_files:
        # Load and display the uploaded image
        content_image = Image.open(uploaded_file)
        st.image(content_image, caption=f"Uploaded Image: {uploaded_file.name}", use_column_width=True)

        # Preprocess the image
        content_image_preprocessed = preprocess_image(content_image)

        # Generate the stylized image
        with st.spinner(f"Generating stylized image for {uploaded_file.name}..."):
            generated_image = generator.predict(content_image_preprocessed)[0]
            stylized_image = postprocess_image(generated_image)

        # Display the stylized image
        st.image(stylized_image, caption=f"Stylized Image: {uploaded_file.name}", use_column_width=True)
        st.success(f"Style transfer complete for {uploaded_file.name}!")

        # Option to download the stylized image
        st.download_button(f"Download Stylized Image: {uploaded_file.name}", stylized_image.tobytes(), f"{uploaded_file.name}_stylized.jpg", "image/jpeg")
