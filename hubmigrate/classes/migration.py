import requests
from .auth import Auth


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
        """ Get data from path 
        
        Arguments:
            params {dict} -- Parameters to pass to path
        """
        response = requests.get(self.path, params, headers=self.headers)
        data = response.json()
        if response.status_code in self.status_codes:
            print(f"Successfully retrieved data from {self.path} 🪃")
            return data
        else:
            print(f"Error retrieving data from {self.path} ❌")
        return data
    
    
    def post_data(self, data, path):
        """ Post data to path 
        
        Arguments:
            data {dict} -- Data to post to path
        """
        url = f"{self.base_path}/{path}"
        response = requests.post(url, json=data, headers=self.headers)
        if response.status_code in self.status_codes:
            print(f"Successfully posted data to {url} 🎉")
        else:
            print(f"Error posting data to {url}: {response.status_code} - {response.text} ❌")  
        return response
    
    
    def patch_data(self, data, path, id=None):
        """ Patch data to path 
        
        Arguments:
            data {dict} -- Data to patch to path
            id {str} -- ID of the data to patch
        """
        url = f"{path}/{id}"
        response = requests.patch(url, json=data, headers=self.headers)
        if response.status_code in self.status_codes:
            print(f"Successfully put data to {url} 🎉")
        else:
            print(f"Error putting data to {url} with ID: {id}: {response.status_code} - {response.text} ❌")
        return response
    
    
    def delete_data(self, path, id=None):
        """ Delete data from path 
        
        Arguments:
            id {str} -- ID of the data to delete
        """
        url = f"{path}/{id}"
        response = requests.delete(url, headers=self.headers)
        if response.status_code in self.status_codes:
            print(f"Successfully deleted data from {url} with ID: {id} 🎉")
        else:
            print(f"Error deleting data from {url} with ID: {id}: {response.status_code} - {response.text} ❌")
        return response
    
    
    def get_all_data(self, path, params):
        """ Get all data from a path with params 
        
        Arguments:
            path {str} -- Path to get data from
            params {dict} -- Parameters to pass to path
        """
        data = []
        has_more = True
        while has_more:
            response = requests.get(path, params=params)
            data.extend(response.json())
            params['offset'] = response.json()['offset']
            has_more = response.json()['hasMore']
        return data