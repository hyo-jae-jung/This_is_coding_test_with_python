from sys import stdin  
S = stdin.readline().strip()
ans0,ans1 = 0,0
buffer = '2'
for i in S:
    if buffer != i:
        if i == '0':
            ans0+=1
        else:
            ans1+=1
        buffer = i

print(min(ans0,ans1))

