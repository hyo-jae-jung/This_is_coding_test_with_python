from sys import stdin  
from bisect import bisect_left

N = int(stdin.readline().strip())
soldiers = list(map(int,stdin.readline().strip().split()))

ans = []
for soldier in soldiers:
    i = bisect_left(ans,-soldier)
    if len(ans) == i:
        ans.append(-soldier)
    else:
        ans[i] = -soldier

print(N - len(ans))
