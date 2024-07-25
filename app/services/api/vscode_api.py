
import subprocess

def start_debug():
    """
    Avvia il debug tramite il CLI di Visual Studio Code.
    """

    file_path = "C:\\Users\\Gledi\\Documents\\my_project\\test.py:1"  # Sostituisci con il percorso file

    try:
        subprocess.run(["code", "--wait", "--new-window", "--goto", file_path], check=True)
        print("Debug started successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to start debug: {e}")
    except FileNotFoundError as e:
        print(f"Visual Studio Code not found: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
