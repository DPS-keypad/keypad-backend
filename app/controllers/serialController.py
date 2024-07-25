import serial
import threading

from app.utils.constants import *
import app.controllers.actionController as actionController


class SerialController:
    def __init__(self, port=SERIAL_PORT, baudrate=BAUDRATE, bytesize=BYTESIZE, stopbit=STOPBITS, parity=PARITY,
                 timeout=TIMEOUT):
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        self.bytesize = bytesize
        self.stopbit = stopbit
        self.parity = parity

        # Initialize the serial connection
        self.ser = serial.Serial(port=self.port, baudrate=self.baudrate, bytesize=self.bytesize, stopbits=self.stopbit,
                                 parity=self.parity, timeout=self.timeout)
        self.action = actionController.ActionController()

    def listen(self):
        # Starts the serial connection and listens for incoming data
        try:
            self.ser.open()
        except serial.SerialException as e:
            print(f"Error opening serial port: {e}")
            return

        # Infinite loop to listen for incoming data
        while True:
            if self.has_received():
                pressed_key = self.read_char()  # or read_string() if you are sending strings
                # Execute the action in a separate thread
                threading.Thread(target=self.action.execute_action, args=(pressed_key,)).start()

    def read_char(self):
        # Reads a single character from the serial port
        return self.ser.read().decode('utf-8')

    def read_string(self):
        # Reads a string from the serial port
        # Reads until a newline character is encountered or until 40 characters are read
        return self.ser.read_until(expected=b'\0', size=40).decode('utf-8')

    def has_received(self):
        # Check if there is data available to read
        return self.ser.in_waiting > 0
