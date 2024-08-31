from .classes.migration import Migrate
from .classes.association import Association

class MigrationClient:
    def __init__(self, config, hubspot):
        self.migrate = Migrate(dict, config, hubspot)
        self.associate = Association(dict, config, hubspot)


    # Migrate contacts
    def migrate_contact(self, data):
        """ Migrate contact to HubSpot 
        
        Arguments:
            data {dict} -- Data to migrate to HubSpot
        """
        return self.migrate.post_data(data, 'contacts')
    
    def update_contact(self, data, contact_id):
        """ Update contact in HubSpot 
        
        Areguments:
            data {dict} -- Data to update in HubSpot
            contact_id {str} -- ID of the contact to update
        """
        return self.migrate.put_data(data, contact_id, 'contacts')
    
    def delete_contact(self, contact_id):
        """ Delete contact in HubSpot 
        
        Arguments:
            contact_id {str} -- ID of the contact to delete
        """
        return self.migrate.delete_data(contact_id, 'contacts')
    
    
    # Migrate companies
    def migrate_company(self, data, data_type):
        """ Migrate company to HubSpot 
        
        Arguments:
            data {dict} -- Data to migrate to HubSpot
        """
        return self.migrate.post_data(data, 'companies', data_type)
    
    def update_company(self, data, company_id):
        """ Update company in HubSpot 
        
        Areguments:
            data {dict} -- Data to update in HubSpot
            company_id {str} -- ID of the company to update
        """
        return self.migrate.put_data(data, company_id, 'companies')
    
    def delete_company(self, company_id):
        """ Delete company in HubSpot 
        
        Arguments:
            company_id {str} -- ID of the company to delete
        """
        return self.migrate.delete_data(company_id, 'companies')
    
    
    # Associate records
    def associate_records(self, object1_id, object2_id, definition_id):
        """ Associate two records in HubSpot by their IDs 
        
        Arguments:
            object1_id {str} -- ID of the first object -> example: company ID
            object2_id {str} -- ID of the second object -> example: contact ID
            definition_id {str} -- ID of the definition for the type of record association -> example: 2 for company to contact
        """
        return Association.associate_records(object1_id, object2_id, definition_id)