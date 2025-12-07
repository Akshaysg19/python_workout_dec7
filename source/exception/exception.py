import sys
from source.logging import logger

class NetworkSecurityException(Exception):
    def __init__(self, error_message, error_details:sys):
        self.error_message = error_message
        _,_,err_tab = error_details.exc_info()

        self.lineno = err_tab.tb_lineno
        self.file_name = err_tab.tb_frame.f_code.co_filename

    def __str__(self):
        return f"Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
            self.file_name, self.lineno, str(self.error_message))

if __name__ == "__main__":
    try:
        logger.logging.info("Enter the try block")
        a = 1/0
        print("This will not be printed", a)
    except Exception as e:
        raise NetworkSecurityException(e, sys)
