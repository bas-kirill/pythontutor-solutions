str = input()

cnt = str.count('f')

if cnt >= 2:
    idx = str.find('f')
    secondOccur = str.find('f', idx + 1)
    print(secondOccur)
elif cnt == 1:
    print(-1)
else:
    print(-2)