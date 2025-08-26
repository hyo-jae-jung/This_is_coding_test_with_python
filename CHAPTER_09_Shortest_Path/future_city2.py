from sys import stdin  
from heapq import heapify,heappop,heappush

N,M = map(int,stdin.readline().strip().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a,b = map(int,stdin.readline().strip().split())
    graph[a].append(b)
    graph[b].append(a)

X,K = map(int,stdin.readline().strip().split())

def dijkstra(graph,start,end):

    visited = [False]*(N+1)
    distance = [float('inf')]*(N+1)
    distance[start] = 0

    q = list(zip(distance,range(N+1)))
    heapify(q)

    while q:
        d,v = heappop(q)
        if visited[v]:
            continue
        visited[v] = True
        for v2 in graph[v]:
            distance[v2] = min(d + 1,distance[v2])
            heappush(q,(distance[v2],v2))

    if distance[end] != float('inf'):
        return distance[end]
    return -1

a = dijkstra(graph,1,K)
b = dijkstra(graph,K,X)
if a != -1 and b != -1:
    print(a+b)
else:
    print(-1)

'''
5 7
1 2
1 3
1 4
2 4
3 4
3 5
4 5
4 5


4 2
1 3
2 4
3 4
'''