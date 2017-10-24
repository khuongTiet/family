#initializes menu for console
from register import *
from member import *

def menuRun():

	print("""Select a choice from the options below:
	A) Add member
	B) select memBer
	C) Cancel member selection.
	D) Delete selected member.
	R) Relate members
	S) add a Sibling
	P) Print current member
	E) Exit menu. \n""")
	userChoice = input("Enter here: ")

	while True:
		if userChoice.rstrip().upper() == "A":
			print ("User has selected A. Adding sibling. \n")
			fname = input("Enter your first name: ")
			lname = input("Enter your last name: ")
			addMember(fname, lname, False)
		elif userChoice.rstrip().upper() == "B":
			print("User has selected ")
		elif userChoice.rstrip().upper() == "C":
			print("Canceling selection... \n")
		elif userChoice.rstrip().upper() == "D":
			print("Deleting member...\n")
		elif userChoice.rstrip().upper() == "P":
			printMembers()
		elif userChoice.rstrip().upper() == "R":
			child = input("Enter child's id")
			parent = input("Enter parent's id")
			relateParent(People[child], People[parent])
		elif userChoice.rstrip().upper() == "E":
			print("Exiting Menu... \n")
			break
		else:
			print("Invalid selection. Please make a choice from one of the menu options.")
		print("""Select a choice from the options below:
		 A) Add member
	 	B) Select member
	 	C) Cancel member selection.
	 	D) Delete selected member.
	 	R) Relate members
	 	S) Siblate
	 	P) Print current member
	 	E) Exit menu. \n""")
		userChoice = input("Enter here:  \n")


if __name__ == "__main__":
	menuRun()
