n, m = [int(elem) for elem in input().split(' ')]

a = [['.' if (i + j) % 2 == 0 else '*' for j in range(m)] for i in range(n)]

for row in a:
    print(' '.join(row))

