'''
5
10 -1
10 1 -1
4 1 -1
4 3 1 -1
3 3 -1
'''

from sys import stdin 

N = int(stdin.readline().strip())

indegree = [0] + [1]*N
node_cost = [0]*(N+1)
graph = [[] if i > 0 else list(range(1,N+1)) for i in range(N+1)]

for i in range(1,N+1):
    l = list(map(int,stdin.readline().strip().split()))
    node_cost[i] = l[0]
    for j in l[1:-1]:
        graph[j].append(i)
        indegree[i]+=1

from collections import deque  

q = deque([0])
node_total_cost = [0]*(N+1)

while q:
    idx = q.popleft()

    for i in graph[idx]:
        node_total_cost[i] = max(node_total_cost[i], node_cost[i] + node_total_cost[idx])
        indegree[i]-=1
        if indegree[i] == 0:
            q.append(i)

print(*node_total_cost[1:],sep='\n')
