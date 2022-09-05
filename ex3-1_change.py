X = int(input())
Y = 0
changes = [500,100,50,10]
for i in changes:
    Y += X//i
    X %= i
print(Y)