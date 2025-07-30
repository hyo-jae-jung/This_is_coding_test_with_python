from sys import stdin  

N,M = map(int,stdin.readline().strip().split())
arr = list(map(int,stdin.readline().strip().split()))

left = 0
right = max(arr)

while left < right:
    tmp = 0
    mid = (left+right)//2

    for i in arr:
        tmp+= i-mid if i > mid else 0

    if tmp > M:
        left = mid + 1
    else:
        right = mid

print(right)
