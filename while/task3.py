n = int(input())

deg = 0
while 2**(deg + 1) <= n:
    deg += 1
print(deg, 2 ** deg)