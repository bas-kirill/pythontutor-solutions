def swap_columns(a, i, j):
    for row in range(len(a)):
        t = a[row][i]
        a[row][i] = a[row][j]
        a[row][j] = t


n, m = [int(elem) for elem in input().split(' ')]
a = [[int(elem) for elem in input().split(' ')] for i in range(n)]

i, j = [int(elem) for elem in input().split(' ')]
swap_columns(a, i, j)

print('\n'.join([' '.join([str(i) for i in row]) for row in a]))
