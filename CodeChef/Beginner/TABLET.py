"""
Author: Teh Run Xun
Date: 18 February 2019
Problem from: https://www.codechef.com/problems/TABLET
.......................
Chef decided to buy a new tablet and his budget is B.
The area of the tablet's screen should be as large as possible.
Area of rectangle=Width x Height
This program is to help chef to choose the table that he should buy with the
maximum area of screen. Or determine he can't buy any.
Example:
N B   where N is the number of tablet and B is the budget
3 6
W H P  each tablet has the information of Width, Height and Price
3 4 4
5 5 7
5 2 5
Case 1: 12
The first tablet's screen area is 3x4=12. Can't afford the second tablet.
Third tablet's screen area is just 5x2=10. So we will output the screen area of
the first tablet.
N B
2 6
3 6 8
5 4 9
Case 2: no tablet
The budget is 6 but the price for both tablet is greater than the budget.
"""

no_test_case=int(input())
for i in range(no_test_case):
    x=input().split()
    area=0
    for k in range(int(x[0])):  #Tablet's information (W,H,P)
        y=input().split()
        W=int(y[0])
        H=int(y[1])
        P=int(y[2])
        if P<=int(x[1]):    #Only compare screen area if the price is within budget
            a=W*H
            if area<a:
                area=a
    if area==0:     #No suitable tablet
        print("no tablet")
    else:
        print(area)
