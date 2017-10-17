class Member:
    def __init__(self, fn, ln):
        self.firstName = fn
        self.lastName = ln
        self.sex = None
        self.age = None
        self.maritalStatus = None
        self.deceased = None
        self.childrenCount = 0

    def updateAge(newAge):
        self.age = newAge

    def updateMaritalStatus(newStatus):
        self.maritalStatus = newStatus

    def updateDeceased(newState):
        self.deceased = newState

    def childrenCount(newCount):
        self.childrenCount = newCount

    def getFullName():
        return self.firstName + self.lastName
    
