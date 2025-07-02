from sys import stdin
from heapq import heapify,heappop,heappush

N,M = map(int,stdin.readline().strip().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a,b = map(int,stdin.readline().strip().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False]*(N+1)
distance = [N+1]*(N+1)
distance[1] = 0
h = list(zip(distance,range(N+1)))
heapify(h)

while h:
    dist,vertex = heappop(h)
    if visited[vertex]:
        continue
    visited[vertex] = True
    for vertex2 in graph[vertex]:
        distance[vertex2] = min(distance[vertex2],dist + 1)
        heappush(h,(distance[vertex2],vertex2))

m = max(distance[1:])
print(distance.index(m),m,distance.count(m))

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