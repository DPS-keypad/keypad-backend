from flask_cors import CORS
from flask import Flask, jsonify, request, redirect, session
import app.controllers.actionController as actionController
import urllib.parse
from datetime import datetime, timedelta
import requests

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:4200"}})

app.secret_key = '53d355f8-571a-4590-a310-1f9579440851'


CLIENT_ID = 'c6e1a2e3479b4890bb1ee4e6a8d69cbe'
CLIENT_SECRET = '7b56a32a5bbc4a9aac92559d1a88b49e'
REDIRECT_URI = 'http://localhost:8000/callback'
AUTH_URL = 'https://accounts.spotify.com/authorize'
TOKEN_URL = 'https://accounts.spotify.com/api/token'
API_BASE_URL = 'https://api.spotify.com/v1/'


@app.route('/', methods=['GET'])
def index():
    return "Welcome to my Spotify APP <br> <a href='/login'>Login with Spotify</a>"



@app.route('/login', methods=['GET'])
def login():
    scope = 'user-read-private user-read-email'

    params = {
        'client_id': CLIENT_ID,
        'response_type': 'code',
        'scope': scope,
        'redirect_uri': REDIRECT_URI,
        'show_dialog': True
    }

    auth_url = f'{AUTH_URL}?{urllib.parse.urlencode(params)}'

    return redirect(auth_url)


@app.route('/callback', methods=['GET'])
def callback():
    if 'error' in request.args:
        return jsonify({"error": request.args['error']}), 400

    if 'code' in request.args:
        req_body = {
            'code': request.args['code'],
            'grant_type': 'authorization_code',
            'redirect_uri': REDIRECT_URI,
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET
        }

        response = requests.post(TOKEN_URL, data=req_body)
        token_info = response.json()

        session['access_token'] = token_info['access_token']  # Use this token to make requests to the Spotify API
        session['refresh_token'] = token_info[
            'refresh_token']  # Save this token for future use when the access token expires
        session['expires_at'] = datetime.now() + timedelta(
            seconds=token_info['expires_in'])  # The time in seconds until the access token expires

        return redirect('/playlists')

@app.route('/playlists', methods=['GET'])
def get_playlists():
    if 'access_token' not in session:
        return redirect('/spotify/login')

    if datetime.now() > session['expires_at'].replace(tzinfo=None):
        return redirect('/refresh_token')

    headers = {
        'Authorization': f'Bearer {session["access_token"]}'
    }
    response = requests.get(f'{API_BASE_URL}me/playlists', headers=headers)
    playlists = response.json()  # This is a list of playlists

    return jsonify(playlists)


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
    app.run(host='0.0.0.0', port=8000, debug=True)

