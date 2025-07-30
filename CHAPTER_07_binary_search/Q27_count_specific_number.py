from sys import stdin  
from bisect import bisect_left,bisect_right

N,x = map(int,stdin.readline().strip().split())
elements = list(map(int,stdin.readline().strip().split()))

diff = bisect_right(elements,x) - bisect_left(elements,x)

print(diff if diff > 0 else -1)

def lower_bound(arr,x):
    left = 0
    right = len(arr) - 1

    while left < right:
        mid = (left+right)//2
        if arr[mid] < x:
            left = mid + 1
        else:
            right = mid

    return left,right

def upper_bound(arr,x):
    left = 0
    right = len(arr) - 1

    while left < right:
        mid = (left+right)//2
        if arr[mid] <= x:
            left = mid + 1
        else:
            right = mid

    return left,right

print(bisect_right(elements,x))
print(bisect_left(elements,x))
print(lower_bound(elements,x))
print(upper_bound(elements,x))

'''
7 2
1 1 2 2 2 2 3
'''
