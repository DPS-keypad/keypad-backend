import requests
from app.utils.constants import *


def get_authorization_url(client_id, redirect_uri):
    """
    Get the authorization URL to direct the user for OAuth2 authentication.
    """
    oauth_params = {
        'client_id': client_id,
        'response_type': 'code',
        'redirect_uri': redirect_uri,
        'scope': 'user-read-playback-state user-modify-playback-state user-read-currently-playing',
    }
    authorization_url = f"{AUTH_URL}?{requests.compat.urlencode(oauth_params)}"
    return authorization_url


def fetch_access_token(client_id, client_secret, authorization_code, redirect_uri):
    """
    Fetch the access token using the authorization code.
    """
    token_params = {
        'grant_type': 'authorization_code',
        'code': authorization_code,
        'redirect_uri': redirect_uri,
        'client_id': client_id,
        'client_secret': client_secret,
    }
    response = requests.post(TOKEN_URL, data=token_params)
    response_data = response.json()
    return response_data['access_token']


def get_currently_playing_track(access_token):
    """
    Get the currently playing track from the Spotify API.
    """
    headers = {'Authorization': f'Bearer {access_token}'}
    response = requests.get(CURRENTLY_PLAYING_URL, headers=headers)
    if response.status_code == 200:
        track_data = response.json()
        track_name = track_data['item']['name']
        artist_name = track_data['item']['artists'][0]['name']
        return track_name, artist_name
    return None, None


#----------------------------------------------------------------------------
def play(access_token):
    """
    Play the currently paused track.
    """
    headers = {'Authorization': f'Bearer {access_token}'}
    response = requests.put(PLAY_URL, headers=headers)
    if response.status_code == 204:
        print('Playback started.')
    else:
        print('Failed to start playback.')


def pause(access_token):
    """
    Pause the currently playing track.
    """
    headers = {'Authorization': f'Bearer {access_token}'}
    response = requests.put(PAUSE_URL, headers=headers)
    if response.status_code == 204:
        print('Playback paused.')
    else:
        print('Failed to pause playback.')


def next(access_token):
    """
    Skip to the next track.
    """
    headers = {'Authorization': f'Bearer {access_token}'}
    response = requests.post(NEXT_TRACK_URL, headers=headers)
    if response.status_code == 204:
        print('Skipped to next track.')
    else:
        print('Failed to skip to next track.')


def previous(access_token):
    """
    Skip to the previous track.
    """
    headers = {'Authorization': f'Bearer {access_token}'}
    response = requests.post(PREVIOUS_TRACK_URL, headers=headers)
    if response.status_code == 204:
        print('Skipped to previous track.')
    else:
        print('Failed to skip to previous track.')


""" 
def set_volume(access_token, volume_percent):
    
    #Set the volume of the currently active device.
    
    headers = {'Authorization': f'Bearer {access_token}'}
    response = requests.put(f'{VOLUME_URL}?volume_percent={volume_percent}', headers=headers)
    if response.status_code == 204:
        print(f'Volume set to {volume_percent}%.')
    else:
        print('Failed to set volume.')
"""


def devices(access_token):
    """
    Get the list of available devices.
    """
    headers = {'Authorization': f'Bearer {access_token}'}
    response = requests.get(DEVICES_URL, headers=headers)
    if response.status_code == 200:
        devices = response.json()['devices']
        return devices
    return []


def playback(access_token, device_id):
    """
    Transfer playback to a different device.
    """
    headers = {'Authorization': f'Bearer {access_token}'}
    data = {"device_ids": [device_id], "play": True}
    response = requests.put(TRANSFER_PLAYBACK_URL, headers=headers, json=data)
    if response.status_code == 204:
        print('Playback transferred.')
    else:
        print('Failed to transfer playback.')


def search(access_token, query):
    """
    Search for a track on Spotify.
    """
    headers = {'Authorization': f'Bearer {access_token}'}
    params = {'q': query, 'type': 'track'}
    response = requests.get(SEARCH_URL, headers=headers, params=params)
    if response.status_code == 200:
        tracks = response.json()['tracks']['items']
        return [(track['name'], track['artists'][0]['name'], track['id']) for track in tracks]
    return []
