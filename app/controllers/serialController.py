import serial
import serial.tools.list_ports
import threading
import datetime
#import app.services.api.spotify_api as spotify_api

from app.utils.constants import *
import app.controllers.actionController as actionController


class SerialController:
    def __init__(self, baudrate=BAUDRATE, bytesize=BYTESIZE, stopbit=STOPBITS, parity=PARITY,
                 timeout=TIMEOUT):
        self.port = None
        while self.port is None:
            # Finds the correct port to listen to
            ports = serial.tools.list_ports.comports()
            for port in ports:
                # print(port.description)
                if port.description.startswith("USB"):
                    self.port = port.device

        self.baudrate = baudrate
        self.timeout = timeout
        self.bytesize = bytesize
        self.stopbit = stopbit
        self.parity = parity

        # Wait for the port to be ready
        while True:
            try:
                # Initialize the serial connection
                self.ser = serial.Serial(port=self.port, baudrate=self.baudrate, bytesize=self.bytesize,
                                         stopbits=self.stopbit, parity=self.parity, timeout=self.timeout)
                # Send the current time on serial port
                self.ser.write(str(datetime.datetime.now().time())[0:5].encode('utf-8') + b'\0')
                print("Sent the current time on serial port")
                # Wait for the response from the microcontroller
                print("Waiting for response from the microcontroller...")
                while True:
                    if self.ser.in_waiting > 0:
                        start_bytes = self.ser.read(2)
                        if start_bytes == b'p\0':
                            print("Response received from the microcontroller")
                            print("Serial communication established")
                            break
                break
            except serial.SerialException:
                pass

    def listen(self):
        # Infinite loop to listen for incoming data
        print("Listening for incoming data...")
        while True:
            if self.has_received():
                received_string = self.read_string()
                # Execute the action in a separate thread
                threading.Thread(target=actionController.execute_action, args=(received_string,), daemon=True).start()
            # TODO: check if the serial port is still open and reconnect if necessary (caso in cui il keypad viene staccato durante l'esecuzione)

    def read_string(self):
        # Reads a string from the serial port
        # Reads until a newline character is encountered or until 40 characters are read
        return self.ser.read(5)

    def has_received(self):
        # Check if there is data available to read
        return self.ser.in_waiting > 0
