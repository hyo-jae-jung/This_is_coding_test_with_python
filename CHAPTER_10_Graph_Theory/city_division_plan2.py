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

N,M = map(int,stdin.readline().strip().split())
parent = list(range(N+1))

items = [tuple(map(int,stdin.readline().strip().split())) for _ in range(M)]
items.sort(key=lambda x:(x[2]))
ans = 0
link_cnt = 0
for item in items:
    if link_cnt < N-2:
        A,B,C = item
        a = find_parent(parent,A)
        b = find_parent(parent,B)
        if a != b:
            ans+=C
            union_parent(parent,a,b)
            link_cnt+=1

print(ans)

'''
7 12
1 2 3
1 3 2
3 2 1
2 5 2
3 4 4
7 3 6
5 1 5
1 6 2
6 4 1
6 5 3
4 5 3
6 7 4
'''
