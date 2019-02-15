"""
Author: Teh Run Xun
Date: 14 February 2019
.......................
This program is to determine the minimum number of button presses
to make the calculator display an integer with no odd digits
Example:
Input: 42   Output: 0   #No odd digits
Input: 2018 Output: 2   #pressing plus button twice to display 2020

Input: 5327
First odd digit is 5. Either decrement by 1 and replace all digits behind with 8
Or increment by 1 and replace all digits behind with 0
So, either 4888 or 6000
5327-4888=439
6000-5327=673
So we choose the minimum number of button presses which is minus 439 times.
"""

def is_odd(x):
    x=int(x)
    if x%2!=0:
        return True
    return False

def plus(x,i):
    #if the first digit is 9 or all the digits to the left of 9 is 8
    #e.g. 88892 and 91112
    if int(x[i])==9:
        if i==0 or x[0:i]=="8"*i:
            new=str("20")+str("0"*(int(len(x))-1))
        else:
            new=str(x[0:i])+str(int(x[i])+1)+str("0"*int(len(x)-i-1))
    else:
        new=str(x[0:i])+str(int(x[i])+1)+str("0"*int(len(x)-i-1))
    return int(new)-int(x)

def minus(x,i):
    new=str(x[0:i])+str(int(x[i])-1)+str("8"*int(len(x)-i-1))
    return int(x)-int(new)

def even_digits(x):
    x=str(x)
    for i in range(len(x)):
        if is_odd(x[i])==True:
            y=plus(x,i)
            z=minus(x,i)
            min_button=min(y,z)
            return min_button
    return 0
"""
file=open("A-large-practice.in","r")
aList=[]
for line in file:
    line=line.strip("\n")
    aList.append(line)
no_test_case=int(aList[0])

for i in range(1,no_test_case+1):
    print("Case #%d: %d"%(i,even_digits(aList[i])))
"""
no_test_case=int(input())
for i in range(no_test_case):
    x=int(input())
    print("Case #%d: %d"%(i+1,even_digits(x)))
   
