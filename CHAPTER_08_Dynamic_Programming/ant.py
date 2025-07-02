from sys import stdin  

N = int(stdin.readline().strip())
storage = list(map(int,stdin.readline().strip().split()))

dp = [0]*N
dp[1] = max(storage[0],storage[1])
for i in range(2,N):
    dp[i] = max(dp[i-1],dp[i-2] + storage[i])
    print(dp)
