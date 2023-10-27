class Validate:
    def __init__(self, data):
        self.data = data

    def validate(self):
        """ Validate data """
        if self.data == "valid":
            return True
        else:
            return False