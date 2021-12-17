from collections import deque


class Skin:

    # each attribute holds an image
    def __init__(self):
        self.body = None
        self.head = None
        self.arms = None
        self.legs = None

    # setters
    def set_head(self, a):
        self.head = a

    def set_body(self, a):
        self.body = a

    def set_arms(self, a):
        self.arms = a

    def set_legs(self, a):
        self.legs = a

    # getters
    def get_head(self):
        return self.head

    def get_body(self):
        return self.body

    def get_arms(self):
        return self.arms

    def get_legs(self):
        return self.legs

    #Skin = property(get_body(), get_head(), get_arms(), get_legs())
    #body = property(body(), set_body())
    #head = property(get_head(), set_head())
