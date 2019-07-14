import find_peaks, get_mic_input, fingerprints, pickle, matching
import numpy as np
from collections import Counter

def main():

    # Known song dict with each key as a song number starting at zero with a list of samples as the value
    with open("song_fingerprints.pkl", mode="rb") as opened_file:
        known_songs = pickle.load(opened_file)

    mic_spec = get_mic_input.rec(10)     # Spectrogram of the mic input

    sorted_a = np.sort(mic_spec, axis=None)
    cutoff = sorted_a[int(0.77 * len(sorted_a))]
    mic_peaks = find_peaks.local_peaks(mic_spec, cutoff, 20)  # Find peaks of the unknown samples

    mic_fingerprint = fingerprints.sample_fingerprint(mic_peaks)   # Fingerprint the unknown samples
    print("Known Songs")
    known_songs_1 = [song[0] for song in known_songs.values()]
    # print(known_songs_1)
    print(matching.match(mic_fingerprint, database=known_songs))
    # print(Counter(known_songs_1).most_common(20))

if __name__ == "__main__":
    main()
