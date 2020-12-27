n, k = [int(elem) for elem in input().split(' ')]
kegels = ['I' for i in range(n)]
for i in range(k):
    kegelL, kegelR = [int(elem) for elem in input().split(' ')]
    for i in range(kegelL - 1, kegelR):
        kegels[i] = '.'
print(''.join([elem for elem in kegels]))
