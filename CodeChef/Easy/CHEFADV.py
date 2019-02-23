"""
Author: Teh Run Xun
Date: 23 February 2019
https://www.codechef.com/problems/CHEFADV
.......................
Chef wants to move all materials from Discuss to Discourse.
Chef will only have access to Discourse if his knowledge and power become exactly
equal to N and M respectively. Initially, power and knowledge equal to 1.
Chef can perform certain actions to improve his skills.
-Solve a problem-increase his knowledge by X
-Do a push-up-increase his power by Y
-Install sharechat(can only use once)-increase both knowledge and power by 1
This program is to find out whether it is possible to move from Discuss to Discourse.

Example:
Note: X and Y is initially equal to 1
N M X Y
2 2 1 2
Case #1: Chefirnemo
install sharechat so both knowledge and power plus 1

11 10 5 9
Case #2: Chefirnemo
add X=5 twice, add Y=9 once
1+10=11, 1+9=10

11 11 5 9
Case #3: Pofik
impossible to reach M=11

12 11 5 9
Case #4: Chefirnemo
add X=5 twice, add X=9 once, install sharechat once
1+10+1=12, 1+9+1=11

From the example case above, we can observe that.
https://discuss.codechef.com/questions/134977/chefadv-editorial
Case #1 and Case #4:
(n-2)%x and (m-2)%y should equal to 0
n and m should be more than 1 

Case #2:
(n-1)%x and (m-1)%y should equal to 0
And of course N and M can be 1 so we don't have to perform any actions.
"""

no_of_test=int(input())
for i in range(no_of_test):
    k=list(map(int,input().split()))
    n=k[0]
    m=k[1]
    x=k[2]
    y=k[3]

    if (n-1)%x==0 and (m-1)%y==0:
        print("Chefirnemo")
    elif (n-2)%x==0 and (m-2)%y==0 and n>1 and m>1:
        print("Chefirnemo")
    else:
        print ("Pofik")
