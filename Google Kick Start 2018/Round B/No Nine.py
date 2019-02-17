"""
Author: Teh Run Xun
Date: 17 February 2019
.......................
No Nine is a counting game where only legal numbers are allowed to say
A number is legal if and only if all the following are true:
-A natural number
-Does not contain the digit 9 anywhere in its base 10 representation
-Not divisible by 9
Example:
Legal number: 16 and 17
Not legal number: 18,19,17.2 and -17
Alice wonders how many turns were in the game in total and she remembers
the first number F, and the last number L.

Input:
16 26   #Case #1: 9
The game lasted for 9 turns and the numbers are:
16,17,20,21,22,23,24,25,26

88 102   #Case #2: 4
The game lasted for 4 turns and the numbers are:
88,100,101,102
"""

def no_nine(F,L):
    F=int(F)
    L=int(L)
    count=0
    for i in range(F,L+1):
        if "9" not in str(i) and i%9!=0:
            count+=1
    return count

no_test_case=int(input())
for i in range(no_test_case):
    x=input()
    x=x.split()
    print("Case #%d: %d"%(i+1,no_nine(x[0],x[1])))
