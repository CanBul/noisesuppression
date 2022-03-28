from pesq import pesq
import librosa


def calculate_pesq(clean_audio_path, enhanced_audio_path, band='wb'):

    reference_signal, sample_rate = librosa.load(clean_audio_path, sr=16000)
    degraded_signal, sample_rate = librosa.load(enhanced_audio_path, sr=16000)

    score = pesq(sample_rate, reference_signal, degraded_signal, band)
    print(f'PESQ score is {score}')
    return score


