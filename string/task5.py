str = input()

cnt = str.count('f')

if cnt == 1:
    print(str.find('f'))
elif cnt >= 2:
    print(str.find('f'), str.rfind('f'), sep=' ')