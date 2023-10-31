# hubmigrate 🦆

**hubmigrate** is a Python library that simplifies data migration to HubSpot.

## Installation

You can install **hubmigrate** using pip:

```bash
pip install hubmigrate
```

## Usage

### Steps

1. Import the `MigrationClient` class from the `hubmigrate.client` module.
2. Create an instance of the `MigrationClient` class with the name of the config file and the name of the HubSpot portal.
3. Import the JSON data file to migrate.
4. Call the `migrate_<object>` method on the `MigrationClient` instance with the object to migrate.

### Usage Example

```python
from hubmigrate.client import MigrationClient
import json

# Create an instance of the MigrationClient class
client = MigrationClient('config', 'hubspot')

def post_company():
    # Create a test company
    with open('hubmigrate/classes/sample_company.json') as f:
        company = json.load(f)
    
    # Migrate the company to HubSpot
    response = client.migrate_company({'properties': company})
    
post_company()
```

## 🧰 Available Methods

### ☎️ Migrate Contacts

- `migrate_contact(data)`: Migrate a contact to HubSpot.
- `update_contact(data, contact_id)`: Update a contact in HubSpot.
- `delete_contact(contact_id)`: Delete a contact in HubSpot.

### 🏭 Migrate Companies

- `migrate_company(data)`: Migrate a company to HubSpot.
- `update_company(data, company_id)`: Update a company in HubSpot.
- `delete_company(company_id)`: Delete a company in HubSpot.

### 🔗 Associate Records

- `associate_records(object1_id, object2_id, definition_id)`: Associate two records in HubSpot by their IDs. This method allows you to create associations between different types of records.

🔐 Make sure to keep your `ACCESS_TOKEN` secure when using this library. Suggestion: store your `ACCESS_TOKEN` in a `.env` file and add it to your `.gitignore` file.

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

