NoiseSuppression is a bundle of three noise suppression algorithms, namely FullSubnet, RNNoise and Nsnet2.

To be able to use NoiseSuppression, a conda environment is needed to be created and activated. After cloning the repo,

```
cd noisesuppression
conda env create -f environment.yml
conda activate noisesuppression

```

If you want to use the UI
```
python run_api.py
```

should start a flask development server. You can select noisy wav files from your computer and denoise them using the default Nsnet2 model. 

All files under data/noisy_data are already denoised. You can find those files specific to each model under results directory. 

To denoise every file under data/noisy_data using fullsubnet and nsnet2 models:

```
python run_all_models.py
```

If you also want to use the RNNoise model, it needs to be cloned from its github page and compiled. For more info:

https://github.com/xiph/rnnoise



ISSUES:

There is an installment problem of PESQ library directly. Therefore, it is not included in environment.yml. It is only required if you run tests/run_test.py

To be able install pesq, you need c compiler and cython. After installing them, you can
```
pip install pesq
```


Papers of the models used can be found under docs directory.






