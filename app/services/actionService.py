# This service links the actionController to APIs

import importlib
import json
import threading
from app.utils.constants import *

# Lock to prevent concurrent access to files
file_lock = threading.Lock()


def execute_action_string(action_string):
    """
    This function will execute the action corresponding to the action_string string.
    """
    # the first part of the action_string is the API name, and the rest is the specific function to call in that API
    api_string, function_string = action_string.split('_')
    # import the API file
    api = importlib.import_module(f'app.services.api.{api_string}')
    # get the function to call
    function = getattr(api, function_string)
    # call the function, execute the action
    function()


def get_action(key):
    """
    This function will return the action corresponding to the key pressed on the keypad.
    """
    with file_lock:
        keyboard_actions = json.load(open(KEYBOARD_ACTIONS_LIST_PATH))
        if key in keyboard_actions:
            return keyboard_actions[key]
        return None


def get_action_list():
    """
    This function will return all the actions available in the system.
    """
    with file_lock:
        return json.load(open(ALL_ACTIONS_LIST_PATH))


def set_action(key, action):
    """
    This function will set the action corresponding to the key pressed on the keypad
    """
    with file_lock:
        keyboard_actions = json.load(open(KEYBOARD_ACTIONS_LIST_PATH))
        if key in keyboard_actions:
            keyboard_actions[key] = action
            with open(KEYBOARD_ACTIONS_LIST_PATH, 'w') as file:
                file.write(json.dumps(keyboard_actions))
