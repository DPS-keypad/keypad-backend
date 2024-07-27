from flask import Flask, jsonify, request
from flask_cors import CORS
import app.controllers.actionController as actionController

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:4200"}})

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
    return jsonify({"data": api_list}), 200


@app.route('/set_api', methods=['POST'])
def post_set_api():
    print("Received POST request")
    data = request.json
    key = data['key']
    action = data['action']
    actionController.set_action(key, action)
    return jsonify({"message": "Action set successfully!"}), 200


def listen():
    print("Server started")
    app.run(port=8000)
