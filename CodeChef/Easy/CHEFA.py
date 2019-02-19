"""
Author: Teh Run Xun
Date: 19 February 2019
https://www.codechef.com/problems/CHEFA
.......................
There are N piles of stones on the table.
Each turn a player can choose one pile to remove.
Each player want to maximize the total number of stones removed.
Chef takes the first turn
This program is to find the maximum number of stones that the chef can remove assuming
that both players play optimally

Sample:
N(number of piles)
3
1 2 3
Case #1: 4
Chef starts by choosing 3 then another play choose 2 then chef will choose 1
3+1=4
"""

no_test_case=int(input())
for i in range(no_test_case):
    x=int(input())
    #executes int for each input then put into a list
    y=list(map(int,input().split()))
    #sort it
    y.sort()
    #reverse it
    y=y[::-1]
    no=0
    counter=0
    while counter<len(y):
        no+=y[counter]
        counter+=2
    print(no)
    
        
    
