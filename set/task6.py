uniqWords = set()
for i in range(int(input())):
    for word in input().split():
        uniqWords.add(word)

print(len(uniqWords))
