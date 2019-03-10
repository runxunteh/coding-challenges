"""
Author: Teh Run Xun
Date: 10 March 2019
https://www.dailycodingproblem.com/
...................................
There's a staircase with N steps and we can climb any number from a set of
positive integers X. e.g. X={1,3,5}, we can climb 1,3 or 5 steps at a time.
This program is to compute the number of unique ways we can climb the staircase.

Example:
N=4
N = 1: [1]
N = 2: [1, 1], [2]
N = 3: [1, 2], [1, 1, 1], [2, 1]
N = 4: [1, 1, 2], [2, 2], [1, 2, 1], [1, 1, 1, 1], [2, 1, 1]
So, to get N=3, we first have to get to N=1 then 2 steps, or N=2 then 1 step.
Therefore, f(3) = f(2) + f(1).
Now we consider taking any number of steps from the set X.
If X = {1, 3, 5}, then f(n) = f(n - 1) + f(n - 3) + f(n - 5).

Conditions to consider:
1. When N=4, X={1,3,5}. We cannot consider 5 steps as we only have 4 steps.
f(1)=f(0)
f(0)=1 <-[0]
dp[0]=1
dp=[1,0,0,0,0]
f(n) = f(n - 1) + f(n - 3) + f(n - 5)
f(4)=f(3)+f(1)+n/a
"""

def staircase(N,X):
    dp=[0]*(N+1)
    dp[0]=1
    for i in range(1,N+1):
        total=0
        for x in X: #go through all the possible steps to climb
            if N-x>=0:  #if we can climb the steps
                total+=dp[i-x]
        dp[i]=total
    return dp[N]

X=[1,3,5]
print(staircase(5,X))
