from sys import stdin   

N = int(stdin.readline().strip())

dp = [0] + list(range(N))

for i in range(1,N+1):
    for j in [2,3]:
        dp[i] = min(dp[i], dp[i//j] + i%j + 1)


# for i in range(5,N+1):
#     dp[i] = min(dp[i], dp[i//5] + i%5 + 1)

dp2 = [0] + list(range(N))
for i in range(2,N+1):
    dp2[i] = min(dp2[i],dp2[i//2] + i%2 + 1)

for i in range(3,N+1):
    dp2[i] = min(dp2[i],dp2[i//3] + i%3 + 1)


dp3 = [0] * (N + 1)

for i in range(2, N + 1):
    dp3[i] = dp3[i - 1] + 1
    if i % 2 == 0:
        dp3[i] = min(dp3[i], dp3[i // 2] + 1)
    if i % 3 == 0:
        dp3[i] = min(dp3[i], dp3[i // 3] + 1)


print(dp)
print(dp2)
print(dp3)