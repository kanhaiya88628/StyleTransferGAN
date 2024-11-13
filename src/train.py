import numpy as np
import tensorflow as tf
from model import build_generator, build_discriminator
from data_preprocessing import load_images

# Load images
content_images = load_images("../data/content")
style_images = load_images("../data/style")

# Define input shape
input_shape = (128, 128, 3)

# Instantiate models
generator_AB = build_generator(input_shape)
discriminator_B = build_discriminator(input_shape)

# Compile models
loss_obj = tf.keras.losses.BinaryCrossentropy(from_logits=True)
generator_optimizer = tf.keras.optimizers.Adam(learning_rate=0.0002, beta_1=0.5)
discriminator_optimizer = tf.keras.optimizers.Adam(learning_rate=0.0002, beta_1=0.5)

# Training loop
epochs = 10  # You can increase this number for better results
for epoch in range(epochs):
    print(f"Epoch {epoch + 1}/{epochs}")
    np.random.shuffle(content_images)
    np.random.shuffle(style_images)

    for content_image, style_image in zip(content_images, style_images):
        content_image = np.expand_dims(content_image, axis=0)
        style_image = np.expand_dims(style_image, axis=0)

        # Training step
        with tf.GradientTape() as gen_tape, tf.GradientTape() as disc_tape:
            generated_image = generator_AB(content_image, training=True)
            real_output = discriminator_B(style_image, training=True)
            fake_output = discriminator_B(generated_image, training=True)
            gen_loss = loss_obj(tf.ones_like(fake_output), fake_output)
            disc_loss = (loss_obj(tf.ones_like(real_output), real_output) +
                         loss_obj(tf.zeros_like(fake_output), fake_output)) * 0.5

        # Apply gradients
        gradients_of_generator = gen_tape.gradient(gen_loss, generator_AB.trainable_variables)
        gradients_of_discriminator = disc_tape.gradient(disc_loss, discriminator_B.trainable_variables)
        generator_optimizer.apply_gradients(zip(gradients_of_generator, generator_AB.trainable_variables))
        discriminator_optimizer.apply_gradients(zip(gradients_of_discriminator, discriminator_B.trainable_variables))

    print(f"Generator Loss: {gen_loss.numpy()}, Discriminator Loss: {disc_loss.numpy()}")

# Save the model
generator_AB.save("../saved_models/generator_AB.h5")
print("Model saved successfully!")
