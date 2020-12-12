from math import sqrt
alpha = float(input())

h = alpha // 30
alphaMinute = (alpha - h * 30) / 30 * 360
print(alphaMinute)