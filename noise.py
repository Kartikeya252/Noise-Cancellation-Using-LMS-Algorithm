import numpy as np
import wave
import struct
import random

# Set the sample rate and number of samples
sample_rate = 44100
num_samples = sample_rate * 5

# Generate the white noise signal
noise = [random.uniform(-1, 1) for i in range(num_samples)]

# Save the noise signal as a wave file
with wave.open("noise.wav", 'w') as file:
    # Set the parameters for the wave file
    file.setnchannels(1)
    file.setsampwidth(2)
    file.setframerate(sample_rate)

    # Write the samples to the wave file
    for sample in noise:
        file.writeframes(struct.pack('h', int(sample * (2 ** 15 - 1))))
