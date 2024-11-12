# data_preprocessing.py
import os
import cv2
import numpy as np

def load_images(data_path, img_size=(128, 128)):
    images = []
    for img_file in os.listdir(data_path):
        img_path = os.path.join(data_path, img_file)
        img = cv2.imread(img_path)
        if img is None:  # Check for any corrupted or missing images
            continue
        img = cv2.resize(img, img_size) / 255.0  # Normalize to [0, 1]
        images.append(img)
    return np.array(images)

# Example usage
content_images = load_images("../data/content")
style_images = load_images("../data/style")

# Check if images loaded properly
print(f"Loaded {len(content_images)} content images and {len(style_images)} style images.")
