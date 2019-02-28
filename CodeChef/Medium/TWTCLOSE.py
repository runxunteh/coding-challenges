"""
Author: Teh Run Xun
Date: 28 February 2019
https://www.codechef.com/problems/TWTCLOSE
.......................
There are N tweets on a page.
Initially all the tweets are closed. Clicking on an open tweet closes it.
Clicking on a closed tweet opens it.
This program is to compute the total number of open tweets after each click.

Example:
N K  (N:number of tweets, K:K lines)
3 6              aList=[False,False,False]
CLICK 1   (1)    aList=[True,False,False]
CLICK 2   (2)    aList=[True,True,False]
CLICK 3   (3)    aList=[True,True,True]
CLICK 2   (2)    aList=[True,False,True]
CLOSEALL  (0)    aList=[False,False,False]
CLICK 1   (1)    aList=[True,False,False]
"""

x=input().split()
N=int(x[0])
K=int(x[1])
aList=[False]*N

for i in range(K):
    x=input().split()
    if x[0]=="CLICK":
        j=int(x[1])-1
        if aList[j]==True:
            aList[j]=False
        else:
            aList[j]=True
    elif x[0]=="CLOSEALL":
        aList=[False]*N
    print(sum(aList))
