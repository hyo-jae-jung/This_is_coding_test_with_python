from sys import stdin  
from collections import deque

N,K = map(int,stdin.readline().strip().split())
graph = []
for _ in range(N):
    graph.append(list(map(int,stdin.readline().strip().split())))
S,X,Y = map(int,stdin.readline().strip().split())

q = []
for i in range(N):
    for j in range(N):
        if graph[i][j] > 0:
            q.append((0,graph[i][j],i,j))

q.sort()
q = deque(q)

while q:
    s,type,x,y = q.popleft()
    if s == S:
        continue
    for dx,dy in [(-1,0),(0,-1),(1,0),(0,1)]:
        if 0 <= x+dx < N and 0 <= y+dy < N:
            if graph[x+dx][y+dy] == 0:
                graph[x+dx][y+dy] = type
                q.append((s+1,type,x+dx,y+dy))

print(graph[X-1][Y-1])

'''
3 3
1 0 2
0 0 0
3 0 0
2 3 2

3 3
1 0 2
0 0 0
3 0 0
1 2 2
'''
