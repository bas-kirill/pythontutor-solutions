x = int(input())
mx1 = -1
mx2 = -1
while x != 0:
    if x > mx1:
        mx2 = mx1
        mx1 = x
    elif x > mx2:
        mx2 = x
    x = int(input())
else:
    print(mx2)