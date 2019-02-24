"""
Author: Teh Run Xun
Date: 24 February 2019
https://www.codechef.com/problems/FLIPCOIN
.......................
There are N coins on the table, from 0 to N-1.
Initially, each coin is kept tails up.
We have to perform two type of operations:
1) command: 0 A B
We have to flip all coins numbered between A and B inclusive.
2) command: 1 A B
We have to answer how many coins numbered between A and B inclusive are
heads up.

Example:
N Q
4 7

1 0 3   Output: 0   Array=[F,F,F,F]   F: tails up T:heads up
0 1 2   Array=[F,T,T,F]
1 0 1   Output: 1
1 0 0   Output: 0
0 0 3   Array=[T,F,F,T]
1 0 3   Output=2
1 3 3   Output=1
"""

N,Q=map(int,input().split())
aList=[False]*N  #each coin is kept tails up initially
for i in range(Q):
    x,A,B=map(int,input().split())
    if x==0:
        #flip the coins
        for i in range(A,B+1):
            if aList[i]==True:
                aList[i]=False
            else:
                aList[i]=True
    if x==1:
        #number of coins numbered between A and B inclusive that are heads up
        print(sum(aList[A:B+1]))

"""
Another solution that uses numpy module
This solution is more elegant as we can use the unary tilde operator (~) to
flip the Boolean values
Reference: https://www.codechef.com/viewsolution/20427958
"""
"""
import numpy as np
N,Q=map(int,input().split())
A=np.zeros(N,dtype=bool)
for i in range(Q):
    x,a,b=map(int,input().split())
    if x==0:
        #~ to flip: True becomes False and False becomes True
        A[a:b+1]=~A[a:b+1]
    if x==1:
        #coins numbered between a and b inclusive are heads up (True)
        print(A[a:b+1].sum())
"""
