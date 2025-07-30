from sys import stdin  

T = int(stdin.readline().strip())
ans = []
for _ in range(T):
    n = int(stdin.readline().strip())
    arr = map(int,stdin.readline().strip().split())
    indegree_previous = [0]*n
    for i,j in enumerate(arr):
        indegree_previous[j-1] = i
    
    indegree_now = indegree_previous.copy()

    m = int(stdin.readline().strip())
    for _ in range(m):
        a,b = map(int,stdin.readline().strip().split())
        if indegree_previous[a-1] > indegree_previous[b-1]:
            indegree_now[a-1]-=1
            indegree_now[b-1]+=1
        else:
            indegree_now[a-1]+=1
            indegree_now[b-1]-=1

    certain = True
    cycle = False
    result = []
    i = 0
    for _ in range(n):
        e = []
        for j,k in enumerate(indegree_now,1):
            if k == i:
                e.append(j)

        l = len(e)
        if l > 1:
            certain = False
        elif l == 0:
            cycle = True
            break
        result.extend(e)
        i+=l
    
    if cycle:
        ans.append(["IMPOSSIBLE"])
    elif not certain:
        ans.append(["?"])
    else:
        ans.append(result)

for i in ans:
    print(*i)

'''
3
5
5 4 3 2 1
2
2 4
3 4
3
2 3 1
0
4
1 2 3 4
3
1 2
3 4
2 3
'''