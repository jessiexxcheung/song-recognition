from microphone import record_audio
def rec(t):
    """
    Receives microphone input and creates a log spectrogram of the audio, capping any amplitude less than 1E-20
    :param t: The amount of seconds to record
    :return: The log scaled spectrogram
    """
    listen_time = t  # seconds
    frames, sample_rate = record_audio(listen_time)
    np.hstack([np.frombuffer(i, np.int16) for i in frames])
    audio_data = np.hstack([np.frombuffer(i, np.int16) for i in frames])
    sampling_rate = 44100
    S, freqs, times = mlab.specgram(audio_data, NFFT=4096, Fs=sampling_rate,
                                    window=mlab.window_hanning,
                                    noverlap=int(4096 / 2))
    S[S <= 1e-20] = 1e-20
    return np.log(S)