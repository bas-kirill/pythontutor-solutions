n = int(input())

a = [[0 for j in range(n)] for i in range(n)]

for i in range(n):
    for j in range(n - i, n):
        a[i][j] = 2
    a[i][n - i - 1] = 1

for row in a:
    print(' '.join([str(elem) for elem in row]))