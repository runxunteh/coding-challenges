"""
Author: Teh Run Xun
Date: 20 February 2019
https://www.codechef.com/problems/COINS
.......................
A coin n can be exchanged in a bank into three coins: n//2,n//3 and n//4
We can also sell Bytelandian coins for American dollars. Rate is 1:1
This program is to find the maximum amount of American dollars we can get.

Example:
12
Case #1: 13
We can exchange in a bank into 6,4,3. 6+4+3=13

2
Case #2: 2
If exchange in a bank: 1,0,0. So is better to just sell 2 coin for 2 dollar

However, we also need to consider after exchanging in the bank.
For example, n=998. After exchanging in the bank, 499,332,249. We need to consider
the maximum amount for each coins as well. So we need to find for 499,322,249 each
and so on
"""

my_dict={}
def coins(n):
    """
    return the value if there is such key in the dictionary
    e.g. coins(12) so our dictionary in the end will be {12: 13}
    if we run coins(24) next, when we run the coins(n//2)=coins(24//2)=coins(12)
    we can just access the value and return 13
    so later on 13+8+6=27

    if the key is not in the dictionary and we want to exchange in the bank
    the else statement will take the maximum value between n and the value of the key
    (n//2+n//3+n//4)
    e.g. coins(124). 124//2=62, 124//3=41, 124//4=31            62+41+31=134
    assume this is the first input so our dictionary is currently empty, so it will
    execute the else statement. When coins(n//2), coins(62) is called, there is no such
    key in the dictionary so it will run the checks again and execute the else statement.
    62//2=31, 62//3=20, 62//4=15
    so in the end it will have the keys with their respective value and can be accessed
    later on. Such as the value for key 31 which will be accessed during
    coins(n//4)=coins(124//4)=coins(31)
    """
    if n in my_dict:
        return my_dict[n]
    if n>=(n//2+n//3+n//4): #is better to just sell the coin than exchange in bank
        return n
    else:
        my_dict[n]=max(n,coins(n//2)+coins(n//3)+coins(n//4))
        return my_dict[n]

for i in range(10):
    x=int(input())
    print(coins(x))
