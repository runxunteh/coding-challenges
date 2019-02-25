"""
Author: Teh Run Xun
Date: 25 February 2019
https://www.codechef.com/problems/ICPC16F
.......................
Chef wants to construct a bipartite graph with n vertices each, on the two parts,
and with total number of edges equal to m.
The vertices on both left and right are numbered from 1 to n.
The degree of each vertex must be greater than or equal to d, less than or
equal to D.
Given 4 integers, n,m,d,D. We have to help Chef to construct bipartite graph
that satisfy the property. If no such graph exists, output -1.

Degree of vertices: number of edges which has another vertex as an endpoint
Bipartite graph: a graph in which the vertices can be put into two separate
                 groups so that the only edges are between those two groups,
                 and no edges between vertices within the same group.
                 Note: No odd-length cycles

Example:
n m d D
2 3 1 2
Case #1:
u v  (u: vertex on the left part) (v: vertex on the right part)
1 1
2 2
1 2

Due to the constraint where the degree of every vertex>=d, <=D.
We will generate in such order:
Example: 3 9 1 3
first loop (to ensure every vertext is >=1)
V1 --- V1   counter=1
V2 --- V2
V3 --- V3   l==n so we reset to 1 and, increase counter and set r=counter.
            counter=2
second
V1 --- V2   
V2 --- V3   r==n so we reset to 1 
V3 --- V1   l==n so we reset to 1 and, increase counter and set r=counter.
            counter=3
third
V1 --- V3   r==n so we reset to 1
V2 --- V1
V3 --- V2
Reference: https://www.codechef.com/viewsolution/21156197
"""
no_of_test=int(input())
for i in range(no_of_test):
    aList=list(map(int,input().split()))
    n=aList[0]
    m=aList[1]
    d=aList[2]
    D=aList[3]
    output=[]
    l=1         #both left and right part will start with vertex 1
    r=1
    counter=1   #counter that act as the loop counter (+1 after a full loop l==n)

    if n*d<=m<=n*D:
        for i in range(m):
            output.append(l)
            output.append(r)
            l+=1   
            r+=1
            """
            when left part reaches the n vertex, we reset left to 1 and 
            increase counter by 1 and set right part to start with the counter
            """
            if l==n+1:
                l=1
                counter+=1
                r=counter
            #if the right part reaches the n vertex, simply reset to 1
            if r==n+1:
                r=1
        #print out output
        for i in range(0,len(output),2):
            print(output[i],output[i+1])
    #not exist any bipartite graph
    else:
        print("-1")
   

