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

parent = list(map(int,range(N+1)))
ans = 0
max_edge = 0
h = []

for _ in range(M):
    A,B,C = map(int,stdin.readline().strip().split())
    heappush(h,(C,A,B))

while h:
    c,a,b = heappop(h)
    if parent_find(parent,a) != parent_find(parent,b):
        parent_union(parent,a,b)
        ans+=c
        max_edge = max(max_edge,c)

print(ans - max_edge)

'''
7 12
1 2 3
1 3 2
3 2 1
2 5 2
3 4 4
7 3 6
5 1 5
1 6 2
6 4 1
6 5 3
4 5 3
6 7 4
'''
