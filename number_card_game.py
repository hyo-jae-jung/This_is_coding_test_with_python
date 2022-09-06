N,M = map(int,input().split())
array = []
for _ in range(N):
    array.append([int(i) for i in input().split()])

print(max(map(min,array)))