from collections import deque


class Skin:

    # each attribute holds an image
    def __init__(self):
        self.body = None
        self.head = None
        self.shirt = None
        self.pants = None

    # setters
    def set_head(self, a):
        self.head = a

    def set_body(self, a):
        self.body = a

    def set_shirt(self, a):
        self.shirt = a

    def set_pants(self, a):
        self.pants = a

    # getters
    def get_head(self):
        return self.head

    def get_body(self):
        return self.body

    def get_shirt(self):
        return self.shirt

    def get_pants(self):
        return self.pants

