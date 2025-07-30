from sys import stdin   

N,M,K,X = map(int,stdin.readline().strip().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    A,B = map(int,stdin.readline().strip().split())
    graph[A].append(B)

stack = [(X,0)]
visited = [False]*(N+1)
ans = []

while stack:
    n,d = stack.pop()

    if d == K:
        ans.append(n)
        continue

    if visited[n]:
        continue
    visited[n] = True

    for n2 in graph[n]:
        if not visited[n2]:
            stack.append((n2,d+1))

if ans:
    ans.sort()
    print(*ans,sep='\n')
else:
    print(-1)

'''
4 4 2 1
1 2
1 3
2 3
2 4

4 3 2 1
1 2
1 3
1 4

4 4 1 1
1 2
1 3
2 3
2 4
'''
