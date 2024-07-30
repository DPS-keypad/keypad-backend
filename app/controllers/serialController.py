import serial
import serial.tools.list_ports
import threading
import datetime
import app.services.api.spotify_api as spotify_api

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
                # Infinite loop to wait for the response from the microcontroller
                print("Waiting for response from the microcontroller...")
                while True:
                    if self.has_received():
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
        # check if the serial port is still open and reconnect if necessary
        # (caso in cui il keypad viene staccato durante l'esecuzione)
        while True:
            if self.has_received():
                received_string = self.read_string()
                # Execute the action in a separate thread
                threading.Thread(target=actionController.execute_action, args=(received_string,), daemon=True).start()

            # Check if the spotify song has changed: if so, send it through the serial
            if spotify_api.song_has_changed():
                new_song = spotify_api.get_song()
                print(f"New song: {new_song}")
                try:
                    self.send_song(new_song)
                except:
                    pass

    def read_string(self):
        # Reads a string from the serial port
        # Reads until a newline character is encountered or until 40 characters are read
        try:
            return self.ser.read(5)
        except serial.SerialException:
            pass

    def has_received(self):
        # Check if there is data available to read
        try:
            return self.ser.in_waiting > 0
        except serial.SerialException:
            print("Serial port closed, reconnecting...")
            return False

    def send_song(self, new_song):

        # The string to send must be long 44 characters: the first 22 are the song name, the last 22 the artist
        # The object song is an array with 2 elements: the song name and the song artist
        # If the song name or the artist are longer than 22 characters, only the first 22 characters are sent,
        # if they are shorter, the remaining characters are filled with spaces

        if len(new_song[0]) > 21:
            # get only the first 22 characters
            song_name = new_song[0][:22]
        else:
            # fill the remaining characters with spaces
            song_name = new_song[0].ljust(22)

        if len(new_song[1]) > 21:
            song_artist = new_song[1][:22]
        else:
            song_artist = new_song[1].ljust(22)

        song = song_name + song_artist
        self.ser.write(song.encode('utf-8'))
