from ..classes.migration import Migrate
from ..classes.auth import Auth
from unittest.mock import patch

def test_get_data():
    # Mock the Auth.get_token() method to return a mock access token
    test_access_token = Auth.get_token()
    
    # Initialize the Migrate object and use the mock access token
    migrate = Migrate('contacts', 'config', 'hubspot', test_access_token)
    
    # Simulate a GET request with the mock access token
    data = migrate.get_data('101')
    
    # Find the contact with firstname 'Bruno' in the 'results' list
    bruno_tester_contact = next(
        (contact for contact in data['results'] if contact['properties']['firstname'] == 'Bruno'),
        None
    )

    # Add an assertion to check the result based on your test case
    assert bruno_tester_contact is not None
    assert bruno_tester_contact['properties']['firstname'] == 'Bruno'
    assert bruno_tester_contact['properties']['lastname'] == 'Tester'
