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

G = int(stdin.readline().strip())
P = int(stdin.readline().strip())
parent = list(range(G+1))
ans,cnt = 0,0
for _ in range(P):
    g = int(stdin.readline().strip())
    if (gg:=find_parent(parent,g)) > 0:
        union_parent(parent,gg,gg-1)
        cnt+=1
    else:
        if ans == 0:
            ans = cnt

print(ans)

'''
4
3
4
1
1

4
6
2
2
3
3
4
4
'''
