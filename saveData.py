import pickle
import matplotlib.mlab as mlab
from numba import njit
import numpy as np
from scipy.ndimage.morphology import generate_binary_structure
from scipy.ndimage.morphology import iterate_structure


@njit()
def _peaks(spec, rows, cols, amp_min):
    peaks = []
    # We want to iterate over the array in column-major
    # order so that we order the peaks by time. That is,
    # we look for nearest neighbors of increasing frequencies
    # at the same times, and then move to the next time bin.
    # This is why we use the reversed-shape
    for c, r in np.ndindex(*spec.shape[::-1]):
        if spec[r, c] < amp_min:
            continue

        for dr, dc in zip(rows, cols):
            # don't compare element (r, c) with itself
            if dr == 0 and dc == 0:
                continue

            # mirror over array boundary
            if not (0 <= r + dr < spec.shape[0]):
                dr *= -1

            # mirror over array boundary
            if not (0 <= c + dc < spec.shape[1]):
                dc *= -1

            if spec[r, c] < spec[r + dr, c + dc]:
                break
        else:
            peaks.append((c, r))
    return peaks


def local_peaks(log_spectrogram, amp_min, p_nn):
    """
    Defines a local neighborhood and finds the local peaks
    in the spectrogram, which must be larger than the
    specified `amp_min`.

    Parameters
    ----------
    log_spectrogram : numpy.ndarray, shape=(n_freq, n_time)
        Log-scaled spectrogram. Columns are the periodograms of
        successive segments of a frequency-time spectrum.

    amp_min : float
        Amplitude threshold applied to local maxima

    p_nn : int
        Number of cells around an amplitude peak in the spectrogram in order

    Returns
    -------
    List[Tuple[int, int]]
        Time and frequency index-values of the local peaks in spectrogram.
        Sorted by ascending frequency and then time.

    Notes
    -----
    The local peaks are returned in column-major order for the spectrogram.
    That is, the peaks are ordered by time. That is, we look for nearest
    neighbors of increasing frequencies at the same times, and then move to
    the next time bin.
    """
    struct = generate_binary_structure(2, 1)
    neighborhood = iterate_structure(struct, p_nn)
    rows, cols = np.where(neighborhood)
    assert neighborhood.shape[0] % 2 == 1
    assert neighborhood.shape[1] % 2 == 1

    # center neighborhood indices around center of neighborhood
    rows -= neighborhood.shape[0] // 2
    cols -= neighborhood.shape[1] // 2

    detected_peaks = _peaks(log_spectrogram, rows, cols, amp_min=amp_min)

    # Extract peaks; encoded in terms of time and freq bin indices.
    # dt and df are always the same size for the spectrogram that is produced,
    # so the bin indices consistently map to the same physical units:
    # t_n = n*dt, f_m = m*df (m and n are integer indices)
    # Thus we can codify our peaks with integer bin indices instead of their
    # physical (t, f) coordinates. This makes storage and compression of peak
    # locations much simpler.

    return detected_peaks


def create_spec(audio):
    sampling_rate = 44100
    S, freqs, times  = mlab.specgram(audio, NFFT=4096, Fs=sampling_rate,
                                    window=mlab.window_hanning,
                                    noverlap=int(4096 / 2))
    S[S<=1E-20] = 1E-20
    return np.log(S)


def song_fingerprint(song_id, peaks, fan_out=15):
    '''
    Reads in the times and frequencies of the peaks and returns
    the unique fingerprint of the song based on the peaks.

    Parameters
    ----------
    song_id : int
        Unique integer used to identify song.

    peaks : List[Tuple[int, int]]
        List of tuples containing times and frequencies of the peaks.

    fan_out : int
        Number of nearest column-major ordered neighbors that the
        fingerprint stores relationships with.

    Returns
    -------
    Dictionary[Tuple[int, int, int], List[Tuple[int,int]]]
        Fingerprint with keys representing (frequency1, frequency2, time between)
        and values representing the list of (song, time)s that match the key.

    '''
    d = {}
    for p in range(len(peaks)):
        if p > len(peaks)-fan_out:
            compare_peaks = peaks[p+1:]
        else:
            compare_peaks = peaks[p+1:p+fan_out]
        for c in range(len(compare_peaks)):
            if (peaks[p][1], compare_peaks[c][1], compare_peaks[c][0]-peaks[p][0]) not in d:
                d[(peaks[p][1], compare_peaks[c][1], compare_peaks[c][0]-peaks[p][0])] = [(song_id, peaks[p][0])]
            else:
                d[(peaks[p][1], compare_peaks[c][1], compare_peaks[c][0]-peaks[p][0])].append((song_id, peaks[p][0]))

    with open(str(song_id) + ".pkl", mode="wb") as opened_file:
        pickle.dump(d, opened_file)

    return d

def main():

if __name__ == "__main__":
    main()