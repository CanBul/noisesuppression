from pesq import pesq
import librosa


def calculate_pesq(clean_audio_path, enhanced_audio_path, band='wb'):
    """
    Calculates PESQ score of clean and enhanced audios, prints and returns it. 

    Args:
        clean_audio_path (str): Clean audio path
        enhanced_audio_path (str): Enhanced audio path
        band (str, optional): wideband or narrowband. Defaults to 'wb'.

    Returns:
        str: PESQ score
    """

    reference_signal, sample_rate = librosa.load(clean_audio_path, sr=16000)
    degraded_signal, sample_rate = librosa.load(enhanced_audio_path, sr=16000)

    score = pesq(sample_rate, reference_signal, degraded_signal, band)
    print(f'PESQ score is {score}')
    return score


