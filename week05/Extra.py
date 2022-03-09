#Write a program that will read in the data for the data structure above, ie
#reads in a student’s name, then keeps reading in their modules and grades
#(until the user enters a blank module name),
#You can break this up into two parts:
#a. Just read in the module names until the user enters blank,
#b. Then read in the grade as well
#This program can just read in one student (and their module details)

Name = input("Enter student Name: ")
Module = input("Enter Module :")
Grade = str(input("Enter Grade:"))

Student = {"Name": Name, "Courses": [{"Module":Module, "Grade":Grade}, 
            ]
}

for Courses in Student["Courses"]:
    Courses["Module"].append(Module)
    while Module != "":
        Module = input("Enter Module :")
        

print("Student Name: " , Student["Name"])
print("\t",Courses["Module"], "\t:", Courses["Grade"])

