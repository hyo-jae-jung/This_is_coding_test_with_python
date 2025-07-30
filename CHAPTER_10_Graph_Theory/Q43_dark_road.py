def parent_find(parent,x):
    if parent[x] != x:
        parent[x] = parent_find(parent,parent[x])
    return parent[x]

def parent_union(parent,a,b):
    a = parent_find(parent,a)
    b = parent_find(parent,b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

from sys import stdin  
from heapq import heappop,heappush

N,M = map(int,stdin.readline().strip().split())
h = []
total_cost = 0
for _ in range(M):
    x,y,z = map(int,stdin.readline().strip().split())
    total_cost+=z
    heappush(h,(z,x,y))

parent = list(range(N))

i = 0
while h and i < N:
    z,x,y = heappop(h)
    if (x:=parent_find(parent,x)) != (y:=parent_find(parent,y)):
        total_cost-=z
        parent_union(parent,x,y)
        i+=1

print(total_cost)

'''
7 11
0 1 7
0 3 5
1 2 8
1 3 9
1 4 7
2 4 5
3 4 15
3 5 6
4 5 8
4 6 9
5 6 11
'''
