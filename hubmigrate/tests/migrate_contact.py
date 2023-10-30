import unittest
from unittest.mock import Mock, patch
from hubmigrate.client import MigrationClient
from ..classes.auth import Auth
import json
import os

class TestMigrateContact(unittest.TestCase):

    @patch('hubmigrate.client.MigrationClient.migrate_contact', return_value=Mock(status_code=200))
    @patch('hubmigrate.classes.auth.Auth.get_token', return_value=Auth.get_token())
    def test_migrate_contact(self, mock_auth, mock_post):
        # Create a test contact
        # Get the path to the current directory of your test script
        current_dir = os.path.dirname(os.path.realpath(__file__))

        # Define the relative path to your JSON file from the current directory
        relative_path = 'sample_contact.json'  # Replace with the actual JSON file name

        # Construct the full file path
        json_file_path = os.path.join(current_dir, relative_path)
        
        path = json_file_path
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