# DONE

from ytmusicapi import YTMusic, setup_oauth
from handle_output import extractSongsFromFile, saveStringsToFile
import os
from time import sleep

file_path = 'oauth.json'

def get_playlist(url):
    try:
        if not os.path.exists(file_path):
            setup_oauth()

        ytmusic = YTMusic(file_path)

        id = url.split('=')[-1]
        playlist = ytmusic.get_playlist(id, limit=None)['tracks']

        track_names = [track['title'] for track in playlist]

        return track_names
    
    except:
        return False

def get_favorites():
    try:
        if not os.path.exists(file_path):
            setup_oauth()

        ytmusic = YTMusic(file_path)

        playlist = ytmusic.get_liked_songs()['tracks']

        track_names = [track['title'] for track in playlist]

        return track_names
    
    except:
        return False

def add_songs():
    if not os.path.exists(file_path):
        setup_oauth()
    ytmusic = YTMusic(file_path)
    songs = extractSongsFromFile('output.txt')
    output = search_songs(ytmusic, songs)
    
    for song in output:
        ytmusic.rate_song(song, "LIKE")
    

def search_songs(ytmusic, querys):
    
    songs = []
    count = 0
    for query in querys:
        try:
            song = ytmusic.search(query, limit=1, filter='songs')[0]['videoId']
            songs.append(song)
        except:
            count += 1
            print(f"({count}) Song Failed.")
    return songs

def im(fav_play, url):
    os.system("cls")
    print("Importing...")
    try:

        if fav_play == "Playlist":
            output_songs = get_playlist(url)
        else:
            output_songs = get_favorites()
        
        saveStringsToFile(output_songs, 'output.txt')
        return True
    except:
        return False

def ex(fav_play, url):
    os.system("cls")
    print("Exporting...")
    try:

        if fav_play == "Playlist":
            if not os.path.exists(file_path):
                setup_oauth()
            ytmusic = YTMusic(file_path)
            songs = extractSongsFromFile('output.txt')
            output = search_songs(ytmusic, songs)
            
            ytmusic.add_playlist_items(url.split("=")[-1], output)
        else:
            add_songs()
        return True
    except any as e:
        print(e)
        return False
