import unittest
from unittest.mock import Mock, patch
from hubmigrate.client import MigrationClient
from ..classes.auth import Auth
import pandas as pd
import os


class TestMigrateCompanyExcel(unittest.TestCase):
    @patch('hubmigrate.client.MigrationClient.migrate_company', return_value=Mock(status_code=200))
    @patch('hubmigrate.classes.auth.Auth.get_token')
    def test_migrate_company(self, mock_auth, mock_post):
        # Create a test company
        # Get the path to the current directory of your test script
        current_dir = os.path.dirname(os.path.realpath(__file__))

        # Define the relative path to your JSON file from the current directory
        relative_path = '../sample_company.xlsx'

        # Construct the full file path
        excel_file_path = os.path.join(current_dir, relative_path)
        path = excel_file_path
        with open(path) as f:
            test_company = pd.read_excel(f)

        # Create an instance of the MigrationClient class
        client = MigrationClient('config', 'hubspot')

        # Call the migrate_company method
        result = client.migrate_company({'properties': test_company}, 'excel')

        # Assertions
        self.assertEqual(result.status_code, 200)