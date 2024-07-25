# this script is used to execute actions on the PC
import os


def volume(volume_value):
    # Set the volume to the specified value
    os.system(f"amixer -D pulse sset Master {volume_value}%")
    print(f"Volume set to {volume_value}%.")
