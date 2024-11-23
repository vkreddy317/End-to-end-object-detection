import os  # Provides functions to interact with the operating system
from pathlib import Path  # Simplifies file path operations
import logging  # Used for tracking events during execution

# Configuring logging to show messages with timestamps and a specific format
logging.basicConfig(level=logging.INFO, format="[%(asctime)s]: %(message)s:")

# Name of the project; will be used as the base for creating subdirectories and files
project_name = "signLanguage"

# List of all files and directories to be created for the project
list_of_files = [
    "data/.gitkeep",  # Placeholder file to keep 'data' directory in version control
    f"{project_name}/__init__.py",  # Makes the project directory a Python package
    f"{project_name}/components/__init__.py",  # Initializes the 'components' package
    f"{project_name}/components/data_ingestion.py",  # Script for data ingestion
    f"{project_name}/components/data_validation.py",  # Script for validating data
    f"{project_name}/components/model_trainer.py",  # Script for model training
    f"{project_name}/components/model_pusher.py",  # Script for deploying models
    f"{project_name}/configuration/__init__.py",  # Initializes 'configuration' package
    f"{project_name}/configuration/s3_operations.py",  # Handles S3-related operations
    f"{project_name}/constant/__init__.py",  # Initializes 'constant' package
    f"{project_name}/constant/training_pipeline/__init__.py",  # Subpackage for pipeline constants
    f"{project_name}/constant/application.py",  # Application constants
    f"{project_name}/entity/__init__.py",  # Initializes 'entity' package
    f"{project_name}/entity/artifacts_entity.py",  # Defines artifact entities
    f"{project_name}/entity/config_entity.py",  # Defines configuration entities
    f"{project_name}/exception/__init__.py",  # Initializes 'exception' package
    f"{project_name}/logger/__init__.py",  # Initializes 'logger' package
    f"{project_name}/pipeline/__init__.py",  # Initializes 'pipeline' package
    f"{project_name}/pipeline/training_pipeline.py",  # Script for training pipeline
    f"{project_name}/utils/__init__.py",  # Initializes 'utils' package
    f"{project_name}/utils/main_utils.py",  # Utility functions
    "template/index.html",  # HTML template for web application
    ".dockerignore",  # File to specify which files Docker should ignore
    "app.py",  # Main entry point for the application
    "Dockerfile",  # Instructions to build a Docker image
    "requirements.txt",  # List of dependencies for the project
    "setup.py",  # Script to package the project
]

# Loop through the list of files to create the necessary directories and files
for filepath in list_of_files:
    filepath = Path(filepath)  # Convert string to a Path object for easier manipulation

    # Split the path into directory (filedir) and filename
    filedir, filename = os.path.split(filepath)

    # If the directory part is not empty, create the directory
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)  # Create directories if they don't exist
        logging.info(f"Creating directory: {filedir} for the file {filename}")

    # If the file doesn't exist or is empty, create an empty file
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass  # Create an empty file
        logging.info(f"Creating empty file: {filename}")

    else:
        # If the file already exists, log that information
        logging.info(f"{filename} is already created")
