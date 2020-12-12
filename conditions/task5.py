a = int(input())
b = int(input())
c = int(input())

if a > b:
    t = a
    a = b
    b = t

if a > c:
    t = a
    a = c
    c = t

print(a)