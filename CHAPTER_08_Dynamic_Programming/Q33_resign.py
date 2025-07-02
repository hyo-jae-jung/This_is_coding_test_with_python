from sys import stdin  

N = int(stdin.readline().strip())
schedule = []
for _ in range(N):
    schedule.append(tuple(map(int,stdin.readline().strip().split())))

dp = [0]*(N+1)

for i,j in enumerate(schedule,1):
    print(i,j)
    if i+j[0]-1 <= N:
        dp[i+j[0]-1] = max(max(dp[:i])+j[1],dp[i+j[0]-1])

print(max(dp))

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