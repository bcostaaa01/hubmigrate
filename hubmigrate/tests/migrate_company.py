import unittest
from unittest.mock import Mock, patch
from hubmigrate.client import MigrationClient
from ..classes.auth import Auth
import json

class TestMigrateCompany(unittest.TestCase):

    @patch('hubmigrate.client.MigrationClient.migrate_company', return_value=Mock(status_code=200))
    @patch('hubmigrate.classes.auth.Auth.get_token', return_value=Auth.get_token())
    def test_migrate_company(self, mock_auth, mock_post):
        # Create a test company
        path = '../classes/sample_company.json'
        with open(path) as f:
            test_company = json.load(f)

        # Create an instance of the MigrationClient class
        client = MigrationClient('config', 'hubspot')

        # Call the migrate_company method
        result = client.migrate_company({'properties': test_company})

        # Assertions
        self.assertEqual(result.status_code, 200)
        mock_auth.assert_called_once()  # Ensure that Auth.get_token was called once
        mock_post.assert_called_once()  # Ensure that migrate_company was called once

if __name__ == '__main__':
    unittest.main()

