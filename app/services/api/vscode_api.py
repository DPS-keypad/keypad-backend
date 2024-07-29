import subprocess
import psutil
from app.utils.constants import *
import os

"""
def find_vscode_path():
    
    #Find the path of the Visual Studio Code executable if it's running.
    
    for process in psutil.process_iter(attrs=['pid', 'name', 'exe']):
        if process.info['name'] == 'Code.exe' or process.info['name'] == 'code':
            return process.info['exe']
    return None
"""


def find_vscode_path():
    """
    Find the path of the Visual Studio Code executable.
    """
    # Percorsi comuni di installazione
    common_paths = [
        r"C:\Program Files\Microsoft VS Code\Code.exe",
        r"C:\Users\{username}\AppData\Local\Programs\Microsoft VS Code\Code.exe".format(username=os.getlogin())
    ]

    # Verifica i percorsi comuni
    for path in common_paths:
        if os.path.exists(path):
            return path


def start(file_path):
    """
    Start VS Code with the specified file.

    Args:
        file_path (str): The path to the file to open.
    """
    vscode_path = find_vscode_path()

    if vscode_path:
        try:
            subprocess.run([vscode_path, file_path], check=True)
            print("VS Code started successfully.")
        except subprocess.CalledProcessError as e:
            print(f"\nFailed to start VS Code: {e}")
        except FileNotFoundError as e:
            print(f"\nVisual Studio Code not found: {e}")
        except Exception as e:
            print(f"\nAn error occurred: {e}")
    else:
        print("VS Code path not found")


def startDebug(file_path):
    """
    Start debugging in VS Code with the specified file.

    Args:
        file_path (str): The path to the file to open and debug.
    """
    vscode_path = find_vscode_path()

    try:
        subprocess.run([vscode_path, "--wait", "--new-window", "--goto", file_path], check=True)
        print("Debug started successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to start debug: {e}")
    except FileNotFoundError as e:
        print(f"Visual Studio Code not found: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


def stopDebug(file_path):
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


def status(file_path):
    """
    Show the status of VS Code.
    """
    vscode_path = find_vscode_path()

    try:
        result = subprocess.run([vscode_path, "--status"], check=True, capture_output=True, text=True)
        print("VS Code status:")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Failed to get status: {e}")
    except FileNotFoundError as e:
        print(f"Visual Studio Code not found: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


def performance(file_path):
    """
    Show VS Code performance data.
    """
    vscode_path = find_vscode_path()

    try:
        result = subprocess.run([vscode_path, "--performance"], check=True, capture_output=True, text=True)
        print("VS Code performance data:")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Failed to get performance data: {e}")
    except FileNotFoundError as e:
        print(f"Visual Studio Code not found: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


def verbose(file_path):
    """
    Start VS Code in verbose mode.
    """
    vscode_path = find_vscode_path()

    try:
        subprocess.run([vscode_path, "--verbose"], check=True)
        print("VS Code started in verbose mode successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to start VS Code in verbose mode: {e}")
    except FileNotFoundError as e:
        print(f"Visual Studio Code not found: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
