from sys import stdin  

N = int(stdin.readline().strip())
arr = list(map(int,stdin.readline().strip().split()))

ans = 0
arr.sort(reverse=True)
p = []
while arr:
    p.append(arr.pop())
    if max(p) == len(p):
        ans+=1
        p = []

print(ans)

'''
5
2 3 1 2 2
'''
