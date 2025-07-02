from sys import stdin 
import pdb

N,M = map(int,stdin.readline().strip().split())
tteoks = [int(i) for i in stdin.readline().strip().split()]

left = 0
right = max(tteoks)

while left <= right:
    mid = (left+right)//2
    temp = sum(i-mid if i > mid else 0 for i in tteoks)
    print(left,mid,right,temp)
    # pdb.set_trace()
    if temp <= M:
        right = mid - 1
    else:
        left = mid + 1

print(mid)
