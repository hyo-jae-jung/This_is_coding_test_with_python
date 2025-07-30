from sys import stdin  
from itertools import permutations as perm

N = int(stdin.readline().strip())
A = list(map(int,stdin.readline().strip().split()))
operators_cnt = list(map(int,stdin.readline().strip().split()))
operators = ['+']*operators_cnt[0] + ['-']*operators_cnt[1] + ['*']*operators_cnt[2] + ['/']*operators_cnt[3]

max_val = -10**9+1
min_val = 10**9+1

for i in perm(operators):
    value = A[0]
    for j,k in zip(i,A[1:]):
        if j == '+':
            value+=k
        elif j == '-':
            value-=k
        elif j == '*':
            value*=k
        elif j == '/':
            if value >= 0:
                value = value//k
            else:
                value = -1*((-1*value)//k)

    max_val = max(max_val,value)
    min_val = min(min_val,value)

print(max_val)
print(min_val)

'''
2
5 6
0 0 1 0

3
3 4 5
1 0 1 0

6
1 2 3 4 5 6
2 1 1 1
'''