"""Methods for checking prompt responses"""
from requests import Response

class Checking():

    """Method for checking status code"""

    @staticmethod
    def check_status_code(responce: Response, status_code):
        assert status_code == responce.status_code
        if responce.status_code == status_code:
            print('Status code is valid: ' + str(responce.status_code))
        else:
            print('Status code is not valid: ' + str(responce.status_code))
