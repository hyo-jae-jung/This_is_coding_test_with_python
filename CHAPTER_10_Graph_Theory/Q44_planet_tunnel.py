def parent_find(parent,x):
    if parent[x] != x:
        parent[x] = parent_find(parent,parent[x])
    return parent[x]

def parent_union(parent,a,b):
    a = parent_find(parent,a)
    b = parent_find(parent,b)

    if a > b:
        parent[a] = b
    else:
        parent[b] = a 

from sys import stdin  
from heapq import heappush,heappop

N = int(stdin.readline().strip())
h = []
X,Y,Z = [],[],[]
for i in range(N):
    x,y,z = map(int,stdin.readline().strip().split())
    heappush(X,(x,i))
    heappush(Y,(y,i))
    heappush(Z,(z,i))

def create_edge(arr,h):
    a,i = heappop(arr)
    while arr:
        b,j = heappop(arr)
        heappush(h,(abs(a-b),i,j))
        a,i = b,j
    
create_edge(X,h)
create_edge(Y,h)
create_edge(Z,h)

ans = 0
parent = list(range(N))
i = 0
while h and i < N:
    cost,x,y = heappop(h)
    if (a:=parent_find(parent,x)) != (b:=parent_find(parent,y)):
        parent_union(parent,a,b)
        ans+=cost
        i+=1

print(ans)
