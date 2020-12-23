str = input()

firstOccur = str.find('h')
lastOccur = str.rfind('h')
print(str[0:firstOccur + 1] + str[lastOccur - 1:firstOccur:-1] + str[lastOccur:])