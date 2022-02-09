#This program chooses a random fruit from the given list of fruits
#Author: Megan Tully

import random

fruits = ["apple", "mango", "pineapple","Grapes","Strawberry","Lemon"]

#We want a random number between 0 and the number of fruits -1
index = random.randint(0,len(fruits)-1)

#Selects the fruit in the position that was chosen by index 
fruit= fruits[index]
print("A Random Fruit: {}".format(fruit))