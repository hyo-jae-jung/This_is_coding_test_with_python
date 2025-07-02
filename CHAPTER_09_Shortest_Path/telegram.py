from sys import stdin   
from heapq import heapify,heappop,heappush

N,M,C = map(int,stdin.readline().strip().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    X,Y,Z = map(int,stdin.readline().strip().split())
    graph[X].append((Y,Z))

visited = [False]*(N+1)
distance = [N*Z+1]*(N+1)
distance[C] = 0
h = list(zip(distance,range(N+1)))
heapify(h)

while h:
    d,v = heappop(h)
    if visited[v]:
        continue
    visited[v] = True
    for v2,d2 in graph[v]:
        distance[v2] = min(distance[v2],distance[v] + d2)
        heappush(h,(distance[v2],v2))

cnt = 0
t = 0
for i in distance[1:]:
    if i > 0:
        cnt+=1
        t = max(t,i)

print(cnt,t)

"""
3 2 1
1 2 4
1 3 2
"""