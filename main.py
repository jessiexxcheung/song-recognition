import find_peaks, get_mic_input, fingerprints, pickle, matching
import numpy as np
import saveSongs
from collections import Counter

def main():

    # Known song dict with each key as a song number starting at zero with a list of samples as the value
    with open("song_fingerprints.pkl", mode="rb") as opened_file:
        known_songs = pickle.load(opened_file)


    #Known song dict with each key as a song number starting at zero with a list of samples as the value
    known_songs = saveSongs.songSave()

    mic_spec = get_mic_input.rec(20)     # Spectrogram of the mic input


    sorted_b = np.sort(mic_spec.flatten())
    cutoff = sorted_b[int(.77 * len(sorted_b))]
    mic_peaks = find_peaks.local_peaks(mic_spec, cutoff, 20)  # Find peaks of the unknown samples

    mic_fingerprint = fingerprints.sample_fingerprint(mic_peaks)   # Fingerprint the unknown samples
    # print("Known Songs")
    # print(known_songs)
    known_songs_1 = [song[0][0] for song in known_songs.values()]
    # print("known songs values")
    # print(known_songs_1)
    print(matching.match(mic_fingerprint, database=known_songs))
    # print('20 most common')
    # print(Counter(known_songs_1).most_common(20))

if __name__ == "__main__":
    main()
