# #guessing no.

import random

n= random.randint(1,100)
a=-1
guess=1
while(a != n):
    a = int(input("Guess a number between 1 and 100: "))
    if(a>n):
        print("choose a smaller number")
        guess=guess+1
    elif(a<n):
        print("choose a bigger number")
        guess+=1
    else:
     print(f"You Guess the number {n} in {guess} attempts")


