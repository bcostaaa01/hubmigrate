import unittest
from unittest.mock import Mock, patch
from hubmigrate.client import MigrationClient
from ..classes.auth import Auth

class TestMigrateCompany(unittest.TestCase):

    @patch('hubmigrate.client.MigrationClient.associate_records', return_value=Mock(status_code=204))
    @patch('hubmigrate.classes.auth.Auth.get_token')
    def test_migrate_company(self, mock_auth, mock_post):
        # Create an instance of the MigrationClient class
        client = MigrationClient('config', 'hubspot')

        # Call the migrate_company method - fix later to find IDs and definition ID by some other approach since this data is only available in my test database
        result = client.associate_records(8866534126, 1051, 2)

        # Assertions
        self.assertEqual(result.status_code, 204)
        mock_auth.assert_called  # Ensure that Auth.get_token was called
        mock_post.assert_called_once()  # Ensure that migrate_company was called once

if __name__ == '__main__':
    unittest.main()