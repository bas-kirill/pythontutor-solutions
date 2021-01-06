n = int(input())

d = {}
for i in range(n):
    candidate, votes = input().split()
    d[candidate] = d.get(candidate, 0) + int(votes)

# My solution:
# d_sorted = list(d.items())
# d_sorted.sort()
#
# for key, item in dict(d_sorted).items():
#     print(key, item)

# Author's solution
for candidate, votes in sorted(d.items()):
    print(candidate, votes)