from sys import stdin  

N = int(stdin.readline().strip())
soldiers = list(map(lambda x:-int(x),stdin.readline().strip().split()))

dp = [1]*N
for i in range(N):
    for j in range(i):
        if soldiers[i] > soldiers[j]:
            dp[i] = max(dp[i],dp[j]+1)

print(N - dp[-1])
