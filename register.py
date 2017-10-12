import member

FamilyTree = []
members = []
fid = 1
def RegisterFamily():
    firstName = input("Enter your first name: ")
    lastName = input("Enter your last name: ")
    user = member.Member(firstName, lastName)
    members.append(user)
    Family = {'members': members, 'id': fid}
    print(Family['members'][0])
