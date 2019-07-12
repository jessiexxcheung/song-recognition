def song_fingerprint(song_id, peaks, fan_out=15):
    '''
    Reads in the frequencies and times of the peaks and returns
    the unique fingerprint of the song based on the peaks.

    Parameters
    ----------
    song_id : int
        Unique integer used to identify song.

    peaks : List[Tuple[int, int]]
        List of tuples containing frequencies and times of the peaks.

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
            compare_peaks = peaks[p:]
        else:
            compare_peaks = peaks[p:p+fan_out]
        for c in range(len(compare_peaks)):
            if (p[0], c[0], c[1]-p[1]) not in d:
                d[(p[0], c[0], c[1]-p[1])] = [(song_id, p[1])]
            else:
                d[(p[0], c[0], c[1]-p[1])].append([(song_id, p[1])])
    return d


def sample_fingerprint(peaks, fan_out=15):
    '''
    Reads in the frequencies and times of the peaks and returns
    the unique fingerprint of the song based on the peaks.

    Parameters
    ----------
    peaks : List[Tuple[int, int]]
        List of tuples containing frequencies and times of the peaks.

    fan_out : int
        Number of nearest column-major ordered neighbors that the
        fingerprint stores relationships with.

    Returns
    -------
    List[Tuple[int,int]]
        Fingerprint with (frequency1, frequency2, time between)s
        to be compared with known song fingerprints.

    '''
    l = []
    for p in range(len(peaks)):
        if p > len(peaks) - fan_out:
            compare_peaks = peaks[p:]
        else:
            compare_peaks = peaks[p:p + fan_out]
        for c in range(len(compare_peaks)):
            l.append((p[0], c[0], c[1]-p[1]))
    return l