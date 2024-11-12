# model.py
from tensorflow.keras.layers import Input, Conv2D, Conv2DTranspose, LeakyReLU
from tensorflow.keras.models import Model

# Define the generator
def build_generator(input_shape):
    inputs = Input(shape=input_shape)
    
    # Down-sampling
    x = Conv2D(64, kernel_size=4, strides=2, padding='same')(inputs)
    x = LeakyReLU(alpha=0.2)(x)
    x = Conv2D(128, kernel_size=4, strides=2, padding='same')(x)
    x = LeakyReLU(alpha=0.2)(x)
    
    # Bottleneck
    x = Conv2D(256, kernel_size=4, strides=2, padding='same')(x)
    x = LeakyReLU(alpha=0.2)(x)
    
    # Up-sampling
    x = Conv2DTranspose(128, kernel_size=4, strides=2, padding='same')(x)
    x = LeakyReLU(alpha=0.2)(x)
    x = Conv2DTranspose(64, kernel_size=4, strides=2, padding='same')(x)
    x = LeakyReLU(alpha=0.2)(x)
    
    outputs = Conv2DTranspose(3, kernel_size=4, strides=2, padding='same', activation='tanh')(x)
    
    return Model(inputs, outputs)

# Define the discriminator
def build_discriminator(input_shape):
    inputs = Input(shape=input_shape)
    x = Conv2D(64, kernel_size=4, strides=2, padding='same')(inputs)
    x = LeakyReLU(alpha=0.2)(x)
    x = Conv2D(128, kernel_size=4, strides=2, padding='same')(x)
    x = LeakyReLU(alpha=0.2)(x)
    x = Conv2D(256, kernel_size=4, strides=2, padding='same')(x)
    x = LeakyReLU(alpha=0.2)(x)
    outputs = Conv2D(1, kernel_size=4, padding='same', activation='sigmoid')(x)
    
    return Model(inputs, outputs)
