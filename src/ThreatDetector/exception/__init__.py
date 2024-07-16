import os

def error_message_detail(error, error_detail):
    """
    Generate a detailed error message for a given error and its error detail.

    Args:
        error (Exception): The error that occurred.
        error_detail (Exception): The error detail containing information about the error.

    Returns:
        str: A formatted error message with information about the error, including the name of the Python script, the line number, and the error message.
    """
    _, _, exc_tb = error_detail.exc_info()
    file_name = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    error_message = "Error occured in python script name [{0}] on line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )

    return error_message


class CustomException(Exception):
    def __init__(self, error_message, error_detail):
        """
        Initializes a new instance of the CustomException class.

        Args:
            error_message (str): The error message associated with the exception.
            error_detail (Exception): The exception detail.

        Returns:
            None
        """
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message