import os
from dotenv import load_dotenv


load_dotenv()


class Auth:
    """ Authenticate with HubSpot """
    @staticmethod
    def get_token():
        # Get the HubSpot private app token from environment variables
        access_token = os.environ.get('ACCESS_TOKEN')
        print(access_token)
        if not access_token:
            raise ValueError("ACCESS_TOKEN not found. Declare it as envvar or define a default value.")
        return access_token
    

Auth.get_token()