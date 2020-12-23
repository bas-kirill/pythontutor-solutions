str = input()

firstOccur = str.find('h')
lastOccur = str.rfind('h')
print(str[:firstOccur] + str[lastOccur + 1:])