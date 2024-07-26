# this script is used to execute actions on the PC
from app.utils.constants import *
import screen_brightness_control as sbc
import ctypes
import time
""" 
def volume(volume_value):

    # Set the volume to the specified value
    # TODO: Implement the volume setting functionality
    print(f"Volume set to {volume_value}%.")
"""


# Load the user32.dll library
user32 = ctypes.windll.user32


# Function to set the system volume
def volume(volume_percentage):
    if volume_percentage is None:
        raise ValueError("Volume percentage must be provided")

    # Ensure the volume percentage is within the range [0, 100]
    try:
        volume_percentage = int(volume_percentage)
    except ValueError:
        raise ValueError("Volume percentage must be an integer")

    if volume_percentage < 0:
        volume_percentage = 0
    elif volume_percentage > 99:
        volume_percentage = 100

    # Calculate the volume value based on the percentage
    volume_value = int(VOLUME_MIN + (VOLUME_MAX - VOLUME_MIN) * (volume_percentage / 100.0))

    print(volume_value)

    # Set the system volume using SendMessageW
    user32.SendMessageW(0xFFFF, 0x319, 0, (0xA0000 | (volume_value & 0xFFFF)))


def brightness(brightness_value):
    if brightness_value is None:
        raise ValueError("Brightness value must be provided")

    # Ensure the brightness value is within the range [0, 100]
    try:
        brightness_value = int(brightness_value)
    except ValueError:
        raise ValueError("Brightness value must be an integer")

    if brightness_value < 0:
        brightness_value = 0
    elif brightness_value > 99:
        brightness_value = 100

    # Set the brightness to the specified value
    sbc.set_brightness(brightness_value)
    print(f"Brightness set to {brightness_value}%.")


""" 
def brightness(brightness_value):
    # Set the brightness to the specified value
    # TODO: Implement the brightness setting functionality
    print(f"Brightness set to {brightness_value}%.")
"""



# Global variables to keep track of the previous scroll values
previous_scroll_value_x = 0
previous_scroll_value_y = 0

# Load user32.dll
user32 = ctypes.WinDLL('user32', use_last_error=True)

def scrollX(scroll_amount):
    global previous_scroll_value_x

    if scroll_amount is None:
        raise ValueError("Scroll amount must be provided")

    # Ensure the scroll amount is an integer and within the valid range
    try:
        scroll_amount = int(scroll_amount)
    except ValueError:
        raise ValueError("Scroll amount must be an integer")

    if scroll_amount < 0:
        scroll_amount = 0
    elif scroll_amount > 99:
        scroll_amount = 99

    # Calculate the number of scroll clicks needed based on the percentage (0-99)
    total_scroll_clicks = 100  # This is an arbitrary number; you may need to adjust it
    current_scroll_clicks = int((scroll_amount / 99) * total_scroll_clicks)
    previous_scroll_clicks = int((previous_scroll_value_x / 99) * total_scroll_clicks)

    # Determine the direction and amount to scroll
    scroll_diff = current_scroll_clicks - previous_scroll_clicks

    if scroll_diff > 0:
        for _ in range(scroll_diff):
            ctypes.windll.user32.mouse_event(MOUSEEVENTF_HWHEEL, 0, 0, 120, 0)  # Positive value for right
            time.sleep(0.01)  # Small delay to allow the scroll to register
        direction = "right"
    elif scroll_diff < 0:
        for _ in range(-scroll_diff):
            ctypes.windll.user32.mouse_event(MOUSEEVENTF_HWHEEL, 0, 0, -120, 0)  # Negative value for left
            time.sleep(0.01)  # Small delay to allow the scroll to register
        direction = "left"
    else:
        direction = "no change"

    # Update the previous scroll value
    previous_scroll_value_x = scroll_amount

    print(f"Scrolled {abs(scroll_diff)} clicks {direction} (scroll amount: {scroll_amount}).")


def scrollY(scroll_amount):
    global previous_scroll_value_y

    if scroll_amount is None:
        raise ValueError("Scroll amount must be provided")

    # Ensure the scroll amount is an integer and within the valid range
    try:
        scroll_amount = int(scroll_amount)
    except ValueError:
        raise ValueError("Scroll amount must be an integer")

    if scroll_amount < 0:
        scroll_amount = 0
    elif scroll_amount > 99:
        scroll_amount = 99

    # Calculate the number of scroll clicks needed based on the percentage (0-99)
    total_scroll_clicks = 100  # This is an arbitrary number; you may need to adjust it
    current_scroll_clicks = int((scroll_amount / 99) * total_scroll_clicks)
    previous_scroll_clicks = int((previous_scroll_value_y / 99) * total_scroll_clicks)

    # Determine the direction and amount to scroll
    scroll_diff = current_scroll_clicks - previous_scroll_clicks

    if scroll_diff > 0:
        for _ in range(scroll_diff):
            ctypes.windll.user32.mouse_event(MOUSEEVENTF_WHEEL, 0, 0, 120, 0)  # Positive value for up
            time.sleep(0.01)  # Small delay to allow the scroll to register
        direction = "up"
    elif scroll_diff < 0:
        for _ in range(-scroll_diff):
            ctypes.windll.user32.mouse_event(MOUSEEVENTF_WHEEL, 0, 0, -120, 0)  # Negative value for down
            time.sleep(0.01)  # Small delay to allow the scroll to register
        direction = "down"
    else:
        direction = "no change"

    # Update the previous scroll value
    previous_scroll_value_y = scroll_amount

    print(f"Scrolled {abs(scroll_diff)} clicks {direction} (scroll amount: {scroll_amount}).")


