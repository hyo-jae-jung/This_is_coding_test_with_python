from sys import stdin   

N,M = map(int,stdin.readline().strip().split())
bowling_balls = list(map(int,stdin.readline().strip().split()))

d = {}
for i in bowling_balls:
    if not d.get(i):
        d.update({i:0})
    d[i]+=1

ans = N*(N-1)//2

for _,cnt in d.items():
    ans-=cnt*(cnt-1)//2

print(ans)

'''
5 3
1 3 2 3 2

8 5
1 5 4 3 2 4 5 2
'''
