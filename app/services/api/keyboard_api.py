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


def number1():
    keyboard.press_and_release('1')


def number2():
    keyboard.press_and_release('2')


def number3():
    keyboard.press_and_release('3')


def number4():
    keyboard.press_and_release('4')


def number5():
    keyboard.press_and_release('5')


def number6():
    keyboard.press_and_release('6')


def number7():
    keyboard.press_and_release('7')


def number8():
    keyboard.press_and_release('8')


def number9():
    keyboard.press_and_release('9')
