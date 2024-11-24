import sys
from signLanguage.logger import logging
from signLanguage.exception import SignException

# logging.info("Welcome to the project")


def divide_numbers(a, b):
    try:
        # Attempt division
        result = a / b
        return result
    except Exception as e:
        # Raise a custom exception with detailed error information
        raise SignException(e, sys)


# Test the custom exception
try:
    divide_numbers(10, 0)  # This will cause a ZeroDivisionError
except SignException as se:
    print(str(se))  # Print the detailed error message
