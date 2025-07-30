from sys import stdin 

S = stdin.readline().strip()
ans = 0
for i in S:
    if i != '0':
        if ans == 0:
            ans+=int(i)
        else:
            ans*=int(i)

print(ans)
