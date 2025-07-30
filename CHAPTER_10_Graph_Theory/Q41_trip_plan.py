'''
연결만 돼 있으면 계획 중간에 다른 장소를 경유해도 되기 때문에 
하나의 컴포넌트인지 확인하는 문제

크루스칼 알고리즘을 사용

크루스칼 알고리즘 사용 조건
    양방향(무방향) 그래프
    하나의 컴포넌트
    간선 비용 존재

해당 문제에서는 간선 비용 X
양방향 그래프이며 컴포넌트 개수가 몇 개인지 물어보는 것으로 보인다.
union-find만 이용하면 되나?

union-find 이용하는 거 맞는데 여행 계획에 포함된 여행지 번호만 같은 컴포넌트면 됨.
'''

def find_parant(parant,x):
    if parant[x] != x:
        parant[x] = find_parant(parant,parant[x])
    return parant[x]

def union_parant(parant,a,b):
    a = find_parant(parant,a)
    b = find_parant(parant,b)

    if a > b:
        parant[a] = b
    else:
        parant[b] = a

from sys import stdin  

N,M = map(int,stdin.readline().strip().split())
arr = [list(map(int,stdin.readline().strip().split())) for _ in range(N)]
plan = list(map(int,stdin.readline().strip().split()))

parant = [i for i in range(N)]

for i in range(N):
    for j in range(i+1,N):
        if arr[i][j] == 1:
            union_parant(parant,i,j)

ans = 'YES'
for i in range(1,M):
    if find_parant(parant,plan[i]) != find_parant(parant,plan[i-1]):
        ans = 'NO'
        break

print(ans)

"""
5 4
0 1 0 1 1
1 0 1 1 0
0 1 0 0 0
1 1 0 0 0
1 0 0 0 0
2 3 4 3
"""