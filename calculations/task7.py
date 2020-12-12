a = int(input())
b = int(input())
n = int(input())

costTotal = (a * 100 + b) * n
print(costTotal // 100, costTotal % 100)