from utils.http_methods import Http_method

"""Methods for testing Google Maps API"""
base_url = 'https://rahulshettyacademy.com'
key = '?key=qaclick123'


class Google_maps_api():
    """Method for creating new location"""

    @staticmethod
    def create_new_place():
        post_resource = '/maps/api/place/add/json'  # Post method resource
        json_create_new_place = {
            "location": {
                "lat": -38.383494,
                "lng": 33.427362
            }, "accuracy": 50,
            "name": "Frontline house",
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
            "types": [
                "shoe park",
                "shop"
            ],
            "website": "http://google.com",
            "language": "French-IN"
        }
        post_url = base_url + post_resource + key
        print(post_url)
        result_post = Http_method.post(post_url, json_create_new_place)
        print('Prompt result: ' + result_post.text)
        return result_post

    """Method for verifying of creation new location"""

    @staticmethod
    def get_new_place(place_id):
        get_resource = '/maps/api/place/get/json'  # Get method resource
        get_url = base_url + get_resource + key + '&place_id=' + place_id
        print(get_url)
        get_result = Http_method.get(get_url)
        print('Prompt result: ' + get_result.text)
        return get_result

    """Method for updating information of new location"""

    @staticmethod
    def put_new_place(place_id):
        put_resource = '/maps/api/place/update/json'  # put method resource
        put_url = base_url + put_resource + key + '&place_id=' + place_id
        json_for_updating_new_location = {
            "place_id": place_id,
            "address": "100 Lenina street, RU",
            "key": "qaclick123"
        }
        print(put_url)
        put_result = Http_method.put(put_url, json_for_updating_new_location)
        print('Prompt result: ' + put_result.text)
        return put_result

    @staticmethod
    def delete_new_place(place_id):
        delete_resource = '/maps/api/place/delete/json'  # delete method resource
        delete_url = base_url + delete_resource + key
        json_for_delete_new_location = {
            "place_id": place_id,
        }
        print(delete_url)
        delete_result = Http_method.delete(delete_url, json_for_delete_new_location)
        print('Prompt result: ' + delete_result.text)
        return delete_result
