"""
Author: Teh Run Xun
Date: 2 March 2019
https://www.codechef.com/problems/DOMSOL
.......................
Domino Solitaire: a grid with two rows and N columns.
Each square in the grid contains an integer A.
This program is to place tiles to cover all the squares in the grid such that
each tile covers two squares and no pair of tiles overlap.
The score for a tile: difference between the bigger and the smaller number.
The aim is to maximize the sum of the scores of all the tiles.

Example:
N
4
8 6 2 3
9 7 1 2

Tiling 1
| 8 | 6 2 | 3 |
|   |-----|   |
| 9 | 7 1 | 2 |
(9 − 8) + (6 − 2) + (7 − 1) + (3 − 2) = 12

Solution:
We can either choose vertical tiles or horizontal
If we chose vertical tiles: row1[i]-row2[i]
If we chose horizontal tiles: we need to consider both row1 and row2 as we cant
choose vertical tiles again. row1[i]-row1[i+1] and row2[i]-row2[i+1]
Reference: https://www.codechef.com/viewsolution/21348755
"""

N=int(input())
row1=list(map(int,input().split()))
row2=list(map(int,input().split()))

#choose vertical
final=abs(row1[0]-row2[0])
#horizontal
previous=0

for i in range(1,N):
    vertical=final+abs(row1[i]-row2[i])
    horizontal=previous+abs(row1[i]-row1[i-1])+abs(row2[i]-row2[i-1])
    previous=final
    final=max(vertical,horizontal)
print(final)
