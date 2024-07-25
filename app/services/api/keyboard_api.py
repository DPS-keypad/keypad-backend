import keyboard


def cut():
    keyboard.press_and_release('ctrl+x')


def copy():
    keyboard.press_and_release('ctrl+c')


def paste():
    keyboard.press_and_release('ctrl+v')
