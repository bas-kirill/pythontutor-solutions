import math
p = int(input())
x = int(input())
y = int(input())

eps = 1e-6

money = x * 100 + y
money = (1 + p / 100) * money
if math.fabs(math.ceil(money) - money) < eps:
    money = math.ceil(money)
print(int(money // 100), int(money % 100))