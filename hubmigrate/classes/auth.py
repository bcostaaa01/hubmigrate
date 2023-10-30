# import .env file
from decouple import config
import os

access_token = os.getenv('ACCESS_TOKEN')

class Auth:
    """ Authenticate with HubSpot """
    def get_token():
        # get HubSpot private app token from input
        # token = input('Enter your HubSpot private app token: ')
        # return token from .env file
        access_token = config('ACCESS_TOKEN')
        return access_token