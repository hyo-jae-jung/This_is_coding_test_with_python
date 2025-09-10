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

from sys import stdin  

N = int(stdin.readline().strip())

items = []
for i in range(N):
    x,y,z = map(int,stdin.readline().strip().split())
    items.append((i,x,y,z))

edges = []
for j in range(1,4):
    items.sort(key=lambda x:(x[j]))
    for i in range(1,N):
        edges.append((abs(items[i][j] - items[i-1][j]),items[i][0],items[i-1][0]))

edges.sort()

parent = list(range(N))
cost = 0
for d,a,b in edges:
    if (a:=find_parent(parent,a)) != (b:=find_parent(parent,b)):
        union_parent(parent,a,b)
        cost+=d

print(cost)

'''
5
11 -15 -15
14 -5 -15
-1 -1 -5
10 -4 -1
19 -4 19
'''