from sys import stdin   

N,C = map(int,stdin.readline().strip().split())
locations = []
for _ in range(N):
    locations.append(int(stdin.readline().strip()))
locations.sort()

def parametric_search_part(n,arr,min_d):
    min_val = float('inf')
    diff = []
    cnt = 1
    i,j = 0,1
    while i+j < n:
        if (pd:=arr[i+j] - arr[i]) < min_d:
            j+=1
        else:
            diff.append(pd)
            min_val = min(min_val,pd)
            i+=j
            j = 1
            cnt+=1
    print(diff)
    return cnt,min_val

left = 0
right = locations[-1] - locations[0]

while left < right:
    mid = (left+right)//2
    cnt,max_val = parametric_search_part(N,locations,mid)
    if cnt <= C:
        right = mid
    else:
        left = mid + 1

print(right)

'''
5 3
1
2
8
4
9
'''
