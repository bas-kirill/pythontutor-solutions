import math
x = int(input())
sumSqr = 0
sum = 0
cnt = 0
while x != 0:
    sum += x
    sumSqr += x * x
    cnt += 1
    x = int(input())

av = sum / cnt
ans = math.sqrt((sumSqr - 2 * av * sum + cnt * av**2) / (cnt - 1))
print(ans)