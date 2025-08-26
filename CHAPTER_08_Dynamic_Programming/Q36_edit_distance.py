from sys import stdin  
from collections import deque  

A = stdin.readline().strip()
B = stdin.readline().strip()

la = len(A)
lb = len(B)
dp = [[0]*(la+1) for _ in range(lb+1)]

for i in range(1,lb+1):
    for j in range(1,la+1):
        dp[i][j] = max(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])
        if A[j-1] == B[i-1]:
            dp[i][j]+=1

print(max(la,lb) - dp[-1][-1])

'''
cat
cut

sunday
saturday
'''
