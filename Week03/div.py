#This program takes in 2 numbers and divides the first by the second and returns the answer and the remainder
#Author: Megan Tully

num1= int(input("Enter first number: "))
num2 = int(input("Enter the number you want to divide by: "))
Answer = num1//num2
Remainder = num1%num2

print("{} divided by {} is equal to {} with remainder {}" .format(num1,num2,Answer,Remainder))