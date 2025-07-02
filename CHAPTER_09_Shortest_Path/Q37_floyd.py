from sys import stdin  

n = int(stdin.readline().strip())
m = int(stdin.readline().strip())

dp = [[100000*n+1]*n for _ in range(n)]

for _ in range(m):
    a,b,c = map(int,stdin.readline().strip().split())
    dp[a-1][b-1] = min(c,dp[a-1][b-1])

for k in range(n):
    for i in range(n):
        for j in range(n):
            if dp[k][j-1] + dp[i-1][k] < dp[i-1][j-1]:
                dp[i-1][j-1] = dp[k][j-1] + dp[i-1][k]

for i in range(n):
    for j in range(n):
        if i == j or dp[i][j] == 100000*n+1:
            dp[i][j] = 0
        
for i in dp:
    print(*i)

'''
5
14
1 2 2
1 3 3
1 4 1
1 5 10
2 4 2
3 4 1
3 5 1
4 5 3
3 5 10
3 1 8
1 4 2
5 1 7
3 4 2
5 2 4
'''