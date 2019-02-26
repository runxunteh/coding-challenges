"""
Author: Teh Run Xun
Date: 18 February 2019
https://www.codechef.com/problems/HS08TEST
.......................
Pooja would like to withdraw X $US from an ATM.
Conditions:
1) X is a multiple of 5
2) Pooja's account balance has enough cash
3) For each successful withdrawal, the bank charges 0.50 $US
This program is to calculate Pooja's account balance after the transaction.

Example:
X   Y   (X: withdraw X $US, Y: initial account balance)
30 120.00
Case #1: 120-30-0.5=89.5

42 120.00
Case #2: 120
42 is not a multiple of 5

300 120.00
Case #3: 120
300>120, X>120

Assume the bank allows Pooja to withdraw all of his money.
E.g. 30 30.5
Output: 0.00
X+0.5<=Y
"""

X,Y=input().split()
X=int(X)
Y=float(Y)
if X%5==0 and X+0.5<=Y:
    Y=Y-X-0.5
    print("%.2f" %Y)
else:
    print("%.2f" %Y)
