a = [int(elem) for elem in input().split(' ')]
for i in range(len(a)):
    flag = True
    for j in range(len(a)):
        if i == j:
            continue
        if a[i] == a[j]:
            flag = False
    if flag:
        print(a[i], end=' ')