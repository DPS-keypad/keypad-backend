# This service links the actionController to APIs

import importlib
import json
import threading
from app.utils.constants import *

# Lock to prevent concurrent access to files
file_lock = threading.Lock()


class ActionService:
    def __init__(self):
        self.pot_values = [0, 0, 0]

    def execute_action_key(self, action_string):
        """
        This function will execute the action corresponding to the action_string string.
        """
        # the first part of the action_string is the API name, and the rest is the specific function to call in that API
        api_string, function_string = action_string.split('_')
        # import the API file
        api = importlib.import_module(f'app.services.api.{api_string}_api')
        # get the function to call
        function = getattr(api, function_string)
        # call the function, execute the action
        function()

    def get_action(self, key):
        """
        This function will return the action corresponding to the key pressed on the keypad.
        """
        with file_lock:
            keyboard_actions = json.load(open(KEYBOARD_ACTIONS_LIST_PATH))
            if key in keyboard_actions:
                return keyboard_actions[key]
            return None

    def get_action_list(self):
        """
        This function will return all the actions available in the system.
        """
        with file_lock:
            return json.load(open(ALL_ACTIONS_LIST_PATH))

    def set_action(self, key, action):
        """
        This function will set the action corresponding to the key pressed on the keypad
        """
        with file_lock:
            keyboard_actions = json.load(open(KEYBOARD_ACTIONS_LIST_PATH))
            if key in keyboard_actions:
                keyboard_actions[key] = action
                with open(KEYBOARD_ACTIONS_LIST_PATH, 'w') as file:
                    file.write(json.dumps(keyboard_actions))

    def execute_action_pot(self, action_strings, values):
        """
        This function will execute the action corresponding to the potentiometers values.
        """
        for index in range(3):
            # The value is a character of 8 bits, so must be first converted into integer
            # for example the character 'a' is 97 in ASCII, so the value is 97.
            int_value = ord(values[index])
            if int_value != self.pot_values[index] and action_strings[index]:
                # Update the value of the potentiometer
                self.pot_values[index] = int_value
                # Execute the action
                # The first part of the action_string is the API name, and the rest is the specific function to call in that API
                api_string, function_string = action_strings[index].split('_')
                # import the API file
                api = importlib.import_module(f'app.services.api.{api_string}_api')  # import the API file
                # get the function to call
                function = getattr(api, function_string)
                # call the function, execute the action
                print(int_value)
                function(int_value)
