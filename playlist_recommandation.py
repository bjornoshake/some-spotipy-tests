import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

auth_manager = SpotifyClientCredentials()
sp = spotipy.Spotify()
song_list= []
recommended_song=[]
user = sp.user('')
sp.set_auth("")
pl = sp.playlist_tracks('')

for keys in pl["items"]:
    song_list.append(keys["track"]["uri"])
recommendation = sp.recommendations(seed_artists=[""], seed_genres=[""], seed_tracks=song_list, limit=30)
for track in recommendation["tracks"]:
    recommended_song.append(track["uri"])



#sp.user_playlist_create("othmanbjorn", "Ouistiti", public=True, collaborative=False, description='')
