from audio_sampling import analog_to_digital, song_to_digital, turn_off_ticks
import numpy as np
import librosa
import matplotlib.pyplot as plt
from IPython.display import Audio
%matplotlib notebook
import matplotlib.mlab as mlab
from microphone import record_audio

# our own files
import spectrogram
import find_peaks
import audio_sampling


log_spectro = create_logspectro(audio)
peak_list = local_peaks(log_spectro, .77, 20)

