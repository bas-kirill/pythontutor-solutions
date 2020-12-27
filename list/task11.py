a = [int(elem) for elem in input().split(' ')]
k = int(input())
b = a[:k] + a[k + 1:]
print(' '.join([str(elem) for elem in b]))