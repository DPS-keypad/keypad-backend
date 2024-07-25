from flask import Flask, jsonify, request
import actionController

app = Flask(__name__)


@app.route('/api', methods=['GET'])
def get_api_list():
    """
    This function is called when a GET request is made to the /data endpoint.
    It will be requested by the frontend to fetch the API list from the backend.
    It returns a JSON response with the data received in the query parameters.
    """
    # Fetches the API list from the actionController
    api_list = actionController.get_action_list()
    return jsonify({"data": api_list}), 200


@app.route('/data', methods=['POST'])
def data():
    data = request.json
    key = data['key']
    action = data['action']
    actionController.set_action(key, action)
    return jsonify({"message": "Action set successfully!"}), 200


def listen():
    app.run(port=8000)
