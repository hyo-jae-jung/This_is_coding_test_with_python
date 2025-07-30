from sys import stdin  

N = int(stdin.readline().strip())
A = list(map(int,stdin.readline().strip().split()))
M = int(stdin.readline().strip())
B = list(map(int,stdin.readline().strip().split()))

A.sort()
print(A)

def binary_search(arr,val):

    left = 0
    right = len(arr) - 1
    while left < right:
        mid = (left+right)//2
        if arr[mid] < val:
            left = mid + 1
        else:
            right = mid

    return 'yes' if arr[right] == val else 'no'

ans = []
for b in B:
    ans.append(binary_search(A,b))
        
print(*ans,sep='\n')


'''
5
8 3 7 9 2
3
5 7 9
'''
