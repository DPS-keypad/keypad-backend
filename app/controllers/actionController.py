from app.services import actionService

"""
This methods will be called by the backendServerController to fetch the API list and by the serialController after
receiving commands from the keypad to execute the corresponding action.
"""


def execute_action(key):
    """
    This function will be called by the serialController to execute the corresponding action based on the command
    received from the keypad.
    """
    action_string = actionService.get_action(key)
    print(f"Action for key {key}: {action_string}")
    # Execute the action
    if action_string:
        actionService.execute_action_string(action_string)


def get_action_list():
    """
    This function will return all the actions available in the system.
    """
    return actionService.get_action_list()


def set_action(key, action):
    """
    This function will set the action corresponding to the key pressed on the keypad.
    """
    actionService.set_action(key, action)
