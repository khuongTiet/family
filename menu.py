#initializes menu for console

def menuRun():
	print("""Select a choice from the options below:
	A) Add a sibling.
	B) Add a parent.
	C) Cancel member selction.
	D) Delete selected member.
	E) Exit menu. \n""")
	userChoice = input("Enter here: ")
	while True:
		if userChoice.rstrip().upper() == "A":
			print ("User has selected A. Adding sibling. \n")
		elif  userChoice.rstrip().upper() == "B":
			print("User has selected B. Adding parent. \n")
		elif userChoice.rstrip().upper() == "C":
			print("Canceling selection... \n")
		elif userChoice.rstrip().upper() == "D":
			print("Deleting member...\n")
		elif userChoice.rstrip().upper() == "E":
			print("Exiting Menu... \n")
			break
		else:
			print("Invalid selection. Please make a choice from one of the menu options.")
		print("""Select a choice from the options below:
		  A) Add a sibling.
		  B) Add a parent.
		  C) Delete member.
		  D) Cancel member selection
		  E) Exit application. \n""")
		userChoice = input("Enter here:  \n")


if __name__ == "__main__":
	menuRun()
