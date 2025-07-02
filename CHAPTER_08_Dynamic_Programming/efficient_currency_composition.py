from sys import stdin  

N,M = map(int,stdin.readline().strip().split())
coins = [int(stdin.readline().strip()) for _ in range(N)]

dp = [0] + [1001]*M
for i in coins:
    for j in range(i,M+1):
        dp[j] = min(dp[j],dp[j-i]+1)

print(dp[M] if dp[M] != 1001 else -1)
