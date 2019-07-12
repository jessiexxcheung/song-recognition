import audio_sampling, saveSongs, find_peaks, spectrogram, get_mic_input
from microphone import record_audio
import numpy as np

def main():


    #Known song dict with each key as a song number starting at zero with a list of samples as the value
    known_songs = saveSongs.orgSongDict

    mic_spec = get_mic_input.rec(10)     #Spectrogram of the mic input

    mic_peaks = find_peaks.local_peaks(mic_spec, .77, 20)  #Find peaks of the unknown samples

    #Fingerprint the unknown samples


    #Check for matches of the unknown samples to the known sample dictionary


    #Return found or not found statement

if __name__ == "__main__":
    main()