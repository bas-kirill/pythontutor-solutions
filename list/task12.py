a = [int(elem) for elem in input().split(' ')]
k, c = [int(elem) for elem in input().split(' ')]

a.insert(k, c)
print(' '.join([str(elem) for elem in a]))