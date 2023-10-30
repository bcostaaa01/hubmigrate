from ..classes.migration import Migrate
from ..classes.auth import Auth
from unittest.mock import patch


client = Migrate('contacts', 'config', 'hubspot')

def test_get_data():
    # Create a test contact
    response = client.get_data({'limit': 1})
    
    assert response['results'][0]['properties'] is not None