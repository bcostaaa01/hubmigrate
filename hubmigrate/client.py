from .classes.migration import Migrate

class MigrationClient:
    def __init__(self, config, hubspot):
        self.migrate = Migrate(dict, config, hubspot)


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
    def migrate_company(self, data):
        """ Migrate company to HubSpot 
        
        Arguments:
            data {dict} -- Data to migrate to HubSpot
        """
        return self.migrate.post_data(data, 'companies')
    
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
    

