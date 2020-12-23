str = input()

ans = ''
tmp = ''
for i in range(len(str)):
    if i % 3 != 0:
        tmp = tmp + str[i]
    else:
        ans += tmp
        tmp = ''

if len(tmp) != 0:
    ans += tmp

print(ans)
