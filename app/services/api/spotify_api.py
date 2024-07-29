from flask import jsonify, session
import requests
from app.utils.constants import *
import app.controllers.backendServerController as backend

"""
# Set up your Spotify API credentials
client_id = 'ad7f25142d414884913dd1483e4d7f61'
client_secret = 'efd29132685b43a38dae11cafff6a7a7'
"""

# Global variable for the name of the song that is currently playing
current_song = None
# Global boolean variable to check if the song has changed
changed_song = False


def get_currently_playing_track():
    """
    Get the currently playing track from the Spotify API.
    """
    headers = {'Authorization': f'Bearer {backend.get_accessToken()}'}
    response = requests.get(CURRENTLY_PLAYING_URL, headers=headers)
    print(f'Response status code: {response.status_code}')  # Debug print statement
    if response.status_code == 200:
        track_data = response.json()
        track_name = track_data['item']['name']
        artist_name = track_data['item']['artists'][0]['name']
        return track_name, artist_name
    return None, None


def play():
    """
    Play the currently paused track.
    """
    headers = {'Authorization': f'Bearer {backend.get_accessToken()}'}
    response = requests.put(PLAY_URL, headers=headers)
    if response.status_code == 204:
        print('Playback started.')
    else:
        print('Failed to start playback.')


def pause():
    """
    Pause the currently playing track.
    """
    headers = {'Authorization': f'Bearer {backend.get_accessToken()}'}
    response = requests.put(PAUSE_URL, headers=headers)
    if response.status_code == 204:
        print('Playback paused.')
    else:
        print('Failed to pause playback.')


def next():
    """
    Skip to the next track.
    """
    headers = {'Authorization': f'Bearer {backend.get_accessToken()}'}
    response = requests.post(NEXT_TRACK_URL, headers=headers)
    if response.status_code == 204:
        print('Skipped to next track.')
    else:
        print('Failed to skip to next track.')
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
    global changed_song
    current_song = song
    changed_song = True
