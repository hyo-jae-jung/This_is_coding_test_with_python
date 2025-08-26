from sys import stdin  

N,M = map(int,stdin.readline().strip().split())
coins = [int(stdin.readline().strip()) for _ in range(N)]

dp = [0] + [float('inf')]*M # 최소 개수를 찾는 문제니까 inf 값을 초기값으로 세팅
for coin in coins: 
    for i in range(coin,M+1): # coin 개수를 마음대로 사용해도 되니까 코인 별로 가능한 모든 시점을 순회
        dp[i] = min(dp[i],dp[i-coin] + 1) # 0을 제외한 값에 inf로 초기값을 세팅했기 때문에 연산이 최적화 됨.

print(dp[M] if dp[M] != float('inf') else -1)
