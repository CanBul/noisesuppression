import os
from subprocess import call


class Nsnet2:
    def __init__(self):
        current_path = os.path.dirname(os.path.realpath(__file__))
        nsnet2_path = "models/nsnet2"

        self.inference_file_path = os.path.join(current_path, nsnet2_path, "run_nsnet2.py") 
        self.model_file_path = os.path.join(current_path, nsnet2_path, "nsnet2-20ms-48k-baseline.onnx")    
        
        
    def denoise_single_file(self, source_file_path, output_directory):    

        call(["python", self.inference_file_path, "-i", source_file_path, "-o", output_directory, "-m", self.model_file_path])
    
    def __repr__(self):
        return 'nsnet2'
        

