import collections
name = "matching"


def match(fingerprint, database):
    """
    method finds if there is a match or song is not recognized

    :param fingerprint: list of unknown recording (f_n, f_n+fan_out_vals,dt)
    :param database: dictionary of all song keys and their (song id, time)

    :return: a song name or 'no match'
    """
    # arr of values

    val = list()
    # check if fingerprint is a key, append to list of values
    for i in range(len(fingerprint)):
        if fingerprint[i] in database.keys():
            val.append(database[fingerprint[i]])

    # collections.Counter
    # check most popular song id
    c = collections.Counter()
    for v in val:
        for i in range(len(v)):
            c[v[i][0]] += 1
    most_com = c.most_common(1)
    song_id = most_com[0][0]
    return song_id