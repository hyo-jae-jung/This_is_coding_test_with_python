from sys import stdin  

N = int(stdin.readline().strip())
coins = list(map(int,stdin.readline().strip().split()))

dp = [1] + [0]*sum(coins)
for coin in coins:
    for i in range(len(dp)-1,-1,-1):
        if dp[i] == 1:
            dp[i+coin] = 1

for i in range(len(dp)):
    if dp[i] == 0:
        print(i)
        break

'''
5
3 2 1 1 9
'''
