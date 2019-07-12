import sys
import librosa
from pathlib import Path
import numpy as np
from mutagen.mp3 import MP3
import pickle

orgSongDict = {}  # Initializes an empty dictionary which the data will be added to.

proj_root = Path(sys.path[0])  # sets the path of proj_root to song-recognition
song_root = proj_root / r"songs"  # sets the path of song_root to song-recognition/songs

files = sorted(song_root.glob('*.mp3'))  # Creates a list of all the song directories

# Iterates through the files, takes samples on each of them, and adds each of them to the dictionary
for item in range(len(files)):
    audio = MP3(files[item])
    samples, fs = librosa.load(files[item], sr=44100, mono=True, duration=audio.info.length)
    samp = np.array(samples)
    samp *= (2 ** 15)
    samples = list(samp)
    orgSongDict[item] = samples
