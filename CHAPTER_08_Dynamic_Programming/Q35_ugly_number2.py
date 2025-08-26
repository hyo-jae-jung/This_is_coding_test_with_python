import sys
from heapq import heappush,heappop

N = int(sys.stdin.readline().strip())
s = set([1])
q = [1]

n = 0
while q:
    u_num = heappop(q)
    n+=1

    if n == N:
        print(u_num)
        break

    for i in [2,3,5]:
        if (tmp:=u_num*i) not in s:
            heappush(q,tmp)
            s.add(tmp)
