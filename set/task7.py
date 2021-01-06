n = int(input())

numbers = [False] * (n + 1)

inp = input()
while inp != 'HELP':
    print(inp)
    if inp == 'HELP':
        break
    a = [int(elem) for elem in inp.split(' ')]
    command = input()
    for i in range(1, n + 1):
        for elem in a:
            if elem == i:
                if command == 'YES':
                    numbers[i] = True
                else:
                    numbers[i] = False
    inp = input()

for i in range(1, n + 1):
    if numbers[i]:
        print(i)