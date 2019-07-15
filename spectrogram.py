import numpy as np
import matplotlib.mlab as mlab


def create_spec(audio):
    sampling_rate = 44100
    S, freqs, times = mlab.specgram(audio, NFFT=4096, Fs=sampling_rate,
                                            window=mlab.window_hanning,
                                            noverlap=4096 // 2)
    S[S <= 1e-20] = 1e-20
    return np.log(S)


