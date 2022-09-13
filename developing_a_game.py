N,M = map(int,input().split())
row,col,start_direction = map(int,input().split())
map = []
for _ in range(N):
    map.append(input().split())

print(N,M)
print(row,col,start_direction)
print(map)
print(map[row][col])

direction = {
    0:[[-1,0],[0,-1],[1,0],[0,1]],
    1:[[0,1],[-1,0],[0,-1],[1,0]],
    2:[[1,0],[0,1],[-1,0],[0,-1]],
    3:[[0,-1],[1,0],[0,1],[-1,0]],
}

print(map[direction[start_direction][0][0]+row][direction[start_direction][0][1]+col])
