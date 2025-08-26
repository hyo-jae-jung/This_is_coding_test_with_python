'''
6 7
3 6
4 3
3 2
1 3
1 2
2 4
5 2
'''

from sys import stdin  
from heapq import heappop,heappush

N,M = map(int,stdin.readline().strip().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    A,B = map(int,stdin.readline().strip().split())
    graph[A].append(B)
    graph[B].append(A)

distance = [float('inf')]*(N+1)
distance[1] = 0
q = [(0,1)]

while q:
    d,v = heappop(q)
    for v2 in graph[v]:
        if distance[v2] > (d2:=d+1):
            distance[v2] = d2
            heappush(q,(d2,v2))

max_idx = 0
max_val = 0
max_cnt = 0
for i,j in enumerate(distance[1:],1):
    if j > max_val:
        max_val = j
        max_idx = i
        max_cnt = 1
    elif max_val == j:
        max_cnt+=1

print(max_idx,max_val,max_cnt)
