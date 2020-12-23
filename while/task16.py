x = int(input())
prev = -1
maxLenSeq = 1
lenSeq = 1
while x != 0:
    if prev == x:
        lenSeq += 1
    else:
        maxLenSeq = max(maxLenSeq, lenSeq)
        lenSeq = 1
        prev = x
    x = int(input())
maxLenSeq = max(maxLenSeq, lenSeq)
print(maxLenSeq)