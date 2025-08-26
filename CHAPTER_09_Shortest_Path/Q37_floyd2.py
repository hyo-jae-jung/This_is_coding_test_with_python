from sys import stdin  

n = int(stdin.readline().strip())
m = int(stdin.readline().strip())
adj_arr = [[float('inf')]*n for _ in range(n)]
for _ in range(m):
    a,b,c = map(int,stdin.readline().strip().split())
    adj_arr[a-1][b-1] = min(adj_arr[a-1][b-1],c)

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i != j:
                adj_arr[i][j] = min(adj_arr[i][k] + adj_arr[k][j], adj_arr[i][j])

for i in range(n):
    for j in range(n):
        if adj_arr[i][j] == float('inf'):
            adj_arr[i][j] = 0

for i in adj_arr:
    print(*i)

'''
5
14
1 2 2
1 3 3
1 4 1
1 5 10
2 4 2
3 4 1
3 5 1
4 5 3
3 5 10
3 1 8
1 4 2
5 1 7
3 4 2
5 2 4
'''