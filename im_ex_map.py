from programs import deezer
from programs import youtube
from programs import spotify

def im_deezer(url):
    return deezer.im(url)

def im_spotify(fav_play, url=False):
    return spotify.im(fav_play, url)

def im_youtube(fav_play, url=False):
    return youtube.im(fav_play, url)

def ex_deezer(fav_play):
    return deezer.ex(fav_play)

def ex_spotify(fav_play, url=False):
    return spotify.ex(fav_play, url)

def ex_youtube(fav_play, url=False):
    return youtube.ex(fav_play, url)