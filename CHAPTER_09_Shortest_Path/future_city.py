from sys import stdin  

N,M = map(int,stdin.readline().strip().split())

dp = [[101]*N for _ in range(N)]
for _ in range(M):
    x,y = map(int,stdin.readline().strip().split())
    dp[y-1][x-1] = 1
    dp[x-1][y-1] = 1

X,K = map(int,stdin.readline().strip().split())

for i in dp:
    print(i)

for k in range(N):
    for i in range(N):
        for j in range(N):
            if dp[k][j] + dp[i][k] < dp[i][j]:
                dp[i][j] = dp[k][j] + dp[i][k]

for i in dp:
    print(i)
    
distance = dp[0][K-1] + dp[K-1][X-1]
print(distance if distance <= 100 else -1)

"""
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

"""