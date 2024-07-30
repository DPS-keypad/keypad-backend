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
    if received_string[0] == 112:  # chr(112) = 'p'
        # it's potentiometers values
        values = [int((256 - received_string[i]) / 2.56) for i in range(1, 4)]
        action_strings = [actionService.get_action("pot" + str(i)) for i in range(1, 4)]
        # Execute the actions
        if action_strings:
            actionService.execute_action_pot(action_strings, values)
        else:
            print("No actions set for potentiometers")

    elif received_string[0] == 107:  # chr(107) = 'k'
        received_string = received_string[:-1].decode()
        action_string = actionService.get_action(received_string)
        print(f"Action for key {received_string[-1]}: {action_string}")
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
