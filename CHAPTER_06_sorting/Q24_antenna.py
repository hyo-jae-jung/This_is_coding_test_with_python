'''
4
5 1 7 9
'''

from sys import stdin   

N = int(stdin.readline().strip())
arr = list(map(int,stdin.readline().strip().split()))

arr.sort()

print(arr[(N-1)//2])
