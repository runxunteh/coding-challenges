"""
Author: Teh Run Xun
Date: 22 February 2019
Problem from: https://www.codechef.com/problems/ICPC16B
.......................
An array a is called beautiful if for every pair of numbers ai, aj, (i ≠ j),
there exists an ak such that ak = ai * aj. k can be equal to i or j too.
This program is to find out whether the given array a is beautiful or not
Example:
2
0 1
Case #1: yes. 0 * 1 = 0 and a0=0

2
1 2
Case #2: yes. 1 * 2 = 2 and a1=2

2
5 6
Case #3: no. 5 * 6 = 30.

We need to accept negative values too. From this, we can observe that we need
to keep track the number of negative ones(-1's), number of ones(1's) and zeros(0's)
There are three conditions when the array will not be beautiful:
1. when the number of other values(values other than -1,0,1) is more than 1
e.g. 4 1 1 0 is fine but 4 1 2 0 is not
2. when the number of other values is 1 and number of negative ones is more than 0
e.g. 4 -1 1 0. we will get 4*-1=-4 but we want positive 4 to be beautiful
3. when the number of negative ones are more than 1 and number of positive
ones and zeros is 0
e.g. -1 -1. -1*-1=1. 
"""

no_of_test=int(input())
for i in range(no_of_test):
    x=int(input())
    y=list(map(int,input().split()))
    n=0
    one_zero=0
    others=0
    for i in range(x):
        if y[i]==0 or y[i]==1:
            one_zero+=1
        elif y[i]==-1:
            n+=1
        else:
            others+=1
    if others>1 or (others==1 and n>0) or (n>1 and one_zero==0):
        print("no")
    else:
        print("yes")
        
