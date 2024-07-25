"""
import requests
import time

from requests_oauthlib import OAuth2Session

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

# Rest of the code...
while True:
    # Make a request to the Spotify API to get the currently playing track
    headers = {
        'Authorization': f'Bearer {access_token}'
    }

    response = requests.get('https://api.spotify.com/v1/me/player/currently-playing', headers=headers)

    print(f'Response status code: {response.status_code}')  # Debug print statement

    if response.status_code == 200:
        track_data = response.json()
        track_name = track_data['item']['name']
        artist_name = track_data['item']['artists'][0]['name']
        print(f'Currently playing: {track_name} by {artist_name}')
    else:
        print('No track currently playing.')

    # Wait for some time before polling again
    time.sleep(5)  # Adjust the sleep duration as needed
"""

import threading
import app.controllers.backendServerController as server
import app.controllers.serialController as serialController

serial = serialController.SerialController()

# Start the serial communication in a separate thread
threading.Thread(target=serial.listen).start()

# Start the Flask server in the main thread
server.listen()
