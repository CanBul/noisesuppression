import contextlib
import wave

def read_wave(path):
    """
    Reads a .wav file.
    Takes the path, and returns (PCM audio data, sample rate).
    """
    with contextlib.closing(wave.open(path, 'rb')) as wf:

        num_channels = wf.getnchannels()
        assert num_channels == 1

        sample_width = wf.getsampwidth()
        assert sample_width == 2

        sample_rate = wf.getframerate()
        assert sample_rate in (8000, 16000, 32000, 48000)
        
        pcm_data = wf.readframes(wf.getnframes())

        return pcm_data, sample_rate    