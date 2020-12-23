str = input()

firstOccur = str.find('h')
lastOccur = str.rfind('h')

print(str[:firstOccur + 1] + str[firstOccur + 1:lastOccur].replace('h', 'H') + str[lastOccur:])