# DONE

import spotipy
from spotipy.oauth2 import SpotifyOAuth
from handle_output import saveStringsToFile, extractSongsFromFile
import os
from load_env import Load_Env_Vars

CLIENT_ID, CLIENT_SECRET, REDIRECT_URI = Load_Env_Vars()

def authenticate_spotify():
    scope = "user-library-modify user-library-read playlist-modify-private playlist-modify-public"
    sp_oauth = SpotifyOAuth(client_id=CLIENT_ID,
                            client_secret=CLIENT_SECRET,
                            redirect_uri=REDIRECT_URI,
                            scope=scope)
    token_info = sp_oauth.get_access_token(as_dict=False)
    sp = spotipy.Spotify(auth=token_info)
    return sp

def get_liked_songs(sp):
    results = sp.current_user_saved_tracks()
    liked_songs = []

    while results:
        for item in results['items']:
            track = item['track']
            liked_songs.append(track['name'])
        if results['next']:
            results = sp.next(results)
        else:
            results = None

    return liked_songs

def get_playlist_songs(sp, playlist_id):
    results = sp.playlist_tracks(playlist_id)
    playlist_songs = []

    while results:
        for item in results['items']:
            track = item['track']
            playlist_songs.append(track['name'])
        if results['next']:
            results = sp.next(results)
        else:
            results = None

    return playlist_songs

def search(sp, query):
    results = sp.search(query, type='track', limit=1)
    return results['tracks']['items'][0]

def im(fav_play, url):
    os.system("cls")
    print("Importing...")
    try:
        if fav_play == "Favorites":
            sp = authenticate_spotify()
            liked_songs = get_liked_songs(sp)
            saveStringsToFile(liked_songs, "output.txt")
        else:
            sp = authenticate_spotify()
            songs = get_playlist_songs(sp, url)
            saveStringsToFile(songs, "output.txt")

        return True    
    except:
        return False

def add_songs_to_playlist(sp, id, ids):
    sp.playlist_add_items(id, ids)

def ex(fav_play, url):
    os.system("cls")
    print("Exporting...")
    try:
        if fav_play == "Favorites":
            sp = authenticate_spotify()
            songs = extractSongsFromFile("output.txt")
            ids = []
            count = 0
            for song in songs:
                try:
                    ids.append(search(sp, song)['id'])
                except:
                    count += 1
                    print(f"({count}) Song Failed.")
            sp.current_user_saved_tracks_add(ids)

        else:
            sp = authenticate_spotify()
            songs = extractSongsFromFile("output.txt")
            ids = []
            count = 0
            for song in songs:
                try:
                    ids.append(search(sp, song)['id'])
                except:
                    count += 1
                    print(f"({count}) Song Failed.")
            add_songs_to_playlist(sp, url, ids)

        return True 
    except:
        return False
            
