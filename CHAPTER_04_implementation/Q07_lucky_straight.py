from sys import stdin  

N = stdin.readline().strip()
l = len(N)//2
ans = 0
for i in range(l):
    ans+=int(N[i]) - int(N[-(i+1)])

if ans == 0:
    print('LUCKY')
else:
    print('READY')
    