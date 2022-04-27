import math

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())

    arr = list(map(int, input().split()))

    hashSet = {}

    i = 0

    while i < n:
        curr = i

        while i < n and  arr[i] == arr[curr]: i+=1

        print(curr, i)
        if i < n:

            normalSteps = math.ceil((n - curr)/k)

            currSteps = math.ceil((n-i)/k)

            reducedSteps = abs(currSteps- normalSteps)

            # print(arr[curr], reducedSteps)

            if arr[curr] in hashSet: hashSet[arr[curr]]+= reducedSteps

            else: hashSet[arr[curr]] = reducedSteps
        

    
    

    print(hashSet)
    

    res = 0

    for key in hashSet.keys():
        res = max(res, hashSet[key])

    
    totalSteps = math.ceil(n/k)

    print(totalSteps- res)