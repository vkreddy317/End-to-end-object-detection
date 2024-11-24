import sys  # Provides access to exception details using `sys.exc_info()`


def error_message_detail(error, error_detail: sys):
    """
    Generate a detailed error message with the script name, line number, and error description.

    :param error: The exception object.
    :param error_detail: A reference to the `sys` module to extract exception details.
    :return: A formatted string containing detailed error information.
    """
    # Extract exception traceback details
    _, _, exc_tb = error_detail.exc_info()  # `exc_tb` holds the traceback object

    # Get the filename where the exception occurred
    file_name = exc_tb.tb_frame.f_code.co_filename

    # Format the error message with the filename, line number, and error message
    error_message = "Error occurred python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )

    return error_message  # Return the detailed error message


class SignException(Exception):
    """
    A custom exception class for detailed error handling.

    Inherits from Python's built-in `Exception` class.
    """

    def __init__(self, error_message, error_detail):
        """
        Initialize the custom exception with a detailed error message.

        :param error_message: The original error message (string format).
        :param error_detail: A reference to the `sys` module to extract exception details.
        """
        # Call the base class constructor with the error message
        super().__init__(error_message)

        # Generate a detailed error message using the helper function
        self.error_message = error_message_detail(
            error_message, error_detail=error_detail
        )

    def __str__(self):
        """
        Return the detailed error message as the string representation of the exception.

        :return: The detailed error message.
        """
        return self.error_message
