from sys import stdin  

T = int(stdin.readline().strip())
ans = []
for _ in range(T):
    n,m = map(int,stdin.readline().strip().split())
    mine = [[] for _ in range(m)]

    for i,j in enumerate(map(int,stdin.readline().strip().split())):
        mine[i%m].append(j)

    for i in range(m-2,-1,-1):
        for j in range(n):
            mine[i][j]+=max(mine[i+1][0 if j <= 0 else j-1:j+2])
            
        
    ans.append(max(mine[0]))

print(*ans,sep='\n')

