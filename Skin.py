class Skin:

    # skin object
    # each attribute holds an image
    def __init__(self):
        self._head = None
        self._body = None
        self._arms = None
        self._legs = None

    #setters
    def set_head(self, a):
        self._head = a

    def set_body(self, a):
        self._body = a

    def set_arms(self, a):
        self._arms = a

    def set_legs(self, a):
        self._legs = a

    #getters
    def get_head(self):
        return self._head

    def get_body(self):
        return self._body

    def get_arms(self):
        return self._arms

    def get_legs(self):
        return self._legs
