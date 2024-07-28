import app.controllers.actionController as actionController
from app.utils.constants import *
from app.services.api.spotify_api import get_currently_playing_track
from datetime import datetime, timedelta
from flask_cors import CORS
from flask import Flask, jsonify, request, redirect, session
import urllib.parse
import requests

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:4200"}})
app.secret_key = '53d355f8-571a-4590-a310-1f9579440851'  # This is a secret key used to sign the session cookies

""" 
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
"""
access_token = ""
refresh_token = ""
expires_at = ""


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
def data():
    data = request.json
    key = data['key']
    action = data['action']
    actionController.set_action(key, action)
    return jsonify({"message": "Action set successfully!"}), 200


def listen():
    app.run(host='0.0.0.0', port=8000, debug=True)
