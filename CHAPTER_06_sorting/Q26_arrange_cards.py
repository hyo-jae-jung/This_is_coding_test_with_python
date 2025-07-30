from sys import stdin  
from heapq import heappop,heappush

N = int(stdin.readline().strip())
arr = []
for _ in range(N):
    heappush(arr,int(stdin.readline().strip()))

ans = 0
while len(arr) > 1:
    print(arr)
    a = heappop(arr)
    b = heappop(arr)
    heappush(arr,a+b)
    ans+=a+b

print(ans)
