x = int(input())
y = int(input())

day = 1
currentX = x
while currentX < y:
    currentX = 1.1 * currentX
    day += 1
print(day)