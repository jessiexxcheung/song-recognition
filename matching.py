import collections
name = "matching"


def match(fingerprint, database):
    """
    method finds if there is a match or song is not recognized

    :param fingerprint: list of unknown recording containing tuples of [t_n,(f_n, f_n+fan_out_vals,dt)]
    :param database: dictionary of all song keys and their (song id, time)

    :return: a song name or 'no match'
    """
    # collections.Counter
    c = collections.Counter()

    # tup is unknown song data- contains time and key
    for tup in fingerprint:

        # check if fingerprint is a key
        if tup[1] in database.keys():
            time, peak = tup

            # pair is value tuple with id and time
            for pair in database[peak]:
                c[pair[0], pair[1]-time] += 1

    # check most popular song id
    most_com = c.most_common(1)
    print(c.most_common[0][1])
    threshold = 100
    if most_com[0][1] < threshold:
        return "Petar doesn't recognize the song"
    else:
        song_id = most_com[0][0]
        return song_id
