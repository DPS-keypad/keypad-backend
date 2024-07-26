import requests
from requests_oauthlib import OAuth2Session
from app.utils.constants import *

# Set up your Spotify API credentials
client_id = 'ad7f25142d414884913dd1483e4d7f61'
client_secret = 'efd29132685b43a38dae11cafff6a7a7'
redirect_uri = 'https://localhost:8000/callback'  # Replace with your own redirect URI

# Set up OAuth session
oauth = OAuth2Session(client_id, redirect_uri=redirect_uri, scope='user-read-currently-playing')
# Get authorization URL
authorization_url, state = oauth.authorization_url('https://accounts.spotify.com/authorize')
# Print the authorization URL and prompt the user to visit it
print(f'Please visit the following URL to authorize the application: {authorization_url}')
# After the user authorizes the application, they will be redirected to the redirect URI with an authorization code
authorization_code = input('Enter the authorization code from the redirect URI: ')

# Fetch access token using the authorization code
token = oauth.fetch_token('https://accounts.spotify.com/api/token', authorization_response=authorization_code, client_secret=client_secret)

# Get the access token from the token response
access_token = token['access_token']

def get_authorization_url():
    """
    Get the authorization URL to direct the user for OAuth2 authentication.
    """
    oauth = OAuth2Session(client_id, redirect_uri=redirect_uri)
    authorization_url, state = oauth.authorization_url(AUTH_URL)
    return authorization_url, state

def fetch_access_token(client_secret, authorization_code):
    """
    Fetch the access token using the authorization code.
    """
    oauth = OAuth2Session(client_id, redirect_uri=redirect_uri)
    token = oauth.fetch_token(TOKEN_URL, authorization_response=authorization_code, client_secret=client_secret)
    return token['access_token']

def get_currently_playing_track(access_token):
    """
    Get the currently playing track from the Spotify API.
    """
    headers = {'Authorization': f'Bearer {access_token}'}
    response = requests.get(CURRENTLY_PLAYING_URL, headers=headers)
    print(f'Response status code: {response.status_code}')  # Debug print statement
    if response.status_code == 200:
        track_data = response.json()
        track_name = track_data['item']['name']
        artist_name = track_data['item']['artists'][0]['name']
        return track_name, artist_name
    return None, None

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

def get_devices(access_token):
    """
    Get the list of available devices.
    """
    headers = {'Authorization': f'Bearer {access_token}'}
    response = requests.get(DEVICES_URL, headers=headers)
    if response.status_code == 200:
        devices = response.json()['devices']
        return devices
    return []


