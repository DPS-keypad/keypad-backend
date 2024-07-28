import threading
import app.controllers.backendServerController as server
import app.controllers.serialController as serialController

serial = serialController.SerialController()

# Start the serial communication in a separate thread
threading.Thread(target=serial.listen, daemon=True).start()

# Start the Flask server in the main thread
server.listen()
