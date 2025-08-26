"""
5 4
0 1 0 1 1
1 0 1 1 0
0 1 0 0 0
1 1 0 0 0
1 0 0 0 0
2 3 4 3
"""

from sys import stdin  

N,M = map(int,stdin.readline().strip().split())

parent = list(range(N+1))
def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x] 

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)

    if a > b:
        parent[a] = b
    else:
        parent[b] = a

for i in range(1,N+1):
    tmp = list(map(int,stdin.readline().strip().split()))
    for j in range(N):
        if tmp[j] == 1:
            union_parent(parent,i,j-1)


tmp = list(map(int,stdin.readline().strip().split()))
for i in range(1,M):
    if parent[tmp[i]] != parent[tmp[i-1]]:
        print('NO')
        break
else:
    print('YES')
