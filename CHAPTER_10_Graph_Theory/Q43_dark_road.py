def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)

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
    heappush(h,(z,x,y))
    total_cost+=z

parent = list(range(N))
use_cost = 0

while N > 1 and h:
    z,x,y = heappop(h)
    if (a:=find_parent(parent,x)) != (b:=find_parent(parent,y)):
        union_parent(parent,a,b)
        use_cost+=z
        N-=1

print(total_cost - use_cost)

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