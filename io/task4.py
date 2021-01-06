n = int(input())

dayMinutes = 60 * 24
n = n % dayMinutes
print(n // 60, n % 60)