import audio_sampling, saveSongs_mac, find_peaks, spectrogram, get_mic_input, fingerprints, pickle, matching
from microphone import record_audio
import numpy as np

def main():


    #Known song dict with each key as a song number starting at zero with a list of samples as the value
    with open("song_fingerprints.pkl", mode="rb") as opened_file:
        known_songs = pickle.load(opened_file)

    mic_spec = get_mic_input.rec(10)     #Spectrogram of the mic input

    sorted_a = np.sort(mic_spec, axis=None)
    cutoff = sorted_a[int(0.77 * len(sorted_a))]
    mic_peaks = find_peaks.local_peaks(mic_spec, cutoff, 20)  #Find peaks of the unknown samples
    mic_fingerprint = fingerprints.sample_fingerprint(mic_peaks)   #Fingerprint the unknown samples

    print(known_songs.values())

    print(matching.match(mic_fingerprint, known_songs))

if __name__ == "__main__":
    main()