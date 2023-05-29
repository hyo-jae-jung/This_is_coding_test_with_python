from sys import stdin 
from collections import deque

n,m = map(int,stdin.readline().strip().split())
start = int(stdin.readline().strip())
INF = int(1e9)
chart = [[0]*(n+1) for _ in range(n+1)]
graph = [deque() for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int,stdin.readline().strip().split())
    chart[a][b]=c
    graph[a].append(b)

visited = [False]*(n+1)
distence = [INF]*(n+1)
distence[start] = 0
queue = deque([start])

while queue:
    present = queue.pop()
    if not visited[present]:
        visited[present] = True
        next = graph[present]
        for i in next:
            if distence[i] > chart[present][i]+distence[present]:
                distence[i] = chart[present][i]+distence[present]
        
            if not visited[i]:
                queue.append(i)

print(distence)
