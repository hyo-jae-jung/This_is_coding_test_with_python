from sys import stdin  

n = int(stdin.readline().strip())
triangle = [list(map(int,stdin.readline().strip().split())) for _ in range(n)]

for i in range(1,n):
    for j in range(i+1):
        triangle[i][j]+=max(triangle[i-1][j-1] if j > 0 else 0,triangle[i-1][j] if j < i else 0)

print(max(triangle[-1]))

for i in triangle:
    print(i)

'''
5
7
3 8
8 1 0
2 7 4 4
4 5 2 6 5
'''