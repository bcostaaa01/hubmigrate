class Auth:
    """ Authenticate with HubSpot """
    def get_token():
        # get HubSpot private app token from input
        token = input('Enter your HubSpot private app token: ')
        return token