x = int(input())
cnt = 0
while x != 0:
    if x % 2 == 0:
        cnt += 1
    x = int(input())
else:
    print(cnt)