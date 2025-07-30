def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

from sys import stdin  

n,e = map(int,stdin.readline().strip().split())

edges = []
ans = 0
parent = list(range(n+1))
for _ in range(e):
    a,b,cost = map(int,stdin.readline().strip().split())
    edges.append((cost,a,b))

edges.sort()
print(edges)
print(parent)
for i,j in enumerate(edges,1):
    cost,a,b = j
    if tt:=(find_parent(parent,a) != find_parent(parent,b)):
        union_parent(parent,a,b)
        ans+=cost
    print(i,parent,tt)

# print(ans)

'''
7 9
1 2 29
1 5 75
2 3 35
2 6 34
3 4 7
4 6 23
4 7 13
5 6 53
6 7 25
'''
