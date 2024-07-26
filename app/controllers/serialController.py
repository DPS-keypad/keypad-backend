import serial
import serial.tools.list_ports
import threading

from app.utils.constants import *
import app.controllers.actionController as actionController


class SerialController:
    def __init__(self, baudrate=BAUDRATE, bytesize=BYTESIZE, stopbit=STOPBITS, parity=PARITY,
                 timeout=TIMEOUT):

        # Finds the correct port to listen to
        ports = serial.tools.list_ports.comports()
        for port in ports:
            if port.description.startswith("STMicroelectronics"):
                self.port = port.device

        self.baudrate = baudrate
        self.timeout = timeout
        self.bytesize = bytesize
        self.stopbit = stopbit
        self.parity = parity

        # Initialize the serial connection
        self.ser = serial.Serial(port=self.port, baudrate=self.baudrate, bytesize=self.bytesize, stopbits=self.stopbit,
                                 parity=self.parity, timeout=self.timeout)

    def listen(self):
        # Starts the serial connection and listens for incoming data

        # Infinite loop to listen for incoming data
        print("Listening for incoming data...")
        while True:
            if self.has_received():
                received_string = self.read_string()  # read_char() if single character or read_string() if you are strings
                print(f"Received string: {received_string}")
                # Execute the action in a separate thread
                threading.Thread(target=actionController.execute_action, args=(received_string,)).start()

    def read_char(self):
        # Reads a single character from the serial port
        return self.ser.read().decode('utf-8')

    def read_string(self):
        # Reads a string from the serial port
        # Reads until a newline character is encountered or until 40 characters are read
        return self.ser.read_until(expected=b'\0', size=40).decode('utf-8').removesuffix('\0')

    def has_received(self):
        # Check if there is data available to read
        return self.ser.in_waiting > 0

