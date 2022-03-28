from flask import Flask, request, render_template
import os
import sys

current_path = os.path.dirname(os.path.realpath(__file__))
main_path = os.path.dirname(current_path)
sys.path.insert(0, main_path)

from main import Nsnet2
from main.utils.convert_to_spectogram import rgb_spectrogram_image


app = Flask(__name__)
model = Nsnet2()

@app.route('/', methods=['POST', 'GET'])
def home():
       
    return render_template('home.html')

@app.route('/process', methods=['POST'])
def index():

    path = os.path.join(current_path, 'static/fromServer.wav') 
    noisy_spectrogram_path = os.path.join(os.path.dirname(path), 'spectrograms/noisy.png') 
    cleaned_audio_dir = os.path.join(os.path.dirname(path), 'results/') 
    clean_spectrogram_path = os.path.join(os.path.dirname(path), 'spectrograms/clean.png') 

    request.files['audio_data'].save(path)    

    rgb_spectrogram_image(path, noisy_spectrogram_path)
    model.denoise_single_file(path, cleaned_audio_dir)

    rgb_spectrogram_image(os.path.join(cleaned_audio_dir, 'fromServer.wav'), clean_spectrogram_path)

    return 'success'
        
    


if __name__ == "__main__":
    app.run(debug=True)