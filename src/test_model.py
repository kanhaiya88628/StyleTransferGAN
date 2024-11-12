import numpy as np
from tensorflow.keras.models import load_model
from PIL import Image
import matplotlib.pyplot as plt

# Load the trained generator model
model_path = '../saved_models/generator_AB.h5'
try:
    generator = load_model(model_path)
    print("Model loaded successfully!")
except Exception as e:
    print(f"Error loading model: {e}")
    exit()

# Load and preprocess a sample content image
def preprocess_image(image_path, target_size=(128, 128)):
    img = Image.open(image_path).resize(target_size)
    img_array = np.array(img) / 127.5 - 1.0  # Normalize to [-1, 1]
    return np.expand_dims(img_array, axis=0)

# Postprocess the generated image
def postprocess_image(image_array):
    image_array = (image_array + 1.0) * 127.5  # Denormalize to [0, 255]
    return np.clip(image_array, 0, 255).astype(np.uint8)

# Test with a sample content image
sample_image_path = '../data/content/content_image_0.jpg'  # Change to a valid image path
content_image = preprocess_image(sample_image_path)

# Generate a stylized image
generated_image = generator.predict(content_image)[0]
generated_image = postprocess_image(generated_image)

# Save the generated image
generated_img = Image.fromarray(generated_image)
generated_img.save("../output/stylized_image.jpg")
print("Stylized image saved to ../output/stylized_image.jpg")


# Display the original and stylized images
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(Image.open(sample_image_path))
plt.title("Original Content Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(Image.fromarray(generated_image))
plt.title("Stylized Image")
plt.axis("off")

plt.show()

