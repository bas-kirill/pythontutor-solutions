str = input().split(' ')
a = [int(elem) for elem in str]

i = 1
ans = 0
while i < len(a) - 1:
    if a[i - 1] < a[i] > a[i + 1]:
        ans += 1
    i += 1

print(ans)
