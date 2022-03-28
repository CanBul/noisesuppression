
import os
from subprocess import call
import shutil


class FullSubnet:
    def __init__(self):
        current_path = os.path.dirname(os.path.realpath(__file__))
        subnet_path = "models/fullsubnet"

        self.inference_file_path = os.path.join(current_path, subnet_path, "recipes/dns_interspeech_2020/inference.py")
        self.settings_file_path = os.path.join(current_path, subnet_path, "recipes/dns_interspeech_2020/fullsubnet/inference.toml")
        self.model_file_path = os.path.join(current_path, subnet_path, "model/bestmodel.tar")
        
        self.tmp_output_dir = os.path.join(os.path.dirname(current_path), "data/fullsubnet_results")
    
    def denoise_single_file(self, source_file_path, output_directory):

        try:          
            
            os.makedirs(self.tmp_output_dir, exist_ok=True)
            shutil.copy(source_file_path, self.tmp_output_dir)  
            
            call(["python", self.inference_file_path, "-C", self.settings_file_path , "-M", self.model_file_path , "-O", output_directory, "-D", self.tmp_output_dir])
                
        finally:
            shutil.rmtree(self.tmp_output_dir)
    
    def __repr__(self):
        return 'fullsubnet'



    

