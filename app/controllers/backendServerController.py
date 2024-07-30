import json
import app.controllers.actionController as actionController
from app.utils.constants import *
import app.services.api.spotify_api as spotify_api
from datetime import datetime, timedelta
from flask_cors import CORS
from flask import Flask, jsonify, request, redirect, session
import requests
import threading

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:4200"}})

app.secret_key = '53d355f8-571a-4590-a310-1f9579440851'  # This is a secret key used to sign the session cookies
file_lock = threading.Lock()


def get_accessToken():
    with open('app/utils/spotify.json', 'r') as file:
        data = json.load(file)
    return data['access_token']


def set_accessToken(access_token_new):
    # writes the access_token constant in the constants.py file
    with file_lock:
        with open('app/utils/spotify.json', 'r') as file:
            data = json.load(file)
            print(data)
            data['access_token'] = access_token_new
            with open('app/utils/spotify.json', 'w') as file:
                json.dump(data, file)


def get_refreshToken():
    with open('app/utils/spotify.json', 'r') as file:
        data = json.load(file)
        return data['refresh_token']


def set_refreshToken(refresh_token_new):
    with file_lock:
        with open('app/utils/spotify.json', 'r') as file:
            data = json.load(file)
            data['refresh_token'] = refresh_token_new
            with open('app/utils/spotify.json', 'w') as file:
                json.dump(data, file)


def get_expires_at():
    with open('app/utils/spotify.json', 'r') as file:
        data = json.load(file)
        return data['expires_at']


def set_expires_at(expires_at_new):
    with file_lock:
        with open('app/utils/spotify.json', 'r') as file:
            data = json.load(file)
            data['expires_at'] = str(expires_at_new)
            with open('app/utils/spotify.json', 'w') as file:
                json.dump(data, file)


# Quando l'utente completa l'autenticazione, il server di autenticazione (come Spotify) reindirizzerà l'utente a questo URI con le informazioni necessarie, come il codice di autorizzazione o il token di accesso.
@app.route('/callback', methods=['GET'])
def callback():
    if 'error' in request.args:
        return redirect(f'http://localhost:4200?auth_status=error&error={request.args["error"]}')

    elif 'code' in request.args:
        req_body = {
            'code': request.args['code'],
            'grant_type': 'authorization_code',
            'redirect_uri': REDIRECT_URI,
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET
        }

        response = requests.post(TOKEN_URL, data=req_body)
        token_info = response.json()
        try:
            set_accessToken(token_info['access_token'])
            set_refreshToken(token_info['refresh_token'])
            set_expires_at(datetime.now() + timedelta(
                seconds=token_info['expires_in']))  # The time in seconds until the access token expires
            print(datetime.now() + timedelta(seconds=token_info['expires_in']))
            current_song = spotify_api.get_currently_playing_track()
            spotify_api.set_song(current_song)

            return redirect(f'http://localhost:4200?auth_status=success')

        except KeyError:
            return redirect(f'http://localhost:4200?auth_status=error&error={token_info["error_description"]}')


@app.route('/refresh_token', methods=['GET'])
def refresh_token():
    if 'refresh_token' not in session:
        return redirect('/spotify/login')

    if datetime.now() > session['expires_at'].replace(tzinfo=None):
        req_body = {
            'grant_type': 'refresh_token',
            'refresh_token': session['refresh_token'],
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET
        }

        response = requests.post(TOKEN_URL, data=req_body)
        token_info = response.json()

    session['access_token'] = token_info['access_token']
    new_token_info = response.json()
    session['access_token'] = new_token_info['access_token']
    session['expires_at'] = datetime.now() + timedelta(
        seconds=new_token_info['expires_in'])  # The time in seconds until the access token expires

    return redirect('/playlists')


@app.route('/api_list', methods=['GET'])
def get_api_list():
    """
    This function is called when a GET request is made to the /data endpoint.
    It will be requested by the frontend to fetch the API list from the backend.
    It returns a JSON response with the data received in the query parameters.
    """
    # Fetches the API list from the actionController
    print("Received GET request")
    api_list = actionController.get_action_list()
    return jsonify(api_list), 200


@app.route('/set_api', methods=['POST'])
def post_set_api():
    print("Received POST request")
    data = request.json
    key = data['key']
    action = data['action']
    actionController.set_action(key, action)
    return jsonify({"message": "Action set successfully!"}), 200


def listen():
    app.run(host='0.0.0.0', port=8000)
