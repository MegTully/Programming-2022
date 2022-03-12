
def displayMenu():
    #prints out the options to choose from
 print("What would you like to do?")
 print("\t(a) Add new student")
 print("\t(v) View students")
 print("\t(q) Quit")

 choice = input("Type one letter (a/v/q):").strip() #Asks user to enter their choice

 return choice

Student =[] #creates an array called Student

def readModules():
    Modules = [] #create an array called Modules
    ModuleName = input("\t Enter the first module name or enter blank to quit :").strip()

    while ModuleName != "": #while the module entered is not blank proceed this loop
        Module = {}         #creates an empty dict
        Module["name"]= ModuleName #assigns the key, "name", the value input by user as ModuleName

    Module["grade"]=int(input("\t\tEnter grade:")) #assigns the grade a user inputs to the key, "grade"
    Modules.append(Module)                         #adds the Modules with the grade to the Modules array

# Next module to be added
    ModuleName = input("\tEnter next module name or enter blank to quit:").strip()

    return Modules

def add(Student):
    currentStudent = {}# creates an empty dict
    currentStudent["name"]=input("enter name :") # assigns the key, "name", to the value, entered by user
    currentStudent["modules"]= readModules() #assigns modules from the readModules function as values for module key
    Student.append(currentStudent) # adds this CurrentStudent to the array Student


#adef View():


choice = displayMenu()

while choice != "q":
 
    if choice == "a":
        add(Student)
    elif choice == "v":
        View(Student)
    elif choice !="q":
        print("\n\nplease select either a,v or q")
choice=displayMenu() 