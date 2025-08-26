from sys import stdin  

N = int(stdin.readline().strip())
storage = list(map(int,stdin.readline().strip().split()))

dp = [0]*N
for i in range(N):
    dp[i] = max(dp[i-2] if i>=2 else 0,dp[i-3] if i>=3 else 0) + storage[i]

print(max(dp))
