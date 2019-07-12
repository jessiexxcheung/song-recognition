import sys
import librosa
from pathlib import Path
import numpy as np
from mutagen.mp3 import MP3
sampling_rate = 44100
bit_depth = 64
dict = {}
from pprint import pprint
import pickle
proj_root = Path(sys.path[0])  # sets the path of proj_root to song-recognition
song_root = proj_root / r"songs"  # sets the path of song_root to song-recognition/songs


files = sorted(song_root.glob('*.mp3'))  # Creates a list of all the song directories

for item in range(len(files)):
    audio = MP3(files[item])
    samples, fs = librosa.load(files[item], sr=44100, mono=True, duration=audio.info.length)
    samp = np.array(samples)
    samp *= (2 ** 15)
    samples = list(samp)
    dict[item] = samples
with open("dict.pkl",mode="wb") as songs_file:
    pickle.dump(dict, songs_file)