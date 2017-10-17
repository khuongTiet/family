from member import *

FamilyTree = []

relations = {
    'self': 0
    'father': 1,
    'mother': 2,
    'brother': 3,
    'sister': 4,
    'uncle': 5,
    'aunt': 6,
    'cousin': 7
}

Family = {
    'members': [],
    'id': 0
}

def RegisterFamily():
    user = Member(firstName, lastName)
    members.append(user)
    Family = {'members': members, 'id': fid}
    print(Family['members'][0])

def addMember(fname, lname, relation):
    user = Member(fname, lname)
    if relations[relation] < 5:
        Family.members.append(user)
