x = int(input())
last = x - 1
cur = x
cnt = 0
while x != 0:
    if cur > last:
        cnt += 1
    x = int(input())
    last = cur
    cur = x
else:
    print(cnt - 1)