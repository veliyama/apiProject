from utils.api import Google_maps_api
from requests import Response

"""Creating, updating, deleting new location"""



class Test_create_place():

    def test_create_new_place(self):

        print("Post method")
        result_post: Response = Google_maps_api.create_new_place()