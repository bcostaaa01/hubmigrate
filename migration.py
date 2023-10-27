# imports
import requests
import json
from ..library.auth import Auth


class Migrate():
    """ Migrate data to HubSpot """
    def __init__(self, object_type, config, hubspot, test_access_token=None):
        self.config = config
        self.hubspot = hubspot
        self.base_path = 'https://api.hubapi.com/crm/v3/objects/'
        self.path = f"{self.base_path}/{object_type}"
        self.headers = {"Authorization": f"Bearer { test_access_token }"}
        
    def get_data(self, params):
        # get data from path with params
        response = requests.get(self.path, params, headers=self.headers)
        data = response.json()
        return data
    
    def post_data(self, data):
        # post data to path
        response = requests.post(self.path, json=data, headers=self.headers)
        return response
    
    def put_data(self, data):
        # put data to path
        response = requests.put(self.path, json=data, headers=self.headers)
        return response
    
    def delete_data(self):
        # delete data from path
        response = requests.delete(self.path, headers=self.headers)
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
    
    
# migrate = Migrate('contacts', 'config', 'hubspot')
# migrate_data = migrate.get_data('101')
# print(migrate_data)