import json

from utils.api import Google_maps_api
from requests import Response
from utils.checking import Checking

"""Creating, updating, deleting new location"""


class Test_create_place():

    def test_create_new_place(self):
        print("Post method")
        result_post: Response = Google_maps_api.create_new_place()
        check_post = result_post.json()
        place_id = check_post.get('place_id')
        Checking.check_status_code(result_post, 200)
        Checking.check_json_token(result_post, ['status', 'place_id', 'scope', 'reference', 'id'])
        Checking.check_json_values(result_post, 'status', 'OK')

        print("Get method for post method")
        result_get: Response = Google_maps_api.get_new_place(place_id)
        Checking.check_status_code(result_get, 200)
        Checking.check_json_token(result_get, ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website', 'language'])
        Checking.check_json_values(result_get, 'address', '29, side layout, cohen 09')

        print('Put method')
        result_put: Response = Google_maps_api.put_new_place(place_id)
        Checking.check_status_code(result_put, 200)
        Checking.check_json_token(result_put, ['msg'])
        Checking.check_json_values(result_put, 'msg', 'Address successfully updated')

        print("Get method for put method")
        result_get: Response = Google_maps_api.get_new_place(place_id)
        Checking.check_status_code(result_get, 200)
        Checking.check_json_token(result_get, ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website', 'language'])
        Checking.check_json_values(result_get, 'address', '100 Lenina street, RU')

        print('Delete method')
        result_delete: Response = Google_maps_api.delete_new_place(place_id)
        Checking.check_status_code(result_delete, 200)
        Checking.check_json_token(result_delete, ['status'])
        Checking.check_json_values(result_delete, 'status', 'OK')

        print("Get method for delete method")
        result_get: Response = Google_maps_api.get_new_place(place_id)
        Checking.check_status_code(result_get, 404)
        Checking.check_json_token(result_get, ['msg'])
        Checking.check_json_search_word_in_values(result_get, 'msg', 'failed')

        print('Test was successful')
