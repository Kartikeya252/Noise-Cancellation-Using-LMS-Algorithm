import numpy as np
import soundfile as sf

def generate_sine_tone(frequency, duration, sample_rate):
    # Calculate the number of samples
    samples = int(duration * sample_rate)

    # Generate the time array
    t = np.linspace(0, duration, samples, False)

    # Generate the sine wave
    sine_wave = 0.5 * np.sin(2 * np.pi * frequency * t)

    return sine_wave, sample_rate

def main():
    # Set the frequency, duration, and sample rate of the sine tone
    frequency = 440 # Hz
    duration = 5 # seconds
    sample_rate = 44100 # Hz

    # Generate the sine tone
    sine_wave, sample_rate = generate_sine_tone(frequency, duration, sample_rate)

    # Write the sine wave to a wave file
    sf.write("sin.wav", sine_wave, sample_rate)

if __name__ == '__main__':
    main()
