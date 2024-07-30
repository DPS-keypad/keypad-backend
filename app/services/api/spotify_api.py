import time
import requests
from app.utils.constants import *
import app.controllers.backendServerController as backend

# Global variable for the name of the song that is currently playing
current_song = ["", ""]
# Global boolean variable to check if the song has changed
changed_song = False
# Global variable for the string to send through the serial
string_song = ""


def get_currently_playing_track():
    """
    Get the currently playing track from the Spotify API.
    """
    headers = {'Authorization': f'Bearer {backend.get_accessToken()}'}
    response = requests.get(CURRENTLY_PLAYING_URL, headers=headers)
    if response.status_code == 200:
        track_data = response.json()
        track_name = track_data['item']['name']
        artist_name = track_data['item']['artists'][0]['name']
        return track_name, artist_name
    return None, None


def play():
    """
    Play/pause the current track.
    """
    # Get the current playback state
    headers = {'Authorization': f'Bearer {backend.get_accessToken()}'}
    response = requests.get(GET_PLAYBACK_URL, headers=headers)
    if response.status_code == 200:
        playing = response.json()['is_playing']
    else:
        print('Failed to get playback state.')
        return
    # Play or pause the track
    url = PLAY_URL if not playing else PAUSE_URL
    headers = {'Authorization': f'Bearer {backend.get_accessToken()}'}
    response = requests.put(url, headers=headers)
    if response.status_code == 200:
        print('Music playing.' if not playing else 'Music paused.')
    else:
        print('Failed to start playback.')


def next():
    """
    Skip to the next track.
    """
    headers = {'Authorization': f'Bearer {backend.get_accessToken()}'}
    response = requests.post(NEXT_TRACK_URL, headers=headers)
    if response.status_code == 200:
        print('Skipped to next track.')
    else:
        print('Failed to skip to next track.')
    tick = time.time()
    while time.time() - tick < 1:
        pass
    set_song(get_currently_playing_track())


def previous():
    """
    Skip to the previous track.
    """
    headers = {'Authorization': f'Bearer {backend.get_accessToken()}'}
    response = requests.post(PREVIOUS_TRACK_URL, headers=headers)
    if response.status_code == 204:
        print('Skipped to previous track.')
    else:
        print('Failed to skip to previous track.')
    tick = time.time()
    while time.time() - tick < 1:
        pass
    set_song(get_currently_playing_track())


def song_has_changed():
    global changed_song
    return changed_song


def get_song():
    global current_song
    global changed_song
    changed_song = False
    return current_song


def set_song(song):
    global current_song
    global string_song
    global changed_song
    current_song = song
    string_song = song[0]
    changed_song = True


def get_song_string():
    global string_song
    global changed_song
    changed_song = False
    return string_song


def set_song_string(song):
    global string_song
    global changed_song
    changed_song = True
    string_song = song
