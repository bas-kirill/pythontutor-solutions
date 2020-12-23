x = int(input())
mx = -1
cnt = 0
while x != 0:
    if x > mx:
        mx, cnt = x, 1
    elif x == mx:
        cnt += 1
    x = int(input())
else:
    print(cnt)