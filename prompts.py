import inquirer
from inquirer.themes import load_theme_from_dict

THEME_CustomCyan = load_theme_from_dict({
    "List": {
        "selection_color": "cyan",
        "selection_cursor": "•"
     }
})

Q_INIT = [
    inquirer.List(
        "answer",
        message="   Music Switcher",
        choices=["Enter", "Quit"],
    ),
]

Q_IM_EX = [
    inquirer.List(
        "answer",
        message="   Import or Export Music?",
        choices=["Import", "Export"],
    ),
]

Q_FAV_PLAY = [
    inquirer.List(
        "answer",
        message="   Favorites or Playlist?",
        choices=["Favorites", "Playlist"],
    ),
    ]

Q_IM_PROGRAM = [
    inquirer.List(
        "answer",
        message="   What program do you want the playlist from?",
        choices=["Youtube", "Spotify", "Deezer (Limited Capability)"],
    ),
]

Q_EX_PROGRAM = [
    inquirer.List(
        "answer",
        message="   What program do you want to transfer the playlist to?",
        choices=["Youtube", "Spotify"],
    ),
]

Q_URL = [
    inquirer.Text(
        "answer",
        message="   URL: ",
    ),
]

Q_ID = [
    inquirer.Text(
        "answer",
        message="   ID: ",
    ),
]