# Import the logging module to handle log messages
import logging  # Provides built-in support for logging messages (INFO, WARNING, ERROR, etc.)

# Import the os module to interact with the file system
import os  # Used for file and directory operations (e.g., path joining, creating directories)

# Import the datetime module to add timestamps to log filenames and messages
from datetime import datetime  # Helps generate timestamps dynamically

# Import the from_root library to find the root directory of the project
from from_root import (
    from_root,
)  # Ensures logs are stored relative to the project's root folder

# Generate a unique log filename based on the current date and time
# Example: If the current date and time is 2024-11-23 at 14:30:00, the filename will be '11_23_2024_14_30_00.log'
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Define the path where log files will be stored, relative to the project's root directory
# Example: If the root directory is "/home/user/project", the log path will be "/home/user/project/log/<LOG_FILE>"
log_path = os.path.join(from_root(), "log", LOG_FILE)

# Ensure the directory for log files exists; if not, create it
# Example: If the 'log' folder doesn't exist, it will be created automatically
os.makedirs(log_path, exist_ok=True)

# Define the full file path for the current log file
# Example: "/home/user/project/log/11_23_2024_14_30_00.log"
lOG_FILE_PATH = os.path.join(log_path, LOG_FILE)

# Configure the logging system to define where and how logs are written
logging.basicConfig(
    filename=lOG_FILE_PATH,  # Specify the log file where log messages will be written
    format="[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",  # Define the log message format
    # Example message: [ 2024-11-23 14:30:00 ] root - INFO - Welcome to the project
    level=logging.INFO,  # Set the minimum log level to INFO
    # Log levels:
    # DEBUG: Detailed diagnostic information
    # INFO: General informational messages
    # WARNING: Something unexpected happened, but the program can continue
    # ERROR: A serious issue that prevented part of the program from running
    # CRITICAL: A very serious error that might cause the program to terminate
)
