"""
Author: Teh Run Xun
Date: 21 February 2019
https://www.codechef.com/problems/ORDERS
.......................
Order of ranks(1-lowest to n-highest)
Sgt Johnny's algorithm: men, starting from the left. Step forward, go left until 
there is no superior to the left of you.
This program is to find out the order of ranks the soldier initially line up in.

Example
N (highest rank)
3 
0 1 0  (how far the i-th soldier in line must walk to the left)
Case #1: 2 1 3

5
0 1 2 0 1
Case #2: 3 2 1 5 4

8
0 1 1 3 0 2 5 2
Case #2: 7 3 4 1 8 5 2 6
"""

"""
https://www.codechef.com/viewsolution/23156310
insert the value output[i-input[i]] to output[i+1],
then delete previous value of output[i-input[i]]
Solution:
0 1 2   3 4 (index i)
1 2 3   4 5 (output array)
0 1 2 | 0 1 (input array)

3 2 1 | 5 4 (output array[index i-1],output array[3]=4) output array=[1,2,3,5,4]
    (output array[2-2]=output array[0]=1)   output array=[2,3,1,5,4]
  (output array[1-1]=output array[0]=2)     output array=[3,2,1,5,4]
"""

no_of_test=int(input())
for i in range(no_of_test):
    N=int(input())
    #executes int for each input then put into a list
    y=list(map(int,input().split()))
    output=[]
    #Initialise output array with (1 to n)
    for i in range(N):
        output.append(i+1)

    #Scan the input array from the right to left
    for i in range(N-1,-1,-1):
        #If the value is not 0, perform the observations above
        if y[i]!=0:
            output.insert(i+1,output[i-y[i]])
            del output[i-y[i]]
    for i in output:
        print(i,end=" ")
    print("")

"""
Another solution:
Reference: https://www.quora.com/What-are-the-ways-to-solve-this-spoj-problem-SPOJ-com-Problem-ORDERS
from Aman Khan, 2013
https://www.codechef.com/viewsolution/22091800
"""
"""
no_of_test=int(input())
for i in range(no_of_test):
    N=int(input())
    #executes int for each input then put into a list
    y=list(map(int,input().split()))
    output=[]
    my_dict={}
    for i in range(N):
        output.insert(i-y[i],i)
        
    for i in range(N):
        my_dict[output[i]]=i+1

    for k,v in sorted(my_dict.items()):
        print(v,end=" ")
    print("")
"""
