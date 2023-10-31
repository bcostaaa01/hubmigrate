import requests
from .auth import Auth


class Association:
    """ Associate two records in HubSpot """
    def __init__(self, config, hubspot, test_access_token=None):
        self.config = config
        self.hubspot = hubspot
        self.base_path = 'https://api.hubapi.com/crm-associations/v1/associations'
        self.headers = {"Authorization": f"Bearer { Auth.get_token() }"}
        
    
    def associate_records(cls, object1_id, object2_id, definition_id):
        """ Associate two records in HubSpot by their IDs 

        Arguments:
            object1_id {str} -- ID of the first object -> example: company ID
            object2_id {str} -- ID of the second object -> example: contact ID
            definition_id {str} -- ID of the definition for the type of record association -> example: 2 for company to contact
        """
        url = cls.base_path
        
        payload = {
            "fromObjectId": object1_id,
            "toObjectId": object2_id,
            "category": "HUBSPOT_DEFINED",
            "definitionId": definition_id
        }
        
        response = requests.put(url, json=payload, headers=cls.headers)
        
        status_codes = {200, 201, 202, 204}
        
        if response.status_code in status_codes:
            print(f"Successfully associated records {object1_id} and {object2_id} 🎉")
        else:
            print(f"Error associating records {object1_id} and {object2_id}: {response.status_code} - {response.text} ❌")
        
        return response
