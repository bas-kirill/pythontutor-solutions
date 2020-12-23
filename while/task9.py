x = int(input())
mx = x
mxIdx = 0
idx = 0
while x != 0:
    if x > mx:
        mx = x
        mxIdx = idx
    idx += 1
    x = int(input())
else:
    print(mxIdx)