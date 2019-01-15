#https://www.pythonforbeginners.com/code-snippets-source-code/python-guessing-game/

import random
x=random.randint(1,99)
guess=int(input("Enter an integer from 1 to 99: "))
count=0
while x!="guess":
    if guess < x:
        print("Higher")
        guess = int(input("Enter an integer from 1 to 99: "))
        count+=1
    elif guess > x:
        print("Lower")
        guess = int(input("Enter an integer from 1 to 99: "))
        count+=1
    else:
        print("You Got It! " + "You guess " + str(count+1) + " times.")
        break
