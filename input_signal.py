import numpy as np
import soundfile as sf

# Sample rate (samples per second)
fs = 44100

# Time duration (seconds)
duration = 5

# Number of samples
samples = int(fs * duration)

# Generate sine wave with a frequency of 440Hz
t = np.arange(samples) / fs
sine_wave = 0.5 * np.sin(2 * np.pi * 440 * t)

# Generate white noise
noise = np.random.randn(samples)

# Combine the sine wave and the noise
input_signal = sine_wave + noise

# Write the input signal to an output .wav file
sf.write("input.wav", input_signal, fs)
