def power(a, n):
    if n == 0:
        return 1
    elif n > 0:
        return a * power(a, n - 1)
    elif n < 0:
        return power(1/a, -n)

a = float(input())
n = float(input())

print(power(a, n))