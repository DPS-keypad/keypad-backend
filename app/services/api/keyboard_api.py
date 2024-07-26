import keyboard

# Basic clipboard operations
def cut():
    keyboard.press_and_release('ctrl+x')

def copy():
    keyboard.press_and_release('ctrl+c')

def paste():
    keyboard.press_and_release('ctrl+v')

# Undo and Redo operations
def undo():
    keyboard.press_and_release('ctrl+z')

def redo():
    keyboard.press_and_release('ctrl+y')

# Select All
def select_all():
    keyboard.press_and_release('ctrl+a')

# Save
def save():
    keyboard.press_and_release('ctrl+s')

# Open a new file
def open_file():
    keyboard.press_and_release('ctrl+o')

# Print
def print_file():
    keyboard.press_and_release('ctrl+p')

# Close window
def close_window():
    keyboard.press_and_release('alt+f4')

# Switching between applications
def switch_window():
    keyboard.press_and_release('alt+tab')

# Screenshot
def screenshot():
    keyboard.press_and_release('prtsc')

# Lock screen
def lock_screen():
    keyboard.press_and_release('win+l')

# Mute
def mute():
    keyboard.press_and_release('ctrl+shift+m')

