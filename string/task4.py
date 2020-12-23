str = input()
idx = str.find(' ')
firstWord = str[:idx]
secondWord = str[idx + 1:]
print(secondWord, firstWord)