from sys import stdin  
from heapq import heappush, heappop

N,M,K = map(int,stdin.readline().strip().split())
nums = list(map(int,stdin.readline().strip().split()))

h = []

while nums:
    heappush(h,nums.pop())
    if len(h) > 2:
        heappop(h)

second = heappop(h)
first = heappop(h)

print((first*K+second)*(M//(K+1)) + first*(M%(K+1)))
