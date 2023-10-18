import numpy as np
import wave
import struct

def lms_noise_cancellation(input_file, noise_file):
    with wave.open(input_file, 'rb') as input_wave:
        n_samples = input_wave.getnframes()
        sample_rate = input_wave.getframerate()
        input_data = input_wave.readframes(n_samples)
        x = np.array(struct.unpack("%dh" % n_samples, input_data))

    with wave.open(noise_file, 'rb') as noise_wave:
        n_samples = noise_wave.getnframes()
        noise_data = noise_wave.readframes(n_samples)
        d = np.array(struct.unpack("%dh" % n_samples, noise_data))

    filter_order = 63
    weights = np.zeros(filter_order)
    step_size = 0.1
    output = np.zeros(n_samples)

    for i in range(filter_order, n_samples):
        x_i = x[i-filter_order:i][::-1]
        d_i = d[i]
        y = np.dot(weights, x_i)
        e = d_i - y
        weights += step_size * e * x_i
        output[i] = y

    output_wave = wave.open('output.wav', 'wb')
    output_wave.setparams((1, 2, sample_rate, n_samples, 'NONE', 'not compressed'))
    output = np.array(output).astype(np.int16)
    output_wave.writeframes(struct.pack("%dh" % n_samples, *output))
    output_wave.close()

if __name__ == '__main__':
    lms_noise_cancellation('input.wav', 'noise.wav')
