import audio_sampling, saveSongs, find_peaks, spectrogram, get_mic_input, fingerprints, pickle, matching
from microphone import record_audio
import numpy as np

def main():


    #Known song dict with each key as a song number starting at zero with a list of samples as the value
    known_songs = saveSongs.orgSongDict

    mic_spec = get_mic_input.rec(10)     #Spectrogram of the mic input

    mic_peaks = find_peaks.local_peaks(mic_spec, .77, 20)  #Find peaks of the unknown samples
    mic_fingerprint = fingerprints.sample_fingerprint(mic_peaks)   #Fingerprint the unknown samples

    return matching.match(mic_fingerprint, known_songs)

if __name__ == "__main__":
    main()