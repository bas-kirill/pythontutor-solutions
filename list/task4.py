str = input().split(' ')
a = [int(elem) for elem in str]

i = 0
while i < len(a) - 1:
    signCur = a[i] > 0
    signNext = a[i + 1] > 0

    if signCur == signNext:
        print(a[i], a[i + 1], end=' ')
        break
    i += 1