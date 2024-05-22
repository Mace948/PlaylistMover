# IMPORT PLAYLIST ONLY

from bs4 import BeautifulSoup
from selenium import webdriver
from handle_output import saveStringsToFile
import time
import os

def createHeadlessFirefoxBrowser():
     options = webdriver.FirefoxOptions()
     options.add_argument('--headless')
     return webdriver.Firefox(options=options)

def scrape_loaded_page(browser):
    html = browser.page_source
    bs4_result = BeautifulSoup(html, 'html.parser')

    songs = bs4_result.find_all('span', attrs={'data-testid': 'title'})

    temp_song_list = []
    for song in songs:
         temp_song_list.append(song.text)
         print(song.text)

    return temp_song_list

def get_songs(url):
    try:
        browser = createHeadlessFirefoxBrowser()
        browser.get(url)

    except:
        print("Incorrect URL, please provide a full URL such as: https://www.deezer.com/en/playlist/id")
        return False

    final_songs = []

    is_at_bottom = False
    while not is_at_bottom:
        for song in scrape_loaded_page(browser):
            if song not in final_songs:
                final_songs.append(song)

        browser.execute_script("window.scrollBy(0, 20);")
        is_at_bottom = browser.execute_script("return (window.innerHeight + window.scrollY) >= document.body.scrollHeight;")

    browser.quit()
    return final_songs

def im(url):
    os.system("cls")
    print("Importing...")
    
    value = get_songs(url)
    time.sleep(10)
    
    if value != False:
        saveStringsToFile(value, "output.txt")
        return True
    
    return False

def ex(fav_play):
    os.system("cls")
    print("Exporting...")
    return False