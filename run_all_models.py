from main.fullsubnet import   FullSubnet
from main.nsnet2 import Nsnet2
from main.rnnoise import RNNoise
import os

def run_all_models():
    """
    Loops over all files under noisy data directory and uses specified models to denoise them.

    Each model outputs its result to its directory under noisesuppression/results
    """
    
    main_path = os.path.dirname(os.path.realpath(__file__))
    NOISY_DATA_DIR = os.path.join(main_path, "data/noisy_data")
    MODELS = [Nsnet2, FullSubnet]
      
    for model in MODELS:
        denoiser = model()
        current_model_name = str(denoiser)
        output_directory = os.path.join(main_path, "results", f"{current_model_name}_results")

        for file in os.listdir(NOISY_DATA_DIR):

            current_file_full_path = os.path.join(NOISY_DATA_DIR, file)
            denoiser.denoise_single_file(current_file_full_path, output_directory)


if __name__ == "__main__":
    run_all_models()

