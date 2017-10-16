#initializes menu for console

def menuRun():
	print("""Select a choice from the options below:
	A) Add a sibling.
	B) Add a parent.
	C) Update current member.
	D) Exit application.""")
	userChoice = input("Enter here: ")
	while True:
		if userChoice.rstrip().upper() == "A":
			print ("User has selected A. Adding sibling. \n")
		elif  userChoice.rstrip().upper() == "B":
			print("User has selected B. Adding parent. \n")
		elif userChoice.rstrip().upper() == "C":
			print("Deleting member... \n")
		elif userChoice.rstrip().upper() == "D":
			print("Exiting Menu... \n")
			break
		else:
			print("Invalid selection. Please make a choice from one of the menu options.\n")
		print("""Select a choice from the options below:
		  A) Add a sibling.
		  B) Add a parent.
		  C) Delete member.
		  D) Cancel member selection
		  E) Exit application. \n""")
		userChoice = input("Enter here:  ")


if __name__ == "__main__":
	menuRun()
