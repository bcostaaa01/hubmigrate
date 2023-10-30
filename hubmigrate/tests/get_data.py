from hubmigrate.client import MigrationClient
from ..classes.auth import Auth
from unittest.mock import patch


client = MigrationClient('config', 'hubspot')

# comment due to lack of get_data method in client.py - will be available soon
# def test_get_data():
#     # Create a test contact
#     response = client
    
#     assert response['results'][0]['properties'] is not None