n = int(input())

last, cur = 0, 1
for i in range(2, n + 1):
    tmp = cur
    cur = last + cur
    last = tmp

if n == 0:
    print(0)
else:
    print(cur)