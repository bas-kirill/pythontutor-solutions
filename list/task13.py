a = [int(elem) for elem in input().split(' ')]
cnt = 0
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if a[i] == a[j]:
            cnt += 1

print(cnt)
