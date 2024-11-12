import os
import numpy as np
import matplotlib.pyplot as plt
from data_preprocessing import load_images

# Load content and style images
content_images = load_images("../data/content")
style_images = load_images("../data/style")

# Understanding the Data: Size and Shape
print(f"Number of Content Images: {len(content_images)}")
print(f"Number of Style Images: {len(style_images)}")
print(f"Shape of Content Images: {content_images[0].shape}")
print(f"Shape of Style Images: {style_images[0].shape}")

# Visualize a few content images
plt.figure(figsize=(10, 5))
for i in range(5):
    plt.subplot(1, 5, i + 1)
    plt.imshow(content_images[i])
    plt.axis('off')
plt.suptitle("Sample Content Images")
plt.show()

# Visualize a few style images
plt.figure(figsize=(10, 5))
for i in range(5):
    plt.subplot(1, 5, i + 1)
    plt.imshow(style_images[i])
    plt.axis('off')
plt.suptitle("Sample Style Images")
plt.show()
