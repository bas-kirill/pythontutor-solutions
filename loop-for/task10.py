n = int(input())

sum = int(n * (n + 1) / 2)
for i in range(0, n - 1):
    x = int(input())
    sum -= x
print(sum)