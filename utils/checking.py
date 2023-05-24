"""Methods for checking prompt responses"""
from requests import Response
import json

class Checking():
    """Method for checking status code"""

    @staticmethod
    def check_status_code(responce: Response, status_code):
        assert status_code == responce.status_code
        if responce.status_code == status_code:
            print('Status code is valid: ' + str(responce.status_code))
        else:
            print('Status code is not valid: ' + str(responce.status_code))

    """Method for checking mandatory fields in the prompt response"""

    @staticmethod
    def check_json_token(responce: Response, expected_value):
        token = json.loads(responce.text)
        assert list(token) == expected_value
        print('Expected values was received!')
