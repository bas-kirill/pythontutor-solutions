x = int(input())
mx = x
while x != 0:
    mx = max(mx, x)
    x = int(input())
else:
    print(mx)