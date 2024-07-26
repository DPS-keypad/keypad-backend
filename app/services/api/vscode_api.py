import subprocess
import psutil

def start(file_path):
    """
    Start VS Code with the specified file.

    Args:
        file_path (str): The path to the file to open.
    """
    try:
        subprocess.run(["code", file_path], check=True)
        print("VS Code started successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to start VS Code: {e}")
    except FileNotFoundError as e:
        print(f"Visual Studio Code not found: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

def startDebug(file_path):
    """
    Start debugging in VS Code with the specified file.

    Args:
        file_path (str): The path to the file to open and debug.
    """
    try:
        subprocess.run(["code", "--wait", "--new-window", "--goto", file_path], check=True)
        print("Debug started successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to start debug: {e}")
    except FileNotFoundError as e:
        print(f"Visual Studio Code not found: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")



def stopDebug():
    """
    Terminate the Visual Studio Code process if it is running.
    """
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'] == 'Code.exe':
            try:
                proc.terminate()
                proc.wait(timeout=3)  # Wait up to 3 seconds for the process to terminate
                print("Visual Studio Code process terminated.")
            except psutil.NoSuchProcess:
                print("Visual Studio Code process not found.")
            except psutil.TimeoutExpired:
                print("Timeout expired while waiting for the process to terminate.")
            except psutil.AccessDenied:
                print("Access denied when trying to terminate the process.")
            except Exception as e:
                print(f"An error occurred: {e}")


def status():
    """
    Show the status of VS Code.
    """
    try:
        result = subprocess.run(["code", "--status"], check=True, capture_output=True, text=True)
        print("VS Code status:")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Failed to get status: {e}")
    except FileNotFoundError as e:
        print(f"Visual Studio Code not found: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")



def performance():
    """
    Show VS Code performance data.
    """
    try:
        result = subprocess.run(["code", "--performance"], check=True, capture_output=True, text=True)
        print("VS Code performance data:")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Failed to get performance data: {e}")
    except FileNotFoundError as e:
        print(f"Visual Studio Code not found: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

def verbose():
    """
    Start VS Code in verbose mode.
    """
    try:
        subprocess.run(["code", "--verbose"], check=True)
        print("VS Code started in verbose mode successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to start VS Code in verbose mode: {e}")
    except FileNotFoundError as e:
        print(f"Visual Studio Code not found: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
