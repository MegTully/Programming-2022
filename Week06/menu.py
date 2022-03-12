

def displayMenu():
    #prints out the options to choose from
 print("What would you like to do?")
 print("\t(a) Add new student")
 print("\t(v) View students")
 print("\t(q) Quit")

 choice = input("Type one letter (a/v/q):").strip() #Asks user to enter their choice

 return choice

def add():
 # Insert add() function here 
    print("add")
def View():
 # Insert View() function here 
    print("view")

choice = displayMenu()

while choice != "q":
 
    if choice == "a":
        add()
    elif choice == "v":
        View()
    elif choice !="q":
        print("\n\nplease select either a,v or q")
choice=displayMenu() 