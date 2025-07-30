from sys import stdin 

N,M = map(int,stdin.readline().strip().split())
arr = [list(map(int,stdin.readline().strip().split())) for _ in range(N)]

chickens = []
home = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            chickens.append((i,j))
        if arr[i][j] == 1:
            home.append((i,j))

from itertools import combinations as comb

ans = float('inf')
for chickens in comb(chickens,M):
    chickens_distance = 0
    for hi,hj in home:
        chicken_distance = float('inf')
        for ci,cj in chickens:
            chicken_distance = min(chicken_distance,abs(hi-ci)+abs(hj-cj))
        chickens_distance+=chicken_distance
    ans = min(ans,chickens_distance)

print(ans)


'''
5 3
0 0 1 0 0
0 0 2 0 1
0 1 2 0 0
0 0 1 0 0
0 0 0 0 2

5 2
0 2 0 1 0
1 0 1 0 0
0 0 0 0 0
2 0 0 1 1
2 2 0 1 2

5 1
1 2 0 0 0
1 2 0 0 0
1 2 0 0 0
1 2 0 0 0
1 2 0 0 0

5 1
1 2 0 2 1
1 2 0 2 1
1 2 0 2 1
1 2 0 2 1
1 2 0 2 1
'''