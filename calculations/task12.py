from math import sqrt
h = int(input())
m = int(input())
s = int(input())

time = h * 30 + m / 60 * 30 + s / 3600 * 30

print(time)