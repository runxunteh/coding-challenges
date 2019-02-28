"""
Author: Teh Run Xun
Date: 27 February 2019
https://www.codechef.com/problems/CHEFARRB
.......................
Chef has an array A consisting of N integers.
A sub-array of the array is good if the bitwise OR of all the elements in it
is greater or equal than number K.
This program is to find out how many sub-arrays of array A are good.
Bitwise OR: takes two bit patterns of equal length and performs the logical
            inclusive OR operation on each pair of corresponding bits.
            0101 4+3=7
            0011
            0111  The result in each position is 0 if both bits are 0,
                  otherwise 1.

Example:
N K
3 3
1 2 3
Case #1: 4 ({3},{1,2},{2,3},{1,2,3})
Subarray: {1},{2},{3},{1,2},{2,3},{1,2,3}

3 6
3 4 5
Case #2: 2 ({3,4},{3,4,5})
Subarray: {3},{4},{5},{3,4},{4,5},{3,4,5}

4 5
5 6 4 3
Case #3:  8 ({5},{6},{5,6},{6,4},{4,3},{5,6,4},{6,4,3},{5,6,4,3})
Subarray: {5},{6},{4},{3},{5,6},{6,4},{4,3},{5,6,4},{6,4,3},{5,6,4,3}

Solution: using two pointers i and j
e.g. 5 6 4 3
i=5 and j loop will run the sum OR {5,6} then {5,6,4} then {5,6,4,3}
"""

no_of_test=int(input())
for i in range(no_of_test):
    N,K=map(int,input().split())
    A=list(map(int,input().split()))
    x=0
    output=0
    for i in range(N):
        x=A[i]
        if x>=K:
            output+=1
        for j in range(i+1,N):
            x=x|A[j]   #|: bitwise OR
            if x>=K:
                output+=1
    print(output)
