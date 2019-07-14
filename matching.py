from collections import Counter
import pickle
name = "matching"


def match(fingerprint, database):
    """
    method finds if there is a match or song is not recognized

    :param fingerprint: list of unknown recording containing tuples of [t_n,(f_n, f_n+fan_out_vals,dt)]
    :param database: dictionary of all song keys and their (song id, time)

    :return: a song name or 'no match'
    """

    c = []
    # tup is unknown song data- contains time and fingerprints
    for tup in fingerprint:

        # check if fingerprint is a key
        if tup[1] in database.keys():
            songs = database[tup[1]]
            for item in songs:
                c.append(songs[0])

    # check most popular song id
    print("c")
    print(c)
    # c1 = [item[0] for item in c]
    # print("C1")
    # print(c1)
    most_com = Counter(c).most_common(5)
    print("Most_com")
    print(most_com)
    threshold = 70
    if most_com[0][1] < threshold:
        return "Petar doesn't recognize that song"
    else:
        song_id = most_com[0][0]
        with open("SongIds.pkl", mode="rb") as opened_file:
            songIDs = pickle.load(opened_file)
            return songIDs[song_id]


    c = Counter()

    for tup in fingerprint:

        # check if fingerprint is a key
        if tup[1] in database.keys():
            time, peak = tup

            # pair is value tuple with id and time
            pair = database[peak]
            c[pair[0], pair[1] - time] += 1

        # check most popular song id
    most_com = c.most_common(5)
    print(most_com)
    threshold = 100
    if most_com[0][1] < threshold:
        return "Petar doesn't recognize that song"
    else:
        song_id = most_com[0][0][0]
        return song_id
