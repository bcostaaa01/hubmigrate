import argparse
import json
import pandas as pd
from hubmigrate.client import MigrationClient
from dotenv import load_dotenv
import os


load_dotenv()


def read_file(file_path, data_type):
    if data_type == 'json':
        with open(file_path, 'r') as file:
            return json.load(file)
    elif data_type == 'excel':
        if file_path.endswith('.xlsx'):
            return pd.read_excel(file_path, engine='calamine').to_dict(orient='records')
        elif file_path.endswith('.xls'):
            return pd.read_excel(file_path, engine='xlrd').to_dict(orient='records')
        else:
            raise ValueError("Unsupported Excel file format")
    elif data_type == 'csv':
        return pd.read_csv(file_path).to_dict(orient='records')
    else:
        raise ValueError("Unsupported data type")


def main():
    parser = argparse.ArgumentParser(description="Migrate data to HubSpot")
    
    parser.add_argument('object_type', choices=['contacts', 'companies'], help="Type of object to migrate")
    parser.add_argument('file_path', help="Path to the data file (JSON, Excel, or CSV)")
    parser.add_argument('data_type', choices=['json', 'excel', 'csv'], help="Type of data file")
    parser.add_argument('--config', default='config', help="Path to the config file")
    parser.add_argument('--hubspot', default='hubspot', help="HubSpot portal name")
    
    args = parser.parse_args()

    data = read_file(args.file_path, args.data_type)
    
    client = MigrationClient(args.config, args.hubspot)
    
    if args.object_type == 'contacts':
        response = client.migrate_contact(data)
    elif args.object_type == 'companies':
        print(data)
        response = client.migrate_company(data)
    
    print(response)

if __name__ == '__main__':
    main()