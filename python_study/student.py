class Student:
    def __init__(self,name):
        self.name = name

    @classmethod
    def create(cls):
        p = cls()
        return p
