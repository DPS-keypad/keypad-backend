# this script is used to execute actions on the PC
import os

""" 
def volume(volume_value):

    # Set the volume to the specified value
    # TODO: Implement the volume setting functionality
    print(f"Volume set to {volume_value}%.")
"""



import ctypes

# Define constants
VOLUME_MIN = 0
VOLUME_MAX = 65535

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

    # Calculate the volume value based on the percentage
    volume_value = int(VOLUME_MIN + (VOLUME_MAX - VOLUME_MIN) * (volume_percentage / 100.0))

    print(volume_value)

    # Set the system volume using SendMessageW
    user32.SendMessageW(0xFFFF, 0x319, 0, (0xA0000 | (volume_value & 0xFFFF)))
















def brightness(brightness_value):
    # Set the brightness to the specified value
    # TODO: Implement the brightness setting functionality
    print(f"Brightness set to {brightness_value}%.")
