# Serial constants
BAUDRATE = 115200
BYTESIZE = 8
PARITY = 'N'
STOPBITS = 1
TIMEOUT = 1

# paths
KEYPAD_ACTIONS_LIST_PATH = 'app/models/keypadActionsList.json'
ALL_ACTIONS_LIST_PATH = 'app/models/allActionsList.json'

# SPOTIFY API
# Constants for the Spotify API
CLIENT_ID = 'd68f5af7ddd941369a760d7e4f958033'
CLIENT_SECRET = 'dde2215cabdd42f2abe3f52256ef4d52'
REDIRECT_URI = 'http://localhost:8000/callback'
API_BASE_URL = 'https://api.spotify.com/v1/'
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
GET_PLAYBACK_URL = 'https://api.spotify.com/v1/me/player'


# SYSTEM API
# Define constants for volume & mouse control
VOLUME_MIN = 0
VOLUME_MAX = 65535

# Define constants for mouse control
MOUSEEVENTF_WHEEL = 0x0800
MOUSEEVENTF_HWHEEL = 0x01000
