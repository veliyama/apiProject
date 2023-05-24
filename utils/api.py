from utils.http_methods import Http_method
"""Methods for testing Google Maps API"""
base_url = 'https://rahulshettyacademy.com'
key = '?key=qaclick123'

class Google_maps_api():

    """Method for creating new location"""

    @staticmethod
    def create_new_place():
        post_resource = '/maps/api/place/add/json'  #Post method resource
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
        print('Prompt result:' + result_post.text)
        return result_post
