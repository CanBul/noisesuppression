from flask import Flask, request, render_template
import os
import sys

current_path = os.path.dirname(os.path.realpath(__file__))
main_path = os.path.dirname(current_path)
sys.path.insert(0, main_path)

from main.nsnet2 import Nsnet2
from main.utils.convert_wav_to_spectogram import convert_wav_to_spectrogram


app = Flask(__name__)
model = Nsnet2()

@app.route('/', methods=['POST', 'GET'])
def home():       
    return render_template('home.html')


@app.route('/process', methods=['POST'])
def transform():
    #Necessary paths
    static_files_path = os.path.join(current_path, 'static')

    noisy_audio_path = os.path.join(static_files_path, 'noisy_data/fromServer.wav') 
    noisy_spectrogram_path = os.path.join(static_files_path, 'spectrograms/noisy.png')     
    clean_spectrogram_path = os.path.join(static_files_path, 'spectrograms/clean.png') 
    
    #Directory path
    cleaned_audio_dir = os.path.join(static_files_path, 'results/') 
    
    request.files['audio_data'].save(noisy_audio_path)  

    #Transformations  
    convert_wav_to_spectrogram(noisy_audio_path, noisy_spectrogram_path)
    model.denoise_single_file(noisy_audio_path, cleaned_audio_dir)
    convert_wav_to_spectrogram(os.path.join(cleaned_audio_dir, 'fromServer.wav'), clean_spectrogram_path)

    return 'success'
        
    


if __name__ == "__main__":
    app.run(debug=True)