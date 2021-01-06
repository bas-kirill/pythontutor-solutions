class1 = int(input())
class2 = int(input())
class3 = int(input())

schoolDesks1 = class1 // 2 + class1 % 2
schoolDesks2 = class2 // 2 + class2 % 2
schoolDesks3 = class3 // 2 + class3 % 2

ans = schoolDesks1 + schoolDesks2 + schoolDesks3
print(ans)