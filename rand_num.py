#python program to generate a random number btw 20 & 30 guess the random number generated, try only 3 times
import random

x = random.randrange(10, 30)

guess = int(input("Enter number generated: "))


for i in range(2):
    if guess == x:
        print("Correrct!!!")
    else:
        guess = int(input("Try again: "))


        
print("The correct number is " + str(x))
