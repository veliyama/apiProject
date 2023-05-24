import requests
from utils import logger
from utils.logger import Logger
import allure

"""Http methods list"""


class Http_method:
    headers = {'Content-Type': 'application/json'}
    cookie = ''

    @staticmethod
    def get(url):
        with allure.step("GET"):
            Logger.add_request(url, method='get')
            result = requests.get(url, headers=Http_method.headers, cookies=Http_method.cookie)
            Logger.add_response(result)
            return result

    @staticmethod
    def post(url, body):
        with allure.step("POST"):
            Logger.add_request(url, method='post')
            result = requests.post(url, json=body, headers=Http_method.headers, cookies=Http_method.cookie)
            Logger.add_response(result)
            return result

    @staticmethod
    def put(url, body):
        with allure.step("PUT"):
            Logger.add_request(url, method='put')
            result = requests.put(url, json=body, headers=Http_method.headers, cookies=Http_method.cookie)
            Logger.add_response(result)
            return result

    @staticmethod
    def delete(url, body):
        with allure.step("DELETE"):
            Logger.add_request(url, method='delete')
            result = requests.delete(url, json=body, headers=Http_method.headers, cookies=Http_method.cookie)
            Logger.add_response(result)
            return result
