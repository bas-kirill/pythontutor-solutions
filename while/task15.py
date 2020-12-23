n = int(input())

last, cur = 0, 1
number = 1
while cur < n:
    tmp = cur
    cur = last + cur
    last = tmp
    number += 1

if n == 0:
    print(0)
else:
    if cur == n:
        print(number)
    else:
        print(-1)