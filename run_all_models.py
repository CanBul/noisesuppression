from main import  Nsnet2, RNNoise, FullSubnet
import os

def run_all_models():

    models = [Nsnet2, RNNoise, FullSubnet]
    main_path = os.path.dirname(os.path.realpath(__file__))
    NOISY_DATA_DIR = os.path.join(main_path, "data/noisy_data")
      
    for model in models:
        denoiser = model()
        current_model_name = str(denoiser)
        output_directory = os.path.join(main_path, "results", f"{current_model_name}_results")

        for file in os.listdir(NOISY_DATA_DIR):

            current_file_full_path = os.path.join(NOISY_DATA_DIR, file)
            denoiser.denoise_single_file(current_file_full_path, output_directory)


if __name__ == "__main__":
    run_all_models()

