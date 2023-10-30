import unittest
from unittest.mock import Mock, patch
from hubmigrate.client import MigrationClient
from ..classes.auth import Auth
import json

class TestMigrateContact(unittest.TestCase):

    @patch('hubmigrate.client.MigrationClient.migrate_contact', return_value=Mock(status_code=200))
    @patch('hubmigrate.classes.auth.Auth.get_token', return_value=Auth.get_token())
    def test_migrate_contact(self, mock_auth, mock_post):
        # Create a test contact
        path = '../classes/sample_contact.json'
        with open(path) as f:
            test_contact = json.load(f)

        # Create an instance of the MigrationClient class
        client = MigrationClient('config', 'hubspot')

        # Call the migrate_contact method
        result = client.migrate_contact({'properties': test_contact})

        # Assertions
        self.assertEqual(result.status_code, 200)
        mock_auth.assert_called_once()  # Ensure that Auth.get_token was called once
        mock_post.assert_called_once()  # Ensure that migrate_contact was called once

if __name__ == '__main__':
    unittest.main()