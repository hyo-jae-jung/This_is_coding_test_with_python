'''
indegree 개념을 활용하면 풀 수 있을 듯?
--> 틀렸어 서로소 개념이야. union-find
'''

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

G = int(stdin.readline().strip())
parent = list(range(G+1))
P = int(stdin.readline().strip())
ans = 0
possibility = True
for _ in range(P):
    g = int(stdin.readline().strip())
    if possibility:
        if (pg:=parent_find(parent,g)) != 0:
            parent_union(parent,pg,pg-1)
            ans+=1
        else:
            possibility = False

print(ans)

'''
예시1
4
3
4
1
1

예시2
4
6
2
2
3
3
4
4
'''
