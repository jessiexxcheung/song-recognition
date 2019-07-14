import sys
import librosa
from pathlib import Path
import numpy as np
from mutagen.mp3 import MP3
import pickle
import spectrogram
import find_peaks
import fingerprints


def songSave():

    """
    :return: dictionary orgSongDict
        A dictionary containing each song key mapped to a digital representation of the song
    """

    orgSongDict = {}  # Initializes an empty dictionary which the song ids mapped to the data will be added to.
    songIdDict = {}  # Initializes an empty dictionary which the song ids mapped to the songs will be added to
    database = {}



    proj_root = Path(sys.path[0])  # sets the path of proj_root to song-recognition
    song_root = proj_root / r"songs"  # sets the path of song_root to song-recognition/songs

    files = sorted(song_root.glob('*.mp3'))  # Creates a list of all the song directories

    # Iterates through the files and maps each song ID to a tuple containing the song and the artist
    for i in range(len(files)):
        item2 = files[i].stem
        item3 = tuple(item2.split("_"))
        songIdDict[i] = item3

    # Pickles songIdDict
    with open("SongIds.pkl", mode="wb") as opened_file:
        pickle.dump(songIdDict, opened_file)

    # Iterates through the files, takes samples on each of them, and adds each of them to the dictionary
    for item in range(len(files)):
        audio = MP3(files[item])
        samples, fs = librosa.load(files[item], sr=44100, mono=True, duration=audio.info.length)
        samp = np.array(samples)
        samp *= (2 ** 15)
        samples = list(samp)
        orgSongDict[item] = samples
    print(len(orgSongDict.values()))
    for i in range(len(orgSongDict.values())):
        sorted_a = np.sort(list(orgSongDict.values())[i], axis=None)
        print("len(sorted_a)")
        print(len(sorted_a))
        cutoff = sorted_a[int(0.77 * len(sorted_a))]
        specSong = spectrogram.create_spec(list(sorted_a))
        songPeaks = find_peaks.local_peaks(specSong, cutoff, 20)
        # print("songpeaks below")
        # print(songPeaks)
        print(i)
        # print("len")
        print(len(songPeaks))
        a = fingerprints.song_fingerprint(i, songPeaks)
        database.update(a)
    with open("song_fingerprints.pkl", mode="wb") as opened_file:
        pickle.dump(database, opened_file)
    # for item in database.values():
    #     print(item)
    return orgSongDict

songSave()
