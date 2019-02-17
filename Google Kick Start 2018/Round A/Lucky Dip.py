"""
Author: Teh Run Xun
Date: 15 February 2019
.......................
The bag contains N items and the i-th item in the bag has value Vi.
The user will draw one item at random(all items have the equal probability of being chosen).
After the user draw an item, he can either keep it or "redip" by returning the
item to the bag and draw an item again.
This program will find out the expected value if the user play optimally to
maximize the value of the item that he will end the game with.
Example:
N K   #N is the number of items in the bag and K is the number of redip
4 0
1 2 3 4
Case #1: 2.5 For this case, the user cannot redip so the expected value is just
the mean (1+2+3+4)/4=2.5

3 1
1 10 1
Case #2: 6 For this case, the best strategy is to keep the item of value 10 when
the user gets it. Otherwise, redip.
The probability of getting 10 is:
P(1)+P(10)=1
p(10)=1-P(1)
     =1-P(1|1)P(1)
     =1-(2/3)*(2/3)
     =5/9
Therefore, the expected value=(5/9*10)+(4/9*1)=6
"""

def lucky_dip(N,K):
    #When K=0, we will just accept the first item and so the expected value is the mean
    K=int(K)
    E=[-1]*(K+1)
    x=0
    for i in range(len(N)):
        x+=int(N[i])
    x/=len(N)
    E[0]=x
    if K==0:
        return x
    #else, K==1 we will calculate the sum of the max(Vi,E[0]) for each items
    #in the bag over N {E[1] = Σmax(Vi, E[0])/N.}
    else:
        e=0
        for i in range(len(N)):
            e+=max(int(N[i]),x)
        e/=len(N)
        E[1]=e
        if K==1:
            return e
        else:
            for i in range(2,len(E)):
                if E[i]==-1:
                    e=0
                    for k in range(len(N)):
                        e+=max(int(N[k]),E[i-1])
                    e/=len(N)
                    E[i]=e
            return E[K]

no_test_case=int(input())
for i in range(no_test_case):
    x=input()
    y=input()
    x=x.split()
    y=y.split()
    print("Case #%d: %f"%(i+1,lucky_dip(y,x[1])))
    
