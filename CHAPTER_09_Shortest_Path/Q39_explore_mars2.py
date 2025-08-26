def dijktra(n,arr):
    visited = [[float('inf')]*n for _ in range(n)]
    visited[0][0] = arr[0][0]
    q = [(visited[0][0],0,0)]
    while q:
        d,x,y = heappop(q)
        if x == n-1 and y == n-1:
            return visited[y][x]
        if visited[y][x] < d:
            continue
        for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            if 0 <= (nx:=x+dx) < n and 0 <= (ny:=y+dy) < n:
                if visited[ny][nx] > d + arr[ny][nx]:
                    visited[ny][nx] = d + arr[ny][nx]
                    heappush(q,(visited[ny][nx],nx,ny))

from sys import stdin  
from heapq import heappop,heappush

T = int(stdin.readline().strip())
ans = []
for _ in range(T):
    N = int(stdin.readline().strip())
    cost_arr = [list(map(int,stdin.readline().strip().split())) for _ in range(N)]
    ans.append(dijktra(N,cost_arr))

print(*ans,sep='\n')

'''
3
3
5 5 4
3 9 1
3 2 7
5
3 7 2 0 1
2 8 0 9 1
1 2 1 8 1
9 8 9 2 0
3 6 5 1 5
7
9 0 5 1 1 5 3
4 1 2 1 6 5 3
0 7 6 1 6 8 5
1 1 7 8 3 2 3
9 4 0 7 6 4 1
5 8 3 2 4 8 3
7 4 8 4 8 3 4
'''