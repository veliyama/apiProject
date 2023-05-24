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

        print("Get method for post method")
        result_get: Response = Google_maps_api.get_new_place(place_id)
        Checking.check_status_code(result_get, 200)

        print('Put method')
        result_put: Response = Google_maps_api.put_new_place(place_id)
        Checking.check_status_code(result_put, 200)

        print("Get method for put method")
        result_get: Response = Google_maps_api.get_new_place(place_id)
        Checking.check_status_code(result_get, 200)

        print('Delete method')
        result_delete: Response = Google_maps_api.delete_new_place(place_id)
        Checking.check_status_code(result_delete, 200)

        print("Get method for delete method")
        result_get: Response = Google_maps_api.get_new_place(place_id)
        Checking.check_status_code(result_get, 404)
