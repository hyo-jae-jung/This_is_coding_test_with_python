from sys import stdin  

N,M = map(int,stdin.readline().strip().split())
dp = [[0]*N for _ in range(N)]
for _ in range(M):
    A,B = map(int,stdin.readline().strip().split())
    dp[A-1][B-1] = 1
    dp[B-1][A-1] = -1

for k in range(N):
    for i in range(N):
        for j in range(N):
            if dp[i][k] == 1 and dp[k][j] == 1:
                dp[i][j] = 1
            elif dp[i][k] == -1 and dp[k][j] == -1:
                dp[i][j] = -1

ans = 0
for i in range(N):
    for j in range(N):
        if i != j and dp[i][j] == 0:
            break
    else:
        ans+=1

print(ans)

'''
6 6
1 5
3 4
4 2
4 6
5 2
5 4
'''
