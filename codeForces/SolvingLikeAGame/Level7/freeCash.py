n = int(input())

hashSet = {}

for _ in range(n):
    h, m = map(int, input().split())

    tup = (h, m)

    if tup in hashSet: hashSet[tup]+=1

    else: hashSet[tup] = 1


res = 0

for key in hashSet.keys():
    res = max(res, hashSet[key])


print(res)