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
        self.id = uuid.uuid4().hex
        self.familyId = None
        self.belongsTo = []
        belongsTo.append(self.familyId)

    def updateBasicInformation(key, newValue):
        self.basicInformation[key] = newValue;

    def getFullName():
        return self.basicInformation['firstName'] + self.basicInformation['lastName']

    def getId():
        return self.id

    def getFamilyId():
        return self.familyId

    def addFamilyId(fid):
        self.familyId = fid
