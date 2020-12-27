a = [int(elem) for elem in input().split(' ')]

occur_before = set()
for elem in a:
    if elem in occur_before:
        print('YES')
    else:
        occur_before.add(elem)
        print('NO')
