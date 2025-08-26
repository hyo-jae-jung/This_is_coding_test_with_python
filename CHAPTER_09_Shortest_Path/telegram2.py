from sys import stdin  
from heapq import heappop,heappush

N,M,C = map(int,stdin.readline().strip().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    X,Y,Z = map(int,stdin.readline().strip().split())
    graph[X].append((Y,Z))

distance = [float('inf')]*(N+1)
distance[C] = 0
q = [(0,C)]

while q:
    d,v = heappop(q)
    for v2,d2 in graph[v]:
        if distance[v2] > d+d2:
            distance[v2] = d+d2
            heappush(q,(distance[v2],v2))

cnt = -1
time = 0
for i in distance[1:]:
    if i != float('inf'):
        cnt+=1
        time = max(time,i)

print(cnt,time)
