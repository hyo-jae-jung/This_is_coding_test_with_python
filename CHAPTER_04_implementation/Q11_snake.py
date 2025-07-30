from sys import stdin
from collections import deque 

N = int(stdin.readline().strip())
K = int(stdin.readline().strip())
apple_loc = set()
direction = [(1,0),(0,1),(-1,0),(0,-1)]
p_direction = 0
snake = deque([(1,1)])

move = []

for _ in range(K):
    y,x = map(int,stdin.readline().strip().split())
    apple_loc.add((x,y))

L = int(stdin.readline().strip())
for _ in range(L):
    X,C = stdin.readline().strip().split()
    move.append((int(X),C))

sec = 0
move_idx = 0

while True:
    px,py = snake[-1]

    dx,dy = direction[p_direction]
    nx = px+dx
    ny = py+dy

    if 0 >= nx or nx > N or 0 >= ny or ny > N:
        break

    if (nx,ny) in snake:
        break

    if (nx,ny) in apple_loc:
        apple_loc.remove((nx,ny))
    else:
        snake.popleft()

    snake.append((nx,ny))

    sec+=1

    if move_idx < L and sec == move[move_idx][0]:
        if move[move_idx][1] == 'D':
            p_direction = (p_direction+1)%4
        else:
            p_direction = (p_direction-1)%4
        move_idx+=1

    print(snake,apple_loc,p_direction,sec)

print(sec+1)

'''
6
3
3 4
2 5
5 3
3
3 D
15 L
17 D

10
4
1 2
1 3
1 4
1 5
4
8 D
10 D
11 D
13 L

10
5
1 5
1 3
1 2
1 6
1 7
4
8 D
10 D
11 D
13 L
'''
