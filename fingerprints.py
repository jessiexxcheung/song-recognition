import pickle


def song_fingerprint(songId, peaks, fan_out=15):
    '''
    Reads in the times and frequencies of the peaks and returns
    the unique fingerprint of the song based on the peaks.

    Parameters
    ----------

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

    dict = {}
    for i in range(len(peaks)):
        imp = peaks[(i+1):(i+1+fan_out)]
        for item in imp:
            f0 = peaks[i][1]
            f1 = item[1]
            t0 = peaks[i][0]
            t1 = item[0]
            key = (f0, f1, t1-t0)
            value = (songId, t0)
            if key in dict:
                dict[key].append(value)
            else:
                dict[key] = [value]
    return dict


















    # d = {}
    # for song_id in range(len(peaks)):
    #     print(len(peaks[song_id]))
    #     for p in range(2):
    #         if p > len(peaks) - fan_out:
    #             compare_peaks = peaks[song_id][p + 1:]
    #         else:
    #             compare_peaks = peaks[song_id][p + 1:p + fan_out]
    #         for c in range(len(compare_peaks)):
    #             if (peaks[song_id][p][1], compare_peaks[c][1], compare_peaks[c][0] - peaks[song_id][p][0]) not in d:
    #                 d[(peaks[song_id][p][1], compare_peaks[c][1], compare_peaks[c][0] - peaks[song_id][p][0])] = [
    #                     (song_id, peaks[song_id][p][0])]
    #             else:
    #                 d[(peaks[song_id][p][1], compare_peaks[c][1], compare_peaks[c][0] - peaks[song_id][p][0])].append(
    #                     (song_id, peaks[song_id][p][0]))




def sample_fingerprint(peaks, fan_out=15):
    '''
    Reads in the times and frequencies of the peaks and returns
    the unique fingerprint of the song based on the peaks.

    Parameters
    ----------
    peaks : List[Tuple[int, int]]
        List of tuples containing times and frequencies of the peaks.

    fan_out : int
        Number of nearest column-major ordered neighbors that the
        fingerprint stores relationships with.

    Returns
    -------
    List[Tuple[int,Tuple[int,int,int]]]
        Fingerprint with times and (frequency1, frequency2, time between)s
        to be compared with known song fingerprints.

    '''

    l = []
    for p in range(len(peaks)):
        if p > len(peaks) - fan_out:
            compare_peaks = peaks[p:]
        else:
            compare_peaks = peaks[p:p + fan_out]
        for c in range(len(compare_peaks)):
            l.append((peaks[p][0],(peaks[p][1], compare_peaks[c][1], compare_peaks[c][0]-peaks[p][0])))
    return l
