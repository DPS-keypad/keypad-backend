# Serial constants
BAUDRATE = 115200
BYTESIZE = 8
PARITY = 'N'
STOPBITS = 1
TIMEOUT = 1

"""
# Keyboard constants
KEY1 = 'a'
KEY2 = 'b'
KEY3 = 'c'
KEY4 = 'd'
KEY5 = 'e'
KEY6 = 'f'
KEY7 = 'g'
KEY8 = 'h'
KEY9 = 'i'
POT1 = 'j'
POT2 = 'k'
POT3 = 'l'
"""

# paths
KEYBOARD_ACTIONS_LIST_PATH = 'app/models/keyboardActionsList.json'
ALL_ACTIONS_LIST_PATH = 'app/models/allActionsList.json'

SECRET_KEY = 'your_secret_key'
DEBUG = True

# SPOTIFY API
# Constants for the Spotify API
AUTH_URL = 'https://accounts.spotify.com/authorize'
TOKEN_URL = 'https://accounts.spotify.com/api/token'
CURRENTLY_PLAYING_URL = 'https://api.spotify.com/v1/me/player/currently-playing'
PLAY_URL = 'https://api.spotify.com/v1/me/player/play'
PAUSE_URL = 'https://api.spotify.com/v1/me/player/pause'
NEXT_TRACK_URL = 'https://api.spotify.com/v1/me/player/next'
PREVIOUS_TRACK_URL = 'https://api.spotify.com/v1/me/player/previous'
VOLUME_URL = 'https://api.spotify.com/v1/me/player/volume'
DEVICES_URL = 'https://api.spotify.com/v1/me/player/devices'
SEARCH_URL = 'https://api.spotify.com/v1/search'
TRANSFER_PLAYBACK_URL = 'https://api.spotify.com/v1/me/player'

# SYSTEM API
# Define constants for volume & mouse control
VOLUME_MIN = 0
VOLUME_MAX = 65535

# Define constants for mouse control
MOUSEEVENTF_WHEEL = 0x0800
MOUSEEVENTF_HWHEEL = 0x01000


# VS Code API
VSCODE_PATH = r'C:\Users\Gledi\AppData\Local\Programs\Microsoft VS Code\Code.exe'  # Modifica questo percorso se necessario
