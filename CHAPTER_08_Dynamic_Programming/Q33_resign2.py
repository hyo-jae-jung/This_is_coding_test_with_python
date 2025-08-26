from sys import stdin  

N = int(stdin.readline().strip())

dp = [0]*(N+1)
max_value = 0
for i in range(1,N+1):
    t,p = map(int,stdin.readline().strip().split())
    if (nt:=i+t-1) <= N:
        dp[nt] = max(dp[nt],max_value + p)
    max_value = max(max_value,dp[i])
    print(dp,max_value)
print(max(dp))

# --- 
# 답안 예시
# n = int(input())
# t = []
# p = []
# dp = [0]*(n+1)
# max_value = 0

# for _ in range(n):
#     x,y = map(int,input().split())
#     t.append(x)
#     p.append(y)

# for i in range(n-1,-1,-1):
#     time = t[i] + i
#     if time <= n:
#         dp[i] = max(p[i]+dp[time],max_value)
#         max_value = dp[i]
#     else:
#         dp[i] = max_value
#     print(dp,max_value)
# print(max(dp))


"""
7
3 10
5 20
1 10
1 20
2 15
4 40
2 200

10
1 1
1 2
1 3
1 4
1 5
1 6
1 7
1 8
1 9
1 10

10
5 10
5 9
5 8
5 7
5 6
5 10
5 9
5 8
5 7
5 6

10
5 50
4 40
3 30
2 20
1 10
1 10
2 20
3 30
4 40
5 50
"""