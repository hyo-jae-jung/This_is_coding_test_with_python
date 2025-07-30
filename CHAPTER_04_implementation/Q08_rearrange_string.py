from sys import stdin  

S = stdin.readline().strip()
string = []
num = 0
for i in S:
    if ord(i) >= 65:
        string.append(i)
    else:
        num+=int(i)
string.sort()
print(''.join(string) + str(num))

'''
K1KA5CB7

AJKDLSI412K4JSJ9D
'''
