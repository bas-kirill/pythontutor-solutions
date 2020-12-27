n, m = [int(elem) for elem in input().split(' ')]

a = [[int(elem) for elem in input().split(' ')] for i in range(n)]

mx = a[0][0]
best_i, best_j = 0, 0
for i in range(n):
    for j in range(m):
        if a[i][j] > mx:
            mx = a[i][j]
            best_i = i
            best_j = j
print(best_i, best_j)
