a = [int(elem) for elem in input().split(' ')]
number = int(input())

l = -1
r = len(a)

while l + 1 < r:
    m = l + (r - l) // 2
    if a[m] >= number:
        l = m
    else:
        r = m

print(r + 1)
