a = [int(elem) for elem in input().split(' ')]

mx = a[0]
idxMax = 0
mn = a[0]
idxMin = 0
for i in range(len(a)):
    if a[i] > mx:
        mx = a[i]
        idxMax = i
    if a[i] < mn:
        mn = a[i]
        idxMin = i

a[idxMin], a[idxMax] = a[idxMax], a[idxMin]

print(' '.join([str(i) for i in a]))
