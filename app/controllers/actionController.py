from app.services import actionService

"""
This methods will be called by the backendServerController to fetch the API list and by the serialController after
receiving commands from the keypad to execute the corresponding action.
"""

actionService = actionService.ActionService()


def execute_action(received_string):
    """
    This function will be called by the serialController to execute the corresponding action based on the command
    received from the keypad.
    """
    if received_string.startswith("p"):
        # it's potentiometers values
        # removes the first letter of the string
        values = received_string[1:]
        action_strings = [actionService.get_action("pot" + str(value)) for value in range(1, 4)]
        print(f"Actions for potentiometers values: {action_strings}")
        # Execute the actions
        if action_strings:
            actionService.execute_action_pot(action_strings, values)
        else:
            print("No action set for this potentiometer")

    elif received_string.startswith("k"):
        action_string = actionService.get_action(received_string)
        print(f"Action for key {received_string}: {action_string}")
        # Execute the action
        if action_string:
            actionService.execute_action_key(action_string)
        else:
            print("No action set for this key.")
    else:
        print(f"Invalid command received: {received_string}")


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
