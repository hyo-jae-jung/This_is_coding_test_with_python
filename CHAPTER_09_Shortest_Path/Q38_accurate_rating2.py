from sys import stdin  

N,M = map(int,stdin.readline().strip().split())
arr = [[0]*N for _ in range(N)]

for _ in range(M):
    A,B = map(int,stdin.readline().strip().split())
    arr[A-1][B-1] = 1

for k in range(N):
    for i in range(N):
        for j in (j for j in range(N) if j != i):
            arr[i][j] = arr[i][j] or (arr[i][k] and arr[k][j])

ans = 0
for i in range(N):
    cnt = 1
    for j in (j for j in range(N) if j != i):
        cnt+=arr[i][j] or arr[j][i]
    if cnt == N:
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
