from sys import stdin   

N = int(stdin.readline().strip())
arr = list(map(int,stdin.readline().strip().split()))

def lower_bound(arr):

    def parametric_search_part(arr,x):
        if arr[x] >= x:
            return True
        else:
            return False
        
    left = 0
    right = len(arr) - 1

    while left < right:
        mid = (left+right)//2

        if parametric_search_part(arr,mid):
            right = mid
        else:
            left = mid + 1
        print(left,right)
    return arr[mid] if arr[mid] == mid else -1

print(lower_bound(arr))


'''
5
-15 -16 1 3 7

7
-15 -4 2 8 9 13 15

7
-15 -4 3 8 9 13 15

'''
