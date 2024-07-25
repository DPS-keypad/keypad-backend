# Serial constants
SERIAL_PORT = 'COM6'
BAUDRATE = 115200
BYTESIZE = 8
PARITY = 'N'
STOPBITS = 1
TIMEOUT = 1

# Keyboard constants
KEY1 = 'a'
KEY2 = 'b'
KEY3 = 'c'
KEY4 = 'd'
KEY5 = 'e'
KEY6 = 'f'
KEY7 = 'g'
KEY8 = 'h'
KEY9 = 'i'
POT1 = 'j'
POT2 = 'k'
POT3 = 'l'

# paths
KEYBOARD_ACTIONS_LIST_PATH = 'app/models/keyboardActionsList.json'
ALL_ACTIONS_LIST_PATH = 'app/models/allActionsList.json'

from os import environ as env


SECRET_KEY = 'your_secret_key'
DEBUG = True
