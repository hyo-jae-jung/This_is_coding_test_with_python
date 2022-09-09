N = int(input())
y,x = 1,1
moves = input().split()
for move in moves:
    if move == "L":
        x-=1
    elif move == "R":
        x+=1
    elif move == "U":
        y-=1
    elif move == "D":
        y+=1

    if x==0:
        x+=1
    if y==0:
        y+=1
print(x,y)