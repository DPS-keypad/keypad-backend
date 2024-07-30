import keyboard


def run():
    keyboard.press_and_release('ctrl+F5')


def debug():
    keyboard.press_and_release('F5')


def stop():
    keyboard.press_and_release('shift+F5')


def stepOver():
    keyboard.press_and_release('F10')


def stepInto():
    keyboard.press_and_release('F11')


def stepOut():
    keyboard.press_and_release('shift+F11')


def newTerminal():
    keyboard.press_and_release('ctrl+shift+ò')
