
# keypad-backend

This is a Flask application that interfaces with a microcontroller STM32F401CEU6 via UART and executes specific functionalities based on received commands.

## Project Structure

- **app/models**: Contains the database resources, so the list of available commands and the chosen command for every keyboard key.
- **app/views**: Contains the route definitions for the flask application.
- **app/controllers**: Contains interfaces for actions, flask server and serial communication.
- **app/services**: Contains the business logic for the apis, flask server.
- **app/utils/constants.py**: Constants for the Flask application, serial communication, keyboard keys and miscellaneous.
- **requirements.txt**: List of Python dependencies.

## Execution flow
The main.py file is the entry point for the application. It initializes the Flask application and the serial communication.
The Flask application is run on the localhost (main thread) and the serial communication (on a separated thread) is established with the microcontroller.
The microcontroller sends the key pressed to the application, which is then processed by the serial controller to execute the corresponding command (on another thread).
