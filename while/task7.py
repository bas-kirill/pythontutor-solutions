sum = 0
cnt = 0
x = int(input())
while x != 0:
    sum += x
    cnt += 1
    x = int(input())
else:
    print(sum / cnt)