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

graph = [[] for _ in range(N+1)]
time = [0]*(N+1)
indegree = [0]*(N+1)
for i in range(1,N+1):
    t = list(map(int,stdin.readline().strip().split()))
    l = len(t)
    indegree[i] = l - 2
    time[i]+=t[0]
    for j in range(1,l-1):
        graph[t[j]].append(i)

print(time)
print(indegree)
print(graph)
ans = time.copy()

from collections import deque

q = deque()
for i in range(1,N+1):
    if indegree[i] == 0:
        q.append(i)

min_time = 0
while q:
    n = q.popleft()
    
    for i in graph[n]:
        ans[i] = max(ans[i],ans[n]+time[i])
        print(ans)
        indegree[i]-=1
        if indegree[i] == 0:
            q.append(i)

print(*ans,sep='\n')
