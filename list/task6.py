a = [int(elem) for elem in input().split(' ')]

mx = a[0]
idx = 0
for i in range(len(a)):
    if a[i] > mx:
        mx = a[i]
        idx = i

print(mx, idx)
