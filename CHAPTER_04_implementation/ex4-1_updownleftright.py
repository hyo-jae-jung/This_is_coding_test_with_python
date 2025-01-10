N = int(input())
moves = input().split()

x,y = 1,1

for move in moves:
    if move == "L":
        x = x-1 if x > 2 else 1
    elif move == "R":
        x = x+1 if x < N else N
    elif move == "U":
        y = y-1 if y > 2 else 1
    elif move == "D":
        y = y+1 if y < N else N

print(y,x)
