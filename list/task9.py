a = [int(elem) for elem in input().split(' ')]

for i in range(0, len(a) - int(len(a) % 2), 2):
    a[i], a[i + 1] = a[i + 1], a[i]

print(' '.join([str(i) for i in a]))
