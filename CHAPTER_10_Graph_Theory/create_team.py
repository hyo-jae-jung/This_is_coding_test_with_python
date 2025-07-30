
def parent_find(parent,x):
    if parent[x] != x:
        parent[x] = parent_find(parent,parent[x])
    return parent[x]

def parent_union(parent,a,b):
    a = parent_find(parent,a)
    b = parent_find(parent,b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

ans = []

from sys import stdin   

N,M = map(int,stdin.readline().strip().split())
parent = list(range(N+1))
for _ in range(M):
    commend,a,b = map(int,stdin.readline().strip().split())
    if commend == 0:
        parent_union(parent,a,b)
    else:
        if parent_find(parent,a) == parent_find(parent,b):
            ans.append('YES')
        else:
            ans.append('NO')

print(*ans,sep='\n')

'''
7 8
0 1 3
1 1 7
0 7 6
1 7 1
0 3 7
0 4 2
0 1 1
1 1 1
'''