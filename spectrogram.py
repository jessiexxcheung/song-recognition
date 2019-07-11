import numpy as np
%matplotlib notebook
import matplotlib.pyplot as plt


import matplotlib.mlab as mlab
from microphone import record_audio

def create_logspectro(audio):
    sampling_rate = 44100
    S, freqs, times = mlab.specgram(audio, NFFT=4096, Fs=sampling_rate,
                                    window=mlab.window_hanning,
                                    noverlap=int(4096 / 2))
    S[S<=1E-20] = 1E-20
    return np.log(S)