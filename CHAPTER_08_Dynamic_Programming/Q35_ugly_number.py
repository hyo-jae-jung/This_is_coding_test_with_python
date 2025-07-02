from sys import stdin  
from heapq import heappop,heappush,heapify

N = int(stdin.readline().strip())
visited = set()
ans = []
u_num = [(1,0,0,0)]
heapify(u_num)

while len(ans) < N:
    n,a,b,c = heappop(u_num)
    if -n not in visited:
        heappush(ans,-n)
        visited.add(-n)
    
    heappush(u_num,((2**(a+1))*(3**b)*(5**c),a+1,b,c))
    heappush(u_num,((2**a)*(3**(b+1))*(5**c),a,b+1,c))
    heappush(u_num,((2**a)*(3**b)*(5**(c+1)),a,b,c+1))    

print(len(u_num))
print(-heappop(ans))

"""
이렇게 만들면 시간이고 공간이고 모두 부족하다.
"""

