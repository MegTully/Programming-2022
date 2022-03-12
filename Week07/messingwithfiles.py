#Create a new file called count.txt 
filename= "count.txt"

#write 0 in the file
#with open(filename, "w") as f:
    #count= f.write("0")


#Write a function that reads in a number from a file that already exists
#(count.txt). test the program by calling the function and outputting the
#number.

def readfile():
    with open(filename,"r") as f:
        count = int(f.read())
        return count

def overwrite(count):
    with open(filename, "w+t") as f:
        f.write(str(count))
        

#Write a program that, uses these two functions, to count how many times
#the program has been run. Test it, check to see that the number goes up
#each time.

number = readfile()
number += 1
print(number)
overwrite(number)

