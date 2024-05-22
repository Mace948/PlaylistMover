from prompts import *
from handles import *
import inquirer
import os
from im_ex_map import *

def toImProgram(im_program):
    if im_program == "Deezer":
        url = prompt(Q_URL)
        return im_deezer(url)
    
    if im_program == "Spotify":
        fav_play = prompt(Q_FAV_PLAY)
        
        if fav_play == "Playlist":
            url = prompt(Q_ID)
            return im_spotify(fav_play, url)
        else:
            return im_spotify(fav_play)
    
    if im_program == "Youtube":
        fav_play = prompt(Q_FAV_PLAY)
        
        if fav_play == "Playlist":
            url = prompt(Q_URL)
            return im_youtube(fav_play, url)
        else:
            return im_youtube(fav_play)

def toExProgram(im_program):
    if im_program == "Deezer":
        return ex_deezer(1)
    
    if im_program == "Spotify":
        fav_play = prompt(Q_FAV_PLAY)
        if fav_play == "Playlist":
            url = prompt(Q_ID)
            return ex_spotify(fav_play, url)
        return ex_spotify(fav_play)
    
    if im_program == "Youtube":
        fav_play = prompt(Q_FAV_PLAY)
        if fav_play == "Playlist":
            url = prompt(Q_URL)
            return ex_youtube(fav_play, url)
        return ex_youtube(fav_play)

def say(text):
    os.system("cls")
    print(text)

def prompt(prompt, text=None):
    os.system("cls")
    if text:
        print("   " + text)
    answers = inquirer.prompt(prompt, theme=THEME_CustomCyan)
    return answers['answer']

if __name__ == "__main__":
    handleInit(prompt(Q_INIT))

    if handleImEx(prompt(Q_IM_EX)): # Exporting
        im_program = prompt(Q_IM_PROGRAM)

        say("Completed.") if toImProgram(im_program) else say("Failed.") 

    else: # Importing
        ex_program = prompt(Q_EX_PROGRAM)

        say("Completed.") if toExProgram(ex_program) else say("Failed.")
