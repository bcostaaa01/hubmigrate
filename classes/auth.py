# import .env file
from decouple import config

class Auth:
    """ Authenticate with HubSpot """
    def get_token():
        access_token = config('ACCESS_TOKEN')
        return access_token