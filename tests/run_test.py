import time
import os
import sys

current_path = os.path.dirname(os.path.realpath(__file__))
main_path = os.path.dirname(current_path)
sys.path.insert(0, main_path)

from metrics.pesq_calculator import calculate_pesq
from main.fullsubnet import FullSubnet
from main.rnnoise import RNNoise
from main.nsnet2 import Nsnet2


def run_one_model(denoiser, input_file_path, output_directory):
    """
    Runs a model to denoise the wav file given. Prints inference time.

    Args:
        denoiser (instance of a model): FullSubnet, RNNoise or Nsnet2
        source_file_path (str): absolute path of noisy wav file
        output_directory (str): output directory of denoised file
    """

    start = time.time()
    
    denoiser.denoise_single_file(input_file_path, output_directory)

    end = time.time()
    print(f'{denoiser} inference time is {end- start}')

    return


if __name__ == "__main__":

    #Arbitrary test files and paths
    
    file_name = "Speaker_M2_Noise_Subway_Station.wav"
    test_file_path = os.path.join(main_path, f'data/noisy_data/{file_name}')
    clean_file_path = os.path.join(main_path, 'data/clean_data/Speaker_M2_Original.wav')

    MODELS = [FullSubnet, RNNoise, Nsnet2]

    for model in MODELS:
    
        denoiser = model()

        current_model_name = str(denoiser)
        print(f'Testing {current_model_name}')
        print('-----------------')

        output_directory = os.path.join(main_path, "results", f"{current_model_name}_results")

        run_one_model(denoiser, test_file_path, output_directory ) 

        #Calculates PESQ score
        calculate_pesq(clean_file_path, os.path.join(output_directory, f"{file_name}")) 

        print('-----------------')



    
                        
            

            

            
            









