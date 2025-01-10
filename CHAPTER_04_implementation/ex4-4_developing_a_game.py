from sys import stdin 
from itertools import cycle 

N,M = map(int,stdin.readline().strip().split())
player = [int(i) for i in stdin.readline().strip().split()]
first_direction = player.pop()

map = []
for _ in range(N):
    map.append([int(i) for i in stdin.readline().strip().split()])

direction = cycle([0,3,2,1])

while True:
    temp = next(direction)
    if first_direction == temp:
        break

delta ={
    0:[-1,0],
    1:[0,1],
    2:[1,0],
    3:[0,-1],
}

cnt=0
while True:
    d_cnt=0
    while d_cnt < 4: 
        temp = next(direction)
        x,y = delta[temp][0]+player[0],delta[temp][1]+player[1]
        if map[x][y] == 0:
            map[player[0]][player[1]] = 1
            player = [x,y]
            cnt+=1
            break
        d_cnt+=1
    else:
        temp = next(direction)
        back = [i*-1 for i in delta[temp]]
        x,y = back[0]+player[0],back[1]+player[1]
        if map[x][y] == 0:
            map[player[0]][player[1]] = 1
            player = [x,y]
            cnt+=1
        else:
            map[player[0]][player[1]] = 1
            cnt+=1
            break

print(map)
print(cnt)

# 범위 밖 고려 안한 고딩임. 그냥 테두리에 1 채워주면 됨 
