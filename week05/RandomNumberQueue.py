#This program adds 10 random numbers into a queue,
#then outputs all the values in the queue, 
#then deletes the number in position [0] and prints the new queue
#this continues until the queue is empty

import random

Queue = []

for num in range(0,10):
    Queue.append(random.randint(0,100))

print("Queue is ", Queue)

while len(Queue) != 0:
    FirstNum = Queue.pop(0)

    print("The current number is ", FirstNum, "and the queue is ", Queue)




