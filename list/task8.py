a = [int(elem) for elem in input().split(' ')]

unique = []
for elem in a:
    if elem not in unique:
        unique.append(elem)

print(len(unique))

