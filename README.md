<!-- Define the README for the hubmigrate module with emojis -->
# 🦆 hubmigrate

<!-- [![PyPI version](https://badge.fury.io/py/hubmigrate.svg)]
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/hubmigrate.svg)]
[![PyPI - License](https://img.shields.io/pypi/l/hubmigrate.svg)] -->

A Python library for migrating data to HubSpot.

## Installation

```bash
pip install hubmigrate
```

## Usage

### Steps

1. Import the `MigrationClient` class from the `hubmigrate.client` module.
2. Create an instance of the `MigrationClient` class with the name of the config file and the name of the HubSpot portal.
3. Import the JSON data file to migrate.
4. Call the `migrate_<object>` method on the `MigrationClient` instance with the object to migrate.

```python
from hubmigrate.client import MigrationClient
import json


client = MigrationClient('config', 'hubspot')


def post_company():
    # Create a test contact
    with open('hubmigrate/classes/sample_company.json') as f:
        company = json.load(f)
    
    # Migrate the contact to HubSpot
    response = client.migrate_company({'properties': company})
    
    
post_company()
```

<!-- ## Contributing

### Setup

### Testing

### Linting

### Building

### Publishing

## License -->

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```



