a = int(input())
b = int(input())
c = int(input())

similarNumbers = 0

if a == b and b == c:
    similarNumbers = 3
elif a == b or a == c or b == c:
    similarNumbers = 2

print(similarNumbers)