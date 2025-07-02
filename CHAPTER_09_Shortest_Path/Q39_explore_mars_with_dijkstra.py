from sys import stdin  
from heapq import heapify,heappop,heappush

T = int(stdin.readline().strip())
ans = []
import time
start = time.time()
for _ in range(T):
    N = int(stdin.readline().strip())
    graph = [list(map(int,stdin.readline().strip().split())) for _ in range(N)]
    distance = [[9*N**2+1]*N for _ in range(N)]
    h = [(graph[0][0],0,0)]
    
    while h:
        v,x,y = heappop(h)

        if distance[x][y] < v:
            continue
        distance[x][y] = v
        
        if x == N-1 and y == N-1:
            ans.append(v)
            break

        for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            if 0 <= x+dx < N and 0 <= y+dy < N:
                heappush(h,(v + graph[x+dx][y+dy],x+dx,y+dy))
                
print(*ans,sep='\n')
print(time.time() - start)

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