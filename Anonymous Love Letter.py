"""
https://www.pramp.com/tryout
Given a string L representing the letter and string N representing the newspaper
Return true if L can be written entirely from N, false otherwise.
"""


def isLoveLetterReproducible(L,M):
    charMap=[0]*256
    charCount=0
    for i in range(len(L)):
        letter=ord(L[i])-97
        if charMap[letter]==0:
            charCount+=1
        charMap[letter]+=1

    for i in range(len(M)):
        letter=ord(M[i])-97
        if charMap[letter]>0:
            charMap[letter]-=1
            if charMap[letter]==0:
                charCount-=1
        if charCount==0:
            return True
    return False

L="Love you"
M="Quote of the day: Love yourself!"

print(isLoveLetterReproducible(L,M))
