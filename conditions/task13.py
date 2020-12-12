# file = open('input.txt', 'r')

N = int(input())
M = int(input())
x = int(input())
y = int(input())

if N > M:
    N, M = M, N

xAnother = N - x
yAnother = M - y

print(min(x, min(y, min(xAnother, yAnother))))