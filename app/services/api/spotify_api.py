from requests_oauthlib import OAuth2Session
from flask import jsonify, redirect, session
import requests
from app.utils.constants import *
import app.controllers.backendServerController as backend
from datetime import datetime, timedelta

"""
# Set up your Spotify API credentials
client_id = 'ad7f25142d414884913dd1483e4d7f61'
client_secret = 'efd29132685b43a38dae11cafff6a7a7'
"""


def playlists():



    headers = {'Authorization': f'Bearer {backend.get_accessToken()}'}
    response = requests.get(f'{API_BASE_URL}me/playlists', headers=headers)
    playlists = response.json()  # This is a list of playlists
    return jsonify(playlists)


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
    access_token = session['access_token']
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


def next(access_token):
    """
    Skip to the next track.
    """
    headers = {'Authorization': f'Bearer {backend.get_accessToken()}'}
    response = requests.post(NEXT_TRACK_URL, headers=headers)
    if response.status_code == 204:
        print('Skipped to next track.')
    else:
        print('Failed to skip to next track.')


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


def get_devices():
    """
    Get the list of available devices.
    """
    headers = {'Authorization': f'Bearer {backend.get_accessToken()}'}
    response = requests.get(DEVICES_URL, headers=headers)
    if response.status_code == 200:
        devices = response.json()['devices']
        return devices
    return []


"""
music = "Ciao"


def get_music():
    global music
    return music


def set_music(music_new):
    global music
    music = music_new
"""


def song_has_changed():
    return None


def get_song():
    return None
