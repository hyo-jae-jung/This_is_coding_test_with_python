N = input()
col_temp=N[0]
row=int(N[1])

trans = {
    'a':1,
    'b':2,
    'c':3,
    'd':4,
    'e':5,
    'f':6,
    'g':7,
    'h':8,
}

col = trans[col_temp]

count = 0
table = range(1,9)
moves = [
    [-2,-1],
    [-1,-2],
    [1,-2],
    [2,-1],
    [-2,1],
    [1,-2],
    [2,1],
    [1,2],
]

for move in moves:
    if col+move[0] in table and row+move[1] in table:
        count+=1

print(count)
