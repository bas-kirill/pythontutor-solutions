# beatiful solution:
# a = [[abs(i - j) for j in range(n)] for i in range(n)]

n = int(input())

a = [[0 for j in range(n)] for i in range(n)]

curRow = [i for i in range(0, n)]
idx = 1
for i in range(n):
    step = 1
    for j in range(i + 1, n):
        a[i][j] = step
        step += 1
    step = i
    for j in range(0, i):
        a[i][j] = step
        step -= 1

for row in a:
    print(' '.join([str(elem) for elem in row]))