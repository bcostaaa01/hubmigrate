# imports
import requests
from auth import Auth

class Migrate():
    """ Migrate data to HubSpot """
    def __init__(self, object_type, config, hubspot, test_access_token=None):
        self.config = config
        self.hubspot = hubspot
        self.base_path = 'https://api.hubapi.com/crm/v3/objects'
        self.path = f"{self.base_path}/{object_type}"
        self.headers = {"Authorization": f"Bearer { test_access_token if test_access_token else Auth.get_token() }"}
        
    status_codes = {
        200,
        201,
        202,
        204
    }
        
    def get_data(self, params):
        # get data from path with params
        response = requests.get(self.path, params, headers=self.headers)
        data = response.json()
        if response.status_code in self.status_codes:
            print(f"Successfully retrieved data from {self.path} 🪃")
            return data
        else:
            print(f"Error retrieving data from {self.path} ❌")
        return data
    
    def post_data(self, data):
        # post data to path
        response = requests.post(self.path, json=data, headers=self.headers)
        if response.status_code in self.status_codes:
            print(f"Successfully posted data to {self.path} 🎉")
        else:
            print(f"Error posting data to {self.path}: {response.status_code} - {response.text} ❌")  
        return response
    
    def put_data(self, data, id=None):
        # put data to path
        url = f"{self.path}/{id}"
        response = requests.patch(url, json=data, headers=self.headers)
        if response.status_code in self.status_codes:
            print(f"Successfully put data to {url} 🎉")
        else:
            print(f"Error putting data to {url} with ID: {id}: {response.status_code} - {response.text} ❌")
        return response
    
    def delete_data(self):
        # delete data from path
        response = requests.delete(self.path, headers=self.headers)
        if response.status_code in self.status_codes:
            print(f"Successfully deleted data from {self.path} 🎉")
        else:
            print(f"Error deleting data from {self.path}: {response.status_code} - {response.text} ❌")
        return response
    
    def get_all_data(self, path, params):
        # get all data from path with params
        data = []
        has_more = True
        while has_more:
            response = requests.get(path, params=params)
            data.extend(response.json())
            params['offset'] = response.json()['offset']
            has_more = response.json()['hasMore']
        return data