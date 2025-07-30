from sys import stdin   

N = int(stdin.readline().strip())

corridor = [stdin.readline().strip().split() for _ in range(N)]

def check(x,y,corridor):
    for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
        stack = [(x,y)]
        while stack:
            j,i = stack.pop()
            if corridor[i][j] == 'S':
                return False
            if corridor[i][j] == 'B':
                break
            if 0 <= (nx:=j+dx) < N and 0 <= (ny:=i+dy) < N:
                    stack.append((nx,ny))
    return True

X_loc = []
for i in range(N):
     for j in range(N):
          if corridor[i][j] == 'X':
               X_loc.append((i,j))

from itertools import combinations as comb
from copy import deepcopy

for BBB in comb(X_loc,3):
    sample_corr = deepcopy(corridor)
    for y,x in BBB:
        sample_corr[y][x] = 'B'

    ans = True
    for i in range(N):
        if ans:
            for j in range(N):
                if ans:
                    if sample_corr[i][j] == 'T':
                        ans = check(j,i,sample_corr)
    if ans:
        break

print('YES' if ans else 'NO')

'''
5
X S X X T
T X S X X
X X X X X
X T X X X
X X T X X

4
S S S T
X X X X
X X X X
T T T X
'''