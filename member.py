import uuid

class Member:
    def __init__(self, fn, ln):
        self.basicInformation = {
            'firstName': fn,
            'lastName': ln,
            'sex': None,
            'age': None,
            'maritalStatus': None,
            'childrenCount': None
        }
        self.id = self.basicInformation['firstName'] + self.basicInformation['lastName']
        self.parents = []
        self.children = []

    def updateBasicInformation(key, newValue):
        self.basicInformation[key] = newValue;

    def getFullName(self):
        return self.basicInformation['firstName'] + " " + self.basicInformation['lastName']

    def __repr__(self):
        return "Member(" + self.getFullName() + ")"

    def __str__(self):
        return getFullName()
