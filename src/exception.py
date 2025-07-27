import sys
import traceback
from src.logger import logging

class CustomException(Exception):
    def __init__(self, error_message: str, error_detail: sys):
        super().__init__(error_message)
        self.error_message = self.get_detailed_error_message(error_message, error_detail)

    @staticmethod
    def get_detailed_error_message(error_message, error_detail: sys):
        _, _, exc_tb = error_detail.exc_info()
        filename = exc_tb.tb_frame.f_code.co_filename
        line_number = exc_tb.tb_lineno
        return f"Error occurred in file: {filename}, line: {line_number}, message: {error_message}"

    def __str__(self):
        return self.error_message
    
if __name__=="__main__" :
    try:
        a=1/0
    except Exception as e :
        logging.info("divide by zero")
        raise CustomException(e,sys)  