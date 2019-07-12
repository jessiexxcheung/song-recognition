from audio_sampling import analog_to_digital, song_to_digital, turn_off_ticks
import numpy as np
import librosa
import matplotlib.pyplot as plt
from IPython.display import Audio
import pickle

sampling_rate = 44100
bit_depth = 64
dict = {}

from pathlib import Path

song_root = Path(r"C:\Users\darsh\Downloads\song-recognition\songs")

Feel = song_root / r"Feel It Still_Portugal The Man.mp3"
samples, fs = librosa.load(Feel, sr=44100, mono=True, duration=156)
samp = np.array(samples)
samp *= (2**15)
samples = list(samp)
dict[0] = samples

Glow = song_root / r"Glow_Justice Skolnik.mp3"
samples, fs = librosa.load(Glow, sr=44100, mono=True, duration=156)
samp = np.array(samples)
samp *= (2**15)
samples = list(samp)
dict[1] = samples

Halo = song_root / r"Halo_Beyonce.mp3"
samples, fs = librosa.load(Halo, sr=44100, mono=True, duration=156)
samp = np.array(samples)
samp *= (2**15)
samples = list(samp)
dict[2] = samples

If = song_root / r"If I Can't Have You_Shawn Mendes.mp3"
samples, fs = librosa.load(If, sr=44100, mono=True, duration=156)
samp = np.array(samples)
samp *= (2**15)
samples = list(samp)
dict[3] = samples

Joy = song_root / r"Joy_For King and Country.mp3"
samples, fs = librosa.load(Joy, sr=44100, mono=True, duration=156)
samp = np.array(samples)
samp *= (2**15)
samples = list(samp)
dict[4] = samples

Kill = song_root / r"Kill This Love_Blackpink.mp3"
samples, fs = librosa.load(Kill, sr=44100, mono=True, duration=156)
samp = np.array(samples)
samp *= (2**15)
samples = list(samp)
dict[5] = samples

Lights = song_root / r"Lights Down Low_MAX.mp3"
samples, fs = librosa.load(Lights, sr=44100, mono=True, duration=156)
samp = np.array(samples)
samp *= (2**15)
samples = list(samp)
dict[6] = samples

One = song_root / r"One Last Time_Ariana Grande.mp3"
samples, fs = librosa.load(One, sr=44100, mono=True, duration=156)
samp = np.array(samples)
samp *= (2**15)
samples = list(samp)
dict[7] = samples

Paris = song_root / r"Paris in the Rain_Lauv.mp3"
samples, fs = librosa.load(Paris, sr=44100, mono=True, duration=156)
samp = np.array(samples)
samp *= (2**15)
samples = list(samp)
dict[8] = samples

Perfect = song_root / r"Perfect_Ed Sheeran.mp3"
samples, fs = librosa.load(Perfect, sr=44100, mono=True, duration=156)
samp = np.array(samples)
samp *= (2**15)
samples = list(samp)
dict[9] = samples

Speechless = song_root / r"Speechless_Dan & Shay.mp3"
samples, fs = librosa.load(Speechless, sr=44100, mono=True, duration=156)
samp = np.array(samples)
samp *= (2**15)
samples = list(samp)
dict[10] = samples

Thank = song_root / r"Thank You Next_ Ariana Grande.mp3"
samples, fs = librosa.load(Thank, sr=44100, mono=True, duration=156)
samp = np.array(samples)
samp *= (2**15)
samples = list(samp)
dict[11] = samples

Stitches = song_root / r"Stitches_Shawn Mendes.mp3"
samples, fs = librosa.load(Stitches, sr=44100, mono=True, duration=156)
samp = np.array(samples)
samp *= (2**15)
samples = list(samp)
dict[12] = samples

Touch = song_root / r"Touch The Sky_Hillsong UNITED.mp3"
samples, fs = librosa.load(Touch, sr=44100, mono=True, duration=156)
samp = np.array(samples)
samp *= (2**15)
samples = list(samp)
dict[13] = samples

Watch = song_root / r"Watch_Billie Eilish.mp3"
samples, fs = librosa.load(Watch, sr=44100, mono=True, duration=156)
samp = np.array(samples)
samp *= (2**15)
samples = list(samp)
dict[14] = samples

