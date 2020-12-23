str = input()
n = len(str)
mid = n//2 + int(n % 2)
firstHalf = str[0:mid]
secondHalf = str[mid:]
print(secondHalf, firstHalf, sep='')