import librosa
import matplotlib.pyplot as plt
import numpy as np
import librosa.display


def convert_wav_to_spectrogram(input_file_path, output_file_path, window_size=1024, hop_length=512):
    """
        Converts a wav file to spectrogram and saves it.
    """

    sample, _ = librosa.load(input_file_path)     
    
    window = np.hanning(window_size)
    stft  = librosa.core.spectrum.stft(sample, n_fft=window_size, hop_length=hop_length, window=window)
    out = 2 * np.abs(stft) / np.sum(window)       

    fig = plt.Figure()
    
    ax = fig.add_subplot(111)
    p = librosa.display.specshow(librosa.amplitude_to_db(out, ref=np.max), ax=ax, y_axis='log', x_axis='time')
    fig.savefig(output_file_path)

    return
    
    

