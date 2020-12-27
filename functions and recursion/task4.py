def pow(a, n):
    if n == 0:
        return 1
    else:
        return a * pow(a, n - 1)

a = float(input())
n = int(input())
print(pow(a, n))