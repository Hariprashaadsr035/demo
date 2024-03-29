import sys
from src.logger import logging

def error_message_detail(error_message, error_detail : sys):
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_msg = f'Error has occured in \nfilename  -->  [{file_name}] \nline number  -->  [{exc_tb.tb_lineno}] \nerror  -->  [{str(error_message)}]'
    return error_msg

class CustomException(Exception):
    def __init__(self, error_message, error_detail):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail = error_detail)
    
    def __str__(self):
        return self.error_message


if __name__ == '__main__':
    try:
        a = 1/0
    except Exception as e:
        logging.info('Exception has occured')
        raise CustomException(e, sys)