#https://www.pythonforbeginners.com/code-snippets-source-code/game-hangman/

import time
import requests
import random
word_site = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"

response = requests.get(word_site)
WORDS = response.content.splitlines()
word=random.choice(WORDS)
word=str(word).replace("'","")
word=str(word).replace("b","")

#welcoming the user
name = input("What is your name? ")

print ("Hello, " + name + "! Time to play hangman!")
print(" ")
#wait for 1 second
time.sleep(0.5)

print ("Start guessing...")
time.sleep(0.5)

#creates an variable with an empty value
guesses = ''

#determine the number of turns
turns = 10

#check if the turns are more than zero
while turns > 0:         
    failed = 0             
    # for every character in word    
    for char in word:      
    # see if the character is in the players guess
        if char in guesses:    
        # print then out the character
            print (char),
        else:
        # if not found, print a dash
            print ("_"),     
        # and increase the failed counter with one
            failed += 1    

    if failed == 0:        
        print ("You Won!")
        break      

    # ask the user to guess a character
    guess = input("Guess a character:") 

    # set the players guess to guesses
    guesses += guess                    

    # if the guess is not found in the word
    if guess not in word:  
     # turns counter decreases with 1
        turns -= 1        
        print ("Wrong! You have", + turns, 'more guesses') 
 
    # if the turns are equal to zero
        if turns == 0:
            print ("You Lose! The word is " + word + "!")
