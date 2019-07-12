import pickle
with open("dict.pkl", mode="rb") as songs_file:
    songs = pickle.load(songs_file)
print(songs)