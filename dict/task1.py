words = input().split()

counter = {}
# own's solution
# for word in words:
#     if word in counter:
#         counter[word] += 1
#         print(counter[word], end=' ')
#     else:
#         counter[word] = 0
#         print(0, end=' ')

# Author's solution
for word in words:
    counter[word] = counter.get(word, 0) + 1
    print(counter[word] - 1, end=' ')