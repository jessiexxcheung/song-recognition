from audio_sampling import analog_to_digital, song_to_digital, turn_off_ticks
import numpy as np
import librosa
import matplotlib.pyplot as plt
from IPython.display import Audio
import spectrogram
import find_peaks
%matplotlib notebook
import matplotlib.mlab as mlab
from microphone import record_audio
