from sys import stdin  

T = int(stdin.readline().strip())
ans = []
for _ in range(T):
    n,m = map(int,stdin.readline().strip().split())
    arr = list(map(int,stdin.readline().strip().split()))

    mine = []
    for j in range(m):
        tmp = []
        for i in range(n):
            tmp.append(arr[j+i*m])
        mine.append(tmp)

    dp = [[0]*n for _ in range(m+1)]

    for i in range(1,m+1):
        for j in range(n):
            dp[i][j] = mine[i-1][j] + max(dp[i-1][j],dp[i-1][j-1] if j > 0 else 0,dp[i-1][j+1] if j < n-1 else 0)

    ans.append(max(dp[-1]))

print(*ans,sep='\n')

'''
2
3 4
1 3 3 2 2 1 4 1 0 6 4 7
4 4
1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2
'''
