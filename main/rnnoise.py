import ctypes
import numpy as np
import soundfile as sf
import os
import librosa
import sys
current_path = os.path.dirname(os.path.realpath(__file__))
main_path = os.path.dirname(current_path)
sys.path.insert(0, main_path)

from main.utils.frame_generator import frame_generator
from main.utils.read_wave import read_wave


class RNNoise:
    """
        A class that uses RNNoise as the model to denoise wav files.
    """
    def __init__(self):
        """
        Initializes RNNoise library which was written in C for processing frames.
        """

        lib_path = ctypes.util.find_library(("rnnoise"))
        if (not("/" in lib_path)):
            lib_path = (os.popen('ldconfig -p | grep '+lib_path).read().split('\n')[0].strip().split(" ")[-1] or ("/usr/local/lib/"+lib_path))
        
        self.lib = ctypes.cdll.LoadLibrary(lib_path)
        self.lib.rnnoise_process_frame.argtypes = [ctypes.c_void_p,ctypes.POINTER(ctypes.c_float),ctypes.POINTER(ctypes.c_float)]
        self.lib.rnnoise_process_frame.restype = ctypes.c_float
        self.lib.rnnoise_create.restype = ctypes.c_void_p
        self.lib.rnnoise_destroy.argtypes = [ctypes.c_void_p]

        self.obj = self.lib.rnnoise_create(None)

    def _process_frame(self,inbuf):
        """
        Denoises and returns the given frame       
        """

        outbuf = np.ndarray((480,), 'h', inbuf).astype(ctypes.c_float)
        outbuf_ptr = outbuf.ctypes.data_as(ctypes.POINTER(ctypes.c_float))
        self.lib.rnnoise_process_frame(self.obj, outbuf_ptr, outbuf_ptr)
        
        return outbuf.astype(ctypes.c_short).tobytes()
    
    def denoise_single_file(self, source_file_path, output_directory):

        """
        Main method to denoise the wav file. 

        Args:
            source_file_path (str): absolute path of noisy wav file
            output_directory (str): output directory of denoised file

        Output file name will be same as the input file name.

        """

        last_index_of_slash = source_file_path.rfind('/')
        name_of_the_file = source_file_path[last_index_of_slash+1:]

        output_path = os.path.join(output_directory, f'{name_of_the_file}')
        

        target_sr = 48000
        temp_file = './test.wav'

        sound, _ = librosa.load(path=source_file_path, sr=target_sr)
        sf.write(file=temp_file, data=sound, samplerate=target_sr)
        # Need to read the file in this format. Converting librosa directly was difficult.
        sound, _ = read_wave(temp_file)     
        

        frames = list(frame_generator(10, sound, target_sr))        
        denoised_frames = [self._process_frame(frame) for frame in frames]       

        denoised_wav = np.concatenate([np.frombuffer(frame,
                                                    dtype=np.int16)
                                    for frame in denoised_frames])
        

        os.remove(temp_file)
        sf.write(output_path, denoised_wav, target_sr)
    
    def __repr__(self):
        return 'rnnoise'







