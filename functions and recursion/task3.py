def capitalize(line):
    words = line.split(' ')
    capWords = []
    for word in words:
        newWord = chr(ord(word[0]) - 32) + word[1:]
        capWords.append(newWord)

    return ' '.join([elem for elem in capWords])

line = input()
print(capitalize(line))