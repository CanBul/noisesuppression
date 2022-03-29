NoiseSuppression is a bundle of three noise suppression algorithms, namely FullSubnet, RNNoise and Nsnet2.

To be able to use NoiseSuppression, a conda environment is needed to be created and activated.

```
conda env create -f environment.yml
conda activate noisesuppression

```

If you want to use the UI, after
```
cd noisesuppression
python run_api.py
```

a flask development server should start. You can select noisy wav files from your computer and denoise them using the default Nsnet2 model. 

To denoise everyfile under data/noisy_data using fullsubnet and nsnet2 models:

```
python run_all_models.py
```

If you also want to use the RNNoise model, it needs to be cloned from its github page and compiled. For more info:

https://github.com/xiph/rnnoise












