#This program stores a student name and a list of their courses and
#grades in a dict, it then prints out her data.

Student = {"Name": "Mary", "Courses": [{"CourseName":"Programming", "Grade":45}, 
            {"CourseName": "History", "Grade":99}]
}

print("Student Name: " , Student["Name"])

for Courses in Student["Courses"]:
    print("\t",Courses["CourseName"], "\t:", Courses["Grade"])