from member import *
import uuid

# FamilyTree = []
# relations = {
#     'self': 0,
#     'father': 1,
#     'mother': 2,
#     'brother': 3,
#     'sister': 4,
#     'uncle': 5,
#     'aunt': 6,
#     'cousin': 7
# }

People = {}

def RegisterFamily():
    addMember("", "", True)

    # user = Member(firstName, lastName)
    # FamilyTree.append({'members': [], 'id': uuid.uuid4().hex})
    # FamilyTree[relations['self']]['members'].append(user)

# For each of these functions, connect them to the menu
# For adding yourself, just call addMember("", "", True)

def addMember(fname, lname, isSelf):
    user = Member(fname, lname)
    People[user.id] = user
    if isSelf:
        return user.id

def deleteMember(uid):
    del People[uid]
    # Remove from relations

def updateMember(uid, nkey, nvalue):
    People[uid].updateBasicInformation(nkey, nvalue)

def relateParent(child, Parent):
    child.parents.append(Parent.id)
    Parent.children.append(child.id)

def printMembers():
    for x in People.items():
        print(x)
