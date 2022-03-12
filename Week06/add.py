
Student =[] #creates an array called Student

def readModules():
 return []
def add(Student):
    currentStudent = {}# creates an empty dict
    currentStudent["name"]=input("enter name :") # assigns the key, "name", to the value, entered by user
    currentStudent["modules"]= readModules() #assigns modules from the readModules function as values for module key
    Student.append(currentStudent) # adds this CurrentStudent to the array Student

#test
add(Student)
add(Student)
print (Student)